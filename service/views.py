import json
import jwt
import datetime
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.contrib.auth.hashers import check_password
from django.conf import settings
from functools import wraps
from .models import Usuario, Proyecto, Contacto, Tool, Categoria, BlacklistedToken

def generate_jwt(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=24),
        'iat': datetime.datetime.now(datetime.timezone.utc)
    }
    return jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

def jwt_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.method in ["OPTIONS", "GET"]:
            return view_func(request, *args, **kwargs)
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return json_response({'error': 'No se proporcionó un token válido'}, status=401)
        token = auth_header.split(' ')[1]
        if BlacklistedToken.objects.filter(token=token).exists():
            return json_response({'error': 'Token en lista negra'}, status=401)
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
            request.user_id = payload['user_id']
        except jwt.ExpiredSignatureError:
            return json_response({'error': 'Token expirado'}, status=401)
        except jwt.InvalidTokenError:
            return json_response({'error': 'Token inválido'}, status=401)
        return view_func(request, *args, **kwargs)
    return _wrapped_view


def json_response(data, status=200):
    response = JsonResponse(data, status=status, safe=False)
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, POST, PUT, DELETE, OPTIONS"
    response["Access-Control-Allow-Headers"] = "Content-Type"
    return response


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def login(request):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        return json_response({'success': False, 'error': 'Formato JSON inválido'}, status=400)

    correo = data.get('correo') or data.get('email')
    contrasena = data.get('contraseña') or data.get('contrasena') or data.get('password')

    if not correo or not contrasena:
        return json_response({
            'success': False,
            'error': 'Por favor, ingrese correo y contraseña'
        }, status=400)

    user = Usuario.objects.filter(correo=correo).first()

    if user and (check_password(contrasena, user.contrasena) or user.contrasena == contrasena):
        token = generate_jwt(user.id)
        return json_response({
            'success': True,
            'message': 'Inicio de sesión exitoso',
            'token': token,
            'user': {
                'id': user.id,
                'correo': user.correo
            }
        }, status=200)
    else:
        return json_response({
            'success': False,
            'error': 'Credenciales incorrectas. Verifique su correo y contraseña.'
        }, status=401)


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def logout(request):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})
    auth_header = request.headers.get('Authorization')
    if auth_header and auth_header.startswith('Bearer '):
        token = auth_header.split(' ')[1]
        BlacklistedToken.objects.get_or_create(token=token)
    return json_response({'success': True, 'message': 'Sesión cerrada exitosamente'})


# ==============================================================================
# CRUD 1: PROYECTOS
# ==============================================================================

def proyecto_to_dict(p):
    return {
        'id': p.id,
        'nombre': p.nombre or '',
        'descripcion': p.descripcion or '',
        'herramientas': p.herramientas if p.herramientas is not None else [],
        'demo': p.demo or '',
        'github': p.github or '',
        'estado': bool(p.estado) if p.estado is not None else True,
        'reto': p.reto or ''
    }


@csrf_exempt
@jwt_required
def proyectos_api(request, pk=None):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})

    if request.method == "GET":
        if pk:
            p = Proyecto.objects.filter(pk=pk).first()
            if not p:
                return json_response({'error': 'Proyecto no encontrado'}, status=404)
            return json_response(proyecto_to_dict(p))
        proyectos = [proyecto_to_dict(p) for p in Proyecto.objects.all().order_by('-id')]
        return json_response(proyectos)

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        p = Proyecto.objects.create(
            nombre=data.get('nombre', ''),
            descripcion=data.get('descripcion', ''),
            herramientas=data.get('herramientas', []),
            demo=data.get('demo', ''),
            github=data.get('github', ''),
            estado=data.get('estado', True),
            reto=data.get('reto', '')
        )
        return json_response({'message': 'Proyecto creado', 'id': p.id}, status=201)

    elif request.method == "PUT":
        if not pk:
            return json_response({'error': 'Falta ID para actualizar'}, status=400)
        p = Proyecto.objects.filter(pk=pk).first()
        if not p:
            return json_response({'error': 'Proyecto no encontrado'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        p.nombre = data.get('nombre', p.nombre)
        p.descripcion = data.get('descripcion', p.descripcion)
        p.herramientas = data.get('herramientas', p.herramientas)
        p.demo = data.get('demo', p.demo)
        p.github = data.get('github', p.github)
        p.estado = data.get('estado', p.estado)
        p.reto = data.get('reto', p.reto)
        p.save()
        return json_response({'message': 'Proyecto actualizado'})

    elif request.method == "DELETE":
        if not pk:
            return json_response({'error': 'Falta ID para eliminar'}, status=400)
        p = Proyecto.objects.filter(pk=pk).first()
        if not p:
            return json_response({'error': 'Proyecto no encontrado'}, status=404)
        p.delete()
        return json_response({'message': 'Proyecto eliminado'})

    return json_response({'error': 'Método no permitido'}, status=405)


# ==============================================================================
# CRUD 2: CONTACTOS
# ==============================================================================

def contacto_to_dict(c):
    return {
        'id': c.id,
        'correo': c.correo or '',
        'link': c.link or '',
        'github': c.github or ''
    }

@csrf_exempt
@jwt_required
def contacto_api(request, pk=None):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})

    if request.method == "GET":
        if pk:
            c = Contacto.objects.filter(pk=pk).first()
            if not c:
                return json_response({'error': 'Contacto no encontrado'}, status=404)
            return json_response(contacto_to_dict(c))
        contactos = [contacto_to_dict(c) for c in Contacto.objects.all().order_by('id')]
        return json_response(contactos)

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)
        c = Contacto.objects.create(
            correo=data.get('correo', ''),
            link=data.get('link', ''),
            github=data.get('github', '')
        )
        return json_response({'message': 'Contacto creado', 'id': c.id}, status=201)

    elif request.method == "PUT":
        if not pk:
            return json_response({'error': 'Falta ID'}, status=400)
        c = Contacto.objects.filter(pk=pk).first()
        if not c:
            return json_response({'error': 'Contacto no encontrado'}, status=404)
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        c.correo = data.get('correo', c.correo)
        c.link = data.get('link', c.link)
        c.github = data.get('github', c.github)
        c.save()
        return json_response({'message': 'Contacto actualizado'})

    elif request.method == "DELETE":
        if not pk:
            return json_response({'error': 'Falta ID'}, status=400)
        c = Contacto.objects.filter(pk=pk).first()
        if not c:
            return json_response({'error': 'Contacto no encontrado'}, status=404)
        c.delete()
        return json_response({'message': 'Contacto eliminado'})

    return json_response({'error': 'Método no permitido'}, status=405)


# ==============================================================================
# CRUD 3: TOOL
# ==============================================================================

def tool_to_dict(t):
    return {
        'id': t.id,
        'area': t.area or '',
        'herramientas': t.herramientas or '',
        'id_categorias': t.id_categorias_id,
        'categoria_nombre': t.id_categorias.nombre if t.id_categorias else '',
        'progreso': t.progreso if t.progreso is not None else 0
    }


@csrf_exempt
@jwt_required
def tools_api(request, pk=None):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})

    if request.method == "GET":
        if pk:
            t = Tool.objects.select_related('id_categorias').filter(pk=pk).first()
            if not t:
                return json_response({'error': 'Tool no encontrada'}, status=404)
            return json_response(tool_to_dict(t))
        tools = [tool_to_dict(t) for t in Tool.objects.select_related('id_categorias').all().order_by('-id')]
        return json_response(tools)

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        cat_id = data.get('id_categorias')
        categoria = Categoria.objects.filter(pk=cat_id).first() if cat_id else None

        t = Tool.objects.create(
            area=data.get('area', ''),
            herramientas=data.get('herramientas', ''),
            id_categorias=categoria,
            progreso=data.get('progreso', 0)
        )
        return json_response(tool_to_dict(t), status=201)

    elif request.method in ["PUT", "PATCH"]:
        if not pk:
            return json_response({'error': 'ID requerido para actualizar'}, status=400)
        t = Tool.objects.filter(pk=pk).first()
        if not t:
            return json_response({'error': 'Tool no encontrada'}, status=404)

        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        if 'area' in data:
            t.area = data['area']
        if 'herramientas' in data:
            t.herramientas = data['herramientas']
        if 'id_categorias' in data:
            cat_id = data['id_categorias']
            t.id_categorias = Categoria.objects.filter(pk=cat_id).first() if cat_id else None
        if 'progreso' in data:
            t.progreso = data['progreso']

        t.save()
        return json_response(tool_to_dict(t))

    elif request.method == "DELETE":
        if not pk:
            return json_response({'error': 'ID requerido para eliminar'}, status=400)
        t = Tool.objects.filter(pk=pk).first()
        if not t:
            return json_response({'error': 'Tool no encontrada'}, status=404)
        t.delete()
        return json_response({'message': 'Tool eliminada correctamente'})

    return json_response({'error': 'Método no permitido'}, status=405)


# ==============================================================================
# CATEGORIAS API (Auxiliar para Tools)
# ==============================================================================

@csrf_exempt
@jwt_required
def categorias_api(request):
    if request.method == "OPTIONS":
        return json_response({'status': 'ok'})

    if request.method == "GET":
        cats = [{'id': c.id, 'nombre': c.nombre or ''} for c in Categoria.objects.all().order_by('nombre')]
        return json_response(cats)

    elif request.method == "POST":
        try:
            data = json.loads(request.body.decode('utf-8'))
        except Exception:
            return json_response({'error': 'JSON inválido'}, status=400)

        nombre = data.get('nombre', '')
        c = Categoria.objects.create(nombre=nombre)
        return json_response({'id': c.id, 'nombre': c.nombre}, status=201)

    return json_response({'error': 'Método no permitido'}, status=405)




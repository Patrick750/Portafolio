import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from .models import Usuario


@csrf_exempt
@require_http_methods(["POST", "OPTIONS"])
def login(request):
    if request.method == "OPTIONS":
        response = JsonResponse({'status': 'ok'})
        response["Access-Control-Allow-Origin"] = "*"
        response["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    try:
        data = json.loads(request.body.decode('utf-8'))
    except Exception:
        response = JsonResponse({'success': False, 'error': 'Formato JSON inválido'}, status=400)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    correo = data.get('correo') or data.get('email')
    contrasena = data.get('contraseña') or data.get('contrasena') or data.get('password')

    if not correo or not contrasena:
        response = JsonResponse({
            'success': False,
            'error': 'Por favor, ingrese correo y contraseña'
        }, status=400)
        response["Access-Control-Allow-Origin"] = "*"
        return response

    user = Usuario.objects.filter(correo=correo, contrasena=contrasena).first()

    if user:
        response = JsonResponse({
            'success': True,
            'message': 'Inicio de sesión exitoso',
            'user': {
                'id': user.id,
                'correo': user.correo
            }
        }, status=200)
    else:
        response = JsonResponse({
            'success': False,
            'error': 'Credenciales incorrectas. Verifique su correo y contraseña.'
        }, status=401)

    response["Access-Control-Allow-Origin"] = "*"
    return response


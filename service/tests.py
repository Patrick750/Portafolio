import json
from django.test import TestCase, Client
from .models import Usuario


class LoginApiTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = Usuario.objects.create(
            correo="admin@ejemplo.com",
            contrasena="secreto123"
        )

    def test_login_exitoso(self):
        response = self.client.post(
            '/login/',
            data=json.dumps({
                'correo': 'admin@ejemplo.com',
                'contrasena': 'secreto123'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertTrue(data['success'])
        self.assertEqual(data['user']['correo'], 'admin@ejemplo.com')

    def test_login_credenciales_incorrectas(self):
        response = self.client.post(
            '/login/',
            data=json.dumps({
                'correo': 'admin@ejemplo.com',
                'contrasena': 'clave_erronea'
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 401)
        data = response.json()
        self.assertFalse(data['success'])
        self.assertIn('Credenciales incorrectas', data['error'])

    def test_login_campos_incompletos(self):
        response = self.client.post(
            '/login/',
            data=json.dumps({
                'correo': ''
            }),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, 400)
        data = response.json()
        self.assertFalse(data['success'])


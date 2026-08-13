from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password
from service.models import Usuario


class Command(BaseCommand):
    help = 'Guarda o actualiza las credenciales de usuario con contraseña encriptada'

    def add_arguments(self, parser):
        parser.add_argument('--correo', type=str, default='ortizpatrick750@gmail.com', help='Correo del usuario')
        parser.add_argument('--password', type=str, default='pac131pap&', help='Contraseña del usuario')

    def handle(self, *args, **options):
        correo = options['correo']
        raw_password = options['password']
        hashed_password = make_password(raw_password)

        usuario, created = Usuario.objects.update_or_create(
            correo=correo,
            defaults={'contrasena': hashed_password}
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS(f"Usuario '{correo}' creado exitosamente con contraseña encriptada.")
            )
        else:
            self.stdout.write(
                self.style.SUCCESS(f"Usuario '{correo}' actualizado exitosamente con contraseña encriptada.")
            )

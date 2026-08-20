import time
from django.db import connection
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Ejecuta todos los scripts de configuración inicial en orden automático'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.WARNING('⏳ Esperando a que la base de datos esté lista...'))
        db_conn = None
        for _ in range(15):
            try:
                connection.ensure_connection()
                db_conn = True
                break
            except OperationalError:
                time.sleep(1)

        if not db_conn:
            self.stdout.write(self.style.ERROR('❌ No se pudo conectar a la base de datos tras 15 segundos.'))
            return

        self.stdout.write(self.style.SUCCESS('🚀 Base de datos conectada. Iniciando ejecución de scripts...'))

        # Lista de comandos que queremos ejecutar secuencialmente. 
        # (Se omiten los duplicados si 'create_categorias' o 'create_user' están vacíos o deprecados)
        scripts_to_run = [
            'seed_categorias',
            'seed_skills',
            'create_usuario',
        ]

        for script in scripts_to_run:
            self.stdout.write(self.style.WARNING(f'⏳ Ejecutando: {script}...'))
            try:
                call_command(script)
                self.stdout.write(self.style.SUCCESS(f'✅ {script} ejecutado con éxito.\n'))
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'❌ Error al ejecutar {script}: {e}\n'))

        self.stdout.write(self.style.SUCCESS('🎉 ¡Todos los scripts han sido ejecutados!'))

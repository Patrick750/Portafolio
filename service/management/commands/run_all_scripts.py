from django.core.management.base import BaseCommand
from django.core.management import call_command

class Command(BaseCommand):
    help = 'Ejecuta todos los scripts de configuración inicial en orden automático'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('🚀 Iniciando ejecución de scripts automáticos...'))

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

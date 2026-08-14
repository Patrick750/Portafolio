from django.core.management.base import BaseCommand
from service.models import Categoria


class Command(BaseCommand):
    help = 'Pobla la tabla categorias con las categorías iniciales'

    def handle(self, *args, **options):
        categorias_iniciales = [
            'Data & Python',
            'Web Development',
            'Bases de Datos',
            'Herramientas & Metodologías'
        ]

        creadas = 0
        existentes = 0

        for nombre in categorias_iniciales:
            obj, created = Categoria.objects.get_or_create(nombre=nombre)
            if created:
                creadas += 1
                self.stdout.write(self.style.SUCCESS(f"Categoría creada: '{nombre}'"))
            else:
                existentes += 1
                self.stdout.write(f"Categoría ya existente: '{nombre}'")

        self.stdout.write(
            self.style.SUCCESS(
                f"\nProceso completado. {creadas} categorías creadas, {existentes} ya existían."
            )
        )

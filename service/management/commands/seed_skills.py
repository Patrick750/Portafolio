"""
Comando: seed_skills
=====================
Pobla la base de datos con categorías y habilidades curadas.

Uso:
  python manage.py seed_skills                   # Inserta sin duplicar
  python manage.py seed_skills --preview         # Solo muestra los datos, no inserta
  python manage.py seed_skills --reset           # Borra todo y re-siembra desde cero
  python manage.py seed_skills --reset --confirm # --reset sin prompt de confirmación
"""

from django.core.management.base import BaseCommand
from service.models import Categoria, Tool


# ==============================================================================
# DATOS CURADOS DE HABILIDADES
# ==============================================================================
SKILLS_DATA = [
    {
        "categoria": "Data & Analytics",
        "skills": [
            {
                "area": "Python Data Science",
                "herramientas": "Python, Pandas, NumPy, Polars, SciPy, Jupyter Notebooks",
                "progreso": 88,
            },
            {
                "area": "Análisis Exploratorio (EDA)",
                "herramientas": "Pandas Profiling, Estadística descriptiva, Data Cleaning, Feature Selection, Correlaciones",
                "progreso": 82,
            },
            {
                "area": "Visualización de Datos",
                "herramientas": "Matplotlib, Seaborn, Plotly, Chart.js, Storytelling con datos",
                "progreso": 75,
            },
            {
                "area": "Machine Learning Básico",
                "herramientas": "Scikit-learn, Regresión, Clasificación, Clustering, Feature Engineering",
                "progreso": 45,
            },
        ],
    },
    {
        "categoria": "Desarrollo Web",
        "skills": [
            {
                "area": "JavaScript Avanzado",
                "herramientas": "ES6+, Async/Await, Fetch API, DOM avanzado, Closures, Módulos, Promises",
                "progreso": 85,
            },
            {
                "area": "Vue.js 3",
                "herramientas": "Composition API, Reactivity, Vue Router, Pinia, Vite, SPA, Componentes",
                "progreso": 70,
            },
            {
                "area": "HTML & CSS Avanzado",
                "herramientas": "Semántica HTML5, CSS Grid, Flexbox, Animaciones CSS, Responsive Design, BEM",
                "progreso": 82,
            },
            {
                "area": "Django & REST Framework",
                "herramientas": "Django 6, Django REST, ORM, Auth, CRUD APIs, Migraciones, Middleware",
                "progreso": 68,
            },
        ],
    },
    {
        "categoria": "Bases de Datos",
        "skills": [
            {
                "area": "SQL Avanzado",
                "herramientas": "JOINs complejos, Subconsultas, Window Functions, CTEs, Índices, Optimización",
                "progreso": 88,
            },
            {
                "area": "PostgreSQL",
                "herramientas": "PostgreSQL 15, JSONB, Triggers, Particionamiento, pg_stat, Explain Analyze",
                "progreso": 78,
            },
            {
                "area": "Diseño de Bases de Datos",
                "herramientas": "Modelado ER, Normalización (1FN-3FN), Integridad referencial, Diagramas, ChartDB",
                "progreso": 85,
            },
            {
                "area": "NoSQL Básico",
                "herramientas": "MongoDB, Redis, Conceptos clave, Casos de uso, Comparativas",
                "progreso": 40,
            },
        ],
    },
    {
        "categoria": "DevOps & Tools",
        "skills": [
            {
                "area": "Git & Control de Versiones",
                "herramientas": "Git Flow, Branching strategies, Merge/Rebase, GitHub, Commits semánticos, PRs",
                "progreso": 72,
            },
            {
                "area": "Docker & Contenedores",
                "herramientas": "Docker, Docker Compose, Imágenes, Volúmenes, Redes, Multi-stage builds",
                "progreso": 55,
            },
            {
                "area": "Linux & Terminal",
                "herramientas": "Bash, Shell scripting, SSH, Permisos, Cron jobs, Procesos, Vim",
                "progreso": 65,
            },
            {
                "area": "Despliegue & VPS",
                "herramientas": "Nginx, Gunicorn, VPS, HTTPS/SSL, Certbot, Variables de entorno",
                "progreso": 52,
            },
        ],
    },
    {
        "categoria": "Metodologías",
        "skills": [
            {
                "area": "Scrum & Agile",
                "herramientas": "Scrum, Kanban, Sprints, Backlog refinement, Daily standups, Retrospectivas",
                "progreso": 75,
            },
            {
                "area": "Clean Architecture",
                "herramientas": "Principios SOLID, Capas, Separación de responsabilidades, DDD básico, Patrones",
                "progreso": 62,
            },
            {
                "area": "APIs RESTful",
                "herramientas": "Diseño REST, HTTP methods, Status codes, Autenticación JWT, CORS, Documentación",
                "progreso": 78,
            },
            {
                "area": "Testing",
                "herramientas": "Unit Testing, Pytest, Jest, TDD básico, Mocking, Coverage",
                "progreso": 40,
            },
        ],
    },
]


class Command(BaseCommand):
    help = "Pobla la DB con categorías y habilidades curadas de forma profesional"

    def add_arguments(self, parser):
        parser.add_argument(
            "--reset",
            action="store_true",
            help="Elimina todas las categorías y tools existentes antes de sembrar",
        )
        parser.add_argument(
            "--preview",
            action="store_true",
            help="Muestra los datos que se insertarían sin hacer cambios en la DB",
        )
        parser.add_argument(
            "--confirm",
            action="store_true",
            help="Confirma automáticamente el --reset sin prompt interactivo",
        )

    def handle(self, *args, **options):
        is_preview = options["preview"]
        is_reset = options["reset"]
        auto_confirm = options["confirm"]

        self._print_banner()

        if is_preview:
            self._run_preview()
            return

        if is_reset:
            if not auto_confirm:
                confirm = input(
                    self.style.WARNING(
                        "\n⚠  Esto eliminará TODAS las categorías y tools existentes. ¿Continuar? [s/N]: "
                    )
                )
                if confirm.strip().lower() not in ("s", "si", "yes", "y"):
                    self.stdout.write(self.style.ERROR("✗  Operación cancelada."))
                    return
            self._reset_db()

        self._seed()

    # --------------------------------------------------------------------------
    # PRIVATE
    # --------------------------------------------------------------------------

    def _print_banner(self):
        self.stdout.write("")
        self.stdout.write(self.style.MIGRATE_HEADING("━" * 60))
        self.stdout.write(self.style.MIGRATE_HEADING("  🚀  SEED SKILLS — Portafolio Patrick Ortiz"))
        self.stdout.write(self.style.MIGRATE_HEADING("━" * 60))
        self.stdout.write("")

    def _reset_db(self):
        cat_count  = Categoria.objects.count()
        tool_count = Tool.objects.count()
        Tool.objects.all().delete()
        Categoria.objects.all().delete()
        self.stdout.write(
            self.style.WARNING(
                f"  🗑  Reset completado: {cat_count} categorías y {tool_count} tools eliminadas."
            )
        )
        self.stdout.write("")

    def _seed(self):
        total_cats   = 0
        total_tools  = 0
        skip_cats    = 0
        skip_tools   = 0

        for group in SKILLS_DATA:
            cat_nombre = group["categoria"]
            cat_obj, cat_created = Categoria.objects.get_or_create(nombre=cat_nombre)

            if cat_created:
                total_cats += 1
                self.stdout.write(self.style.SUCCESS(f"  ✔  Categoría creada : {cat_nombre}"))
            else:
                skip_cats += 1
                self.stdout.write(f"  ─  Categoría existe : {cat_nombre}")

            for skill in group["skills"]:
                _, skill_created = Tool.objects.get_or_create(
                    area=skill["area"],
                    id_categorias=cat_obj,
                    defaults={
                        "herramientas": skill["herramientas"],
                        "progreso":     skill["progreso"],
                    },
                )

                level_label = (
                    "Avanzado"   if skill["progreso"] >= 80 else
                    "Intermedio" if skill["progreso"] >= 50 else
                    "En Estudio"
                )
                bar   = self._progress_bar(skill["progreso"])
                mark  = "✔" if skill_created else "─"
                style = self.style.SUCCESS if skill_created else str

                self.stdout.write(
                    style(
                        f"    {mark}  {skill['area']:<38} {bar}  {skill['progreso']:>3}%  [{level_label}]"
                    )
                )

                if skill_created:
                    total_tools += 1
                else:
                    skip_tools += 1

            self.stdout.write("")

        self._print_summary(total_cats, skip_cats, total_tools, skip_tools)

    def _run_preview(self):
        self.stdout.write(self.style.MIGRATE_HEADING("  👁  MODO PREVIEW — No se realizarán cambios\n"))

        for group in SKILLS_DATA:
            self.stdout.write(self.style.MIGRATE_HEADING(f"  📁  {group['categoria']}"))
            for skill in group["skills"]:
                level_label = (
                    "Avanzado"   if skill["progreso"] >= 80 else
                    "Intermedio" if skill["progreso"] >= 50 else
                    "En Estudio"
                )
                bar = self._progress_bar(skill["progreso"])
                self.stdout.write(
                    f"    •  {skill['area']:<38} {bar}  {skill['progreso']:>3}%  [{level_label}]"
                )
                self.stdout.write(
                    f"       Chips: {skill['herramientas'][:70]}{'...' if len(skill['herramientas']) > 70 else ''}"
                )
            self.stdout.write("")

        total_skills = sum(len(g["skills"]) for g in SKILLS_DATA)
        self.stdout.write(
            self.style.SUCCESS(
                f"  📊  Total a insertar: {len(SKILLS_DATA)} categorías, {total_skills} habilidades"
            )
        )

    def _print_summary(self, new_cats, skip_cats, new_tools, skip_tools):
        self.stdout.write(self.style.MIGRATE_HEADING("━" * 60))
        self.stdout.write(self.style.SUCCESS(f"  ✅  COMPLETADO"))
        self.stdout.write(
            f"     Categorías: {self.style.SUCCESS(str(new_cats))} creadas  /  {skip_cats} ya existían"
        )
        self.stdout.write(
            f"     Habilidades: {self.style.SUCCESS(str(new_tools))} creadas  /  {skip_tools} ya existían"
        )
        self.stdout.write(self.style.MIGRATE_HEADING("━" * 60))
        self.stdout.write("")

    @staticmethod
    def _progress_bar(progress: int, width: int = 16) -> str:
        """Genera una barra ASCII de progreso."""
        filled = round(progress / 100 * width)
        empty  = width - filled
        return f"[{'█' * filled}{'░' * empty}]"

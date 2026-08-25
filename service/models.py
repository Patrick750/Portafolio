from django.db import models


class Proyecto(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    herramientas = models.JSONField(null=True, blank=True)
    demo = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)
    estado = models.BooleanField(null=True, blank=True)
    reto = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'proyectos'

    def __str__(self):
        return self.nombre or f"Proyecto {self.pk}"


class Contacto(models.Model):
    correo = models.CharField(max_length=255, null=True, blank=True)
    link = models.CharField(max_length=255, null=True, blank=True)
    github = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'contacto'

    def __str__(self):
        return self.correo or f"Contacto {self.pk}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'categorias'

    def __str__(self):
        return self.nombre or f"Categoría {self.pk}"


class Tool(models.Model):
    area = models.CharField(max_length=255, null=True, blank=True)
    herramientas = models.CharField(max_length=255, null=True, blank=True)
    id_categorias = models.ForeignKey(
        Categoria,
        on_delete=models.CASCADE,
        db_column='id_categorias',
        related_name='tools',
        null=True,
        blank=True
    )
    progreso = models.IntegerField(default=0, null=True, blank=True)

    class Meta:
        db_table = 'tools'

    def __str__(self):
        return f"{self.area or 'Tool'} - {self.herramientas or self.pk}"


class Usuario(models.Model):
    correo = models.CharField(max_length=255, null=True, blank=True)
    contrasena = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.correo or f"Usuario {self.pk}"


class BlacklistedToken(models.Model):
    token = models.CharField(max_length=500, unique=True)
    blacklisted_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'blacklisted_tokens'

    def __str__(self):
        return self.token

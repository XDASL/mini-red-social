from django.db import models

# Constantes para mantener consistencia en los campos repetitivos
str_habilitado = "Habilitado"
str_fecha_creacion = "Fecha Creación"
str_fecha_actualizacion = "Fecha Actualización"


class PerfilAcceso(models.Model):
    nombre = models.CharField(
        "Nombre del Perfil", max_length=50
    )  # Ej: Administrador, Moderador, Usuario Base
    descripcion = models.CharField("Descripción", max_length=255, null=True)
    habilitado = models.BooleanField(str_habilitado, default=True)

    class Meta:
        db_table_comment = (
            "Gestión de perfiles de acceso al sistema (Público, Privado, Admin)."
        )


class Usuario(models.Model):
    rut = models.CharField("RUT", max_length=12, unique=True)
    nombre = models.CharField("Nombre Completo", max_length=150)
    correo = models.EmailField("Email", max_length=150, unique=True)
    contrasenia = models.CharField("Contraseña", max_length=128)
    perfil = models.ForeignKey(PerfilAcceso, on_delete=models.CASCADE)

    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)


class Publicacion(models.Model):
    ESTADOS_CHOICES = [
        ("Activa", "Activa"),
        ("Bloqueada", "Bloqueada por Moderación"),
        ("Archivada", "Archivada"),
    ]
    VISIBILIDAD_CHOICES = [("Publica", "Pública"), ("Privada", "Privada")]

    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    contenido = models.TextField("Contenido de la publicación")
    visibilidad = models.CharField(
        "Visibilidad", max_length=20, choices=VISIBILIDAD_CHOICES, default="Publica"
    )
    estado = models.CharField(
        "Estado del Registro", max_length=30, choices=ESTADOS_CHOICES, default="Activa"
    )

    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)
    updated_at = models.DateTimeField(str_fecha_actualizacion, auto_now=True)


class Interaccion(models.Model):
    TIPO_CHOICES = [
        ("Like", "Me Gusta"),
        ("Comentario", "Comentario"),
        ("Compartir", "Compartir"),
    ]

    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
    tipo_interaccion = models.CharField("Tipo", max_length=20, choices=TIPO_CHOICES)
    comentario = models.TextField("Texto del comentario", null=True, blank=True)

    habilitado = models.BooleanField(str_habilitado, default=True)
    created_at = models.DateTimeField(str_fecha_creacion, auto_now_add=True)

    class Meta:
        db_table_comment = "Registro de operaciones diarias e interacciones que afectan a la comunidad."


class RegistroAuditoria(models.Model):
    usuario_responsable = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, null=True
    )
    accion_realizada = models.CharField("Acción", max_length=100)
    tabla_afectada = models.CharField("Entidad Afectada", max_length=50)
    id_registro_afectado = models.IntegerField("ID del Registro")
    detalle = models.TextField("Detalle del evento o situación excepcional", null=True)

    fecha_evento = models.DateTimeField(str_fecha_creacion, auto_now_add=True)

    class Meta:
        db_table_comment = (
            "Bitácora para auditoría de cambios de estado y situaciones excepcionales."
        )

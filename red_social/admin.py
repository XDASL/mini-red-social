from django.contrib import admin
from .models import PerfilAcceso, Usuario, Publicacion, Interaccion, RegistroAuditoria

admin.site.register(PerfilAcceso)
admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Interaccion)
admin.site.register(RegistroAuditoria)

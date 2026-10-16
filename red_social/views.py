from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from django.utils import timezone
from .models import PerfilAcceso, Usuario, Publicacion, Interaccion, RegistroAuditoria
from .serializers import (
    PerfilAccesoSerializer,
    UsuarioSerializer,
    PublicacionSerializer,
    InteraccionSerializer,
    RegistroAuditoriaSerializer,
)


def bienvenida(request):
    return render(request, "bienvenida.html")


class PerfilAccesoViewSet(viewsets.ModelViewSet):
    queryset = PerfilAcceso.objects.all()
    serializer_class = PerfilAccesoSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer


class PublicacionViewSet(viewsets.ModelViewSet):
    queryset = Publicacion.objects.filter(habilitado=True)  # Solo muestra las activas
    serializer_class = PublicacionSerializer

    def destroy(self, request, *args, **kwargs):
        publicacion = self.get_object()

        publicacion.estado = "Archivada"
        publicacion.habilitado = False
        publicacion.save()

        RegistroAuditoria.objects.create(
            usuario_responsable=publicacion.autor,
            accion_realizada="Publicación Archivada/Eliminada por API",
            tabla_afectada="Publicacion",
            id_registro_afectado=publicacion.id,
            detalle=f"La publicación '{publicacion.contenido[:20]}...' fue archivada.",
        )

        return Response(
            {"mensaje": "Publicación archivada y auditada correctamente."},
            status=status.HTTP_204_NO_CONTENT,
        )


class InteraccionViewSet(viewsets.ModelViewSet):
    queryset = Interaccion.objects.all()
    serializer_class = InteraccionSerializer


class RegistroAuditoriaViewSet(viewsets.ModelViewSet):
    queryset = RegistroAuditoria.objects.all()
    serializer_class = RegistroAuditoriaSerializer

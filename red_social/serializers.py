from rest_framework import serializers
from .models import PerfilAcceso, Usuario, Publicacion, Interaccion, RegistroAuditoria


class PerfilAccesoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PerfilAcceso
        fields = "__all__"


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = "__all__"


class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicacion
        fields = "__all__"


class InteraccionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interaccion
        fields = "__all__"


class RegistroAuditoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroAuditoria
        fields = "__all__"

from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r"perfiles", views.PerfilAccesoViewSet)
router.register(r"usuarios", views.UsuarioViewSet)
router.register(r"publicaciones", views.PublicacionViewSet)
router.register(r"interacciones", views.InteraccionViewSet)
router.register(r"auditoria", views.RegistroAuditoriaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

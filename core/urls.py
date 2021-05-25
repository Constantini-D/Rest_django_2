from django.urls import include, path
from rest_framework import routers
from .views import SorveteViewSet, AvaliacaoViewSet

router = routers.DefaultRouter()
router.register(r'sorvete', SorveteViewSet)
router.register(r'avaliacao', AvaliacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
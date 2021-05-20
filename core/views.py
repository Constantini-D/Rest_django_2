from django.shortcuts import render

from rest_framework import viewsets

from .serializers import SorveteSerializer
from .models import Sorvete


class SorveteViewSet(viewsets.ModelViewSet):
    queryset = Sorvete.objects.all().order_by('nome')   # verificiar a ordenação
    serializer_class = SorveteSerializer




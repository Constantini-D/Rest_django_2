from django.shortcuts import render

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .serializers import SorveteSerializer, AvaliacaoSerializer
from .models import Sorvete, Avaliacao


class SorveteViewSet(viewsets.ModelViewSet):
    queryset = Sorvete.objects.all().order_by('id')   # verificiar a ordenação
    serializer_class = SorveteSerializer

    @action(detail=True, methods=['get'])
    def avaliacoes(self, request, pk= None):
        sorvete = self.get_object()
        serializer = AvaliacaoSerializer(sorvete.avaliacoes.all(), many=True)
        return Response(serializer.data)


class AvaliacaoViewSet(viewsets.ModelViewSet):
    queryset = Avaliacao.objects.all().order_by('nota')   # verificiar a ordenação
    serializer_class = AvaliacaoSerializer




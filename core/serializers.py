from rest_framework import serializers
from .models import Sorvete, Avaliacao


class SorveteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sorvete
        fields = ('id', 'nome', 'preco')


class AvaliacaoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'sorvete', 'cliente', 'nota', 'comentario')
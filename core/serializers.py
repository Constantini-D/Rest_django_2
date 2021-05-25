from rest_framework import serializers
from .models import Sorvete, Avaliacao


class SorveteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sorvete
        fields = ('id', 'nome', 'preco')


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = ('id', 'sorvete', 'cliente', 'nota', 'comentario')
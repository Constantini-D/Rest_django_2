from rest_framework import serializers
from .models import Sorvete


class SorveteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Sorvete
        fields = ('nome', 'preco')
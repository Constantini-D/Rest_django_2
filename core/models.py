from django.db import models


class Sorvete(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Sorvete'
        verbose_name_plural = 'Sorvetes'

    def __str__(self):
        return self.nome


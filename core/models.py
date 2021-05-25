from django.db import models


class Sorvete(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Sorvete'
        verbose_name_plural = 'Sorvetes'

    def __str__(self):
        return self.nome


class Avaliacao(models.Model):
    sorvete = models.ForeignKey(Sorvete, related_name='avaliacoes', on_delete=models.CASCADE)
    cliente = models.CharField(max_length=100)
    nota = models.DecimalField(max_digits=2, decimal_places=0)
    comentario = models.TextField(blank=True, default='')

    class Meta:
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'

    def __str__(self):
        return f'{self.cliente} avaliou com a nota {self.nota} o sorvete {Sorvete.nome}'
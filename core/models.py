from django.db import models
from django.utils import timezone

# Create your models here.

class Cliente(models.Model):
    cnpj = models.ForeignKey('auth.user',on_delete=models.CASCADE)
    razao = models.CharField(max_length=200)
    solicitante = models.CharField(max_length=200)

    def __str__(self):
        return self.cnpj

class Chamado(models.Model):
    numero_chamado = models.ForeignKey
    data_abertura = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.numero_chamado



class Tecnico(models.Model):
    codigo = models.ForeignKey
    nome =models.CharField(max_length=200)

    def __str__(self):
        return self.nome

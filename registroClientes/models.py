from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=70)
    sobrenome = models.CharField(max_length=70)
    idade = models.IntegerField()
    email = models.EmailField(max_length=70, unique=True)
    dataNascimento = models.DateField()
    apelido = models.CharField(max_length=70, blank=True)
    observacao = models.TextField(max_length=1000, blank=True)

    def __str__(self):
        return self.nome

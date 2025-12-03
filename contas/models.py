from django.contrib.auth.models import User
from django.db import models


class VoluntarioProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_voluntario")
    nome_completo = models.CharField(max_length=150)
    telefone = models.CharField(max_length=20, blank=True)
    interesses = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nome_completo} (Voluntário)"


class OrganizacaoProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="perfil_organizacao")
    nome_organizacao = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    site = models.URLField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome_organizacao

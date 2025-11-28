from django.db import models
from django.contrib.auth.models import AbstractUser

# ===== Usuário personalizado =====
class Usuario(AbstractUser):
    TIPOS_CONTA = [
        ('voluntario', 'Voluntário'),
        ('organizacao', 'Organização'),
    ]

    nome_completo = models.CharField(max_length=150)
    tipo_conta = models.CharField(max_length=20, choices=TIPOS_CONTA, default='voluntario')
    email = models.EmailField(unique=True)

    # Usamos o e-mail como identificador principal
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'nome_completo', 'tipo_conta']

    def __str__(self):
        return f"{self.nome_completo} ({self.get_tipo_conta_display()})"


# ===== Modelo para Mensagens de Contato =====
class Contato(models.Model):
    nome = models.CharField(max_length=120)
    email = models.EmailField()
    mensagem = models.TextField()
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Mensagem de {self.nome} - {self.email}"


# ===== Modelo para Organizações (perfil detalhado) =====
class Organizacao(models.Model):
    usuario = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil_organizacao')
    nome_ong = models.CharField(max_length=150)
    descricao = models.TextField(blank=True)
    site = models.URLField(blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.nome_ong


# ===== Modelo para Vagas de Voluntariado =====
class VagaVoluntariado(models.Model):
    organizacao = models.ForeignKey(Organizacao, on_delete=models.CASCADE, related_name='vagas')
    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    localizacao = models.CharField(max_length=120)
    data_evento = models.DateField(null=True, blank=True)
    vagas_disponiveis = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.titulo} ({self.organizacao.nome_ong})"

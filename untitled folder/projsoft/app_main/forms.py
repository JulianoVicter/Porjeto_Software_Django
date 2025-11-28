from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Usuario, Contato


# ===== Formulário de Criação de Conta =====
class UsuarioForm(UserCreationForm):
    nome_completo = forms.CharField(
        label="Nome completo",
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome completo'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'seu@exemplo.com'})
    )
    tipo_conta = forms.ChoiceField(
        label="Tipo de conta",
        choices=Usuario.TIPOS_CONTA,
        widget=forms.RadioSelect
    )

    class Meta:
        model = Usuario
        fields = ['nome_completo', 'email', 'password1', 'password2', 'tipo_conta']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.nome_completo = self.cleaned_data['nome_completo']
        user.email = self.cleaned_data['email']
        user.tipo_conta = self.cleaned_data['tipo_conta']
        user.username = user.email  # username = e-mail
        if commit:
            user.save()
        return user


# ===== Formulário de Contato =====
class ContatoForm(forms.ModelForm):
    nome = forms.CharField(
        label="Nome",
        widget=forms.TextInput(attrs={'placeholder': 'Seu nome'})
    )
    email = forms.EmailField(
        label="E-mail",
        widget=forms.EmailInput(attrs={'placeholder': 'seu@exemplo.com'})
    )
    mensagem = forms.CharField(
        label="Mensagem",
        widget=forms.Textarea(attrs={'placeholder': 'Como podemos ajudar?', 'rows': 4})
    )

    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']

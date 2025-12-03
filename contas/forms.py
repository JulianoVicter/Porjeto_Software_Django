from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

from .models import OrganizacaoProfile, VoluntarioProfile


class BaseSignupForm(UserCreationForm):
    email = forms.EmailField(label="E-mail", required=True)
    nome_completo = forms.CharField(label="Nome completo", max_length=150)
    telefone = forms.CharField(label="Telefone", max_length=20, required=False)

    class Meta:
        model = User
        fields = ("email", "password1", "password2")

    def save_user(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data["email"]
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class VoluntarioSignupForm(BaseSignupForm):
    interesses = forms.CharField(
        label="Áreas de interesse", required=False, widget=forms.Textarea(attrs={"rows": 3})
    )

    def save(self, commit=True):
        user = self.save_user(commit=commit)
        if commit:
            VoluntarioProfile.objects.create(
                user=user,
                nome_completo=self.cleaned_data["nome_completo"],
                telefone=self.cleaned_data.get("telefone", ""),
                interesses=self.cleaned_data.get("interesses", ""),
            )
        else:
            # Para o caso de commit=False mantemos a instância preparada
            self._pending_profile = VoluntarioProfile(
                user=user,
                nome_completo=self.cleaned_data["nome_completo"],
                telefone=self.cleaned_data.get("telefone", ""),
                interesses=self.cleaned_data.get("interesses", ""),
            )
        return user


class OrganizacaoSignupForm(BaseSignupForm):
    nome_organizacao = forms.CharField(label="Nome da organização", max_length=150)
    descricao = forms.CharField(label="Descrição", widget=forms.Textarea(attrs={"rows": 3}), required=False)
    site = forms.URLField(label="Site", required=False)

    def save(self, commit=True):
        user = self.save_user(commit=commit)
        if commit:
            OrganizacaoProfile.objects.create(
                user=user,
                nome_organizacao=self.cleaned_data["nome_organizacao"],
                descricao=self.cleaned_data.get("descricao", ""),
                site=self.cleaned_data.get("site", ""),
                telefone=self.cleaned_data.get("telefone", ""),
            )
        else:
            self._pending_profile = OrganizacaoProfile(
                user=user,
                nome_organizacao=self.cleaned_data["nome_organizacao"],
                descricao=self.cleaned_data.get("descricao", ""),
                site=self.cleaned_data.get("site", ""),
                telefone=self.cleaned_data.get("telefone", ""),
            )
        return user


class LoginForm(AuthenticationForm):
    username = forms.CharField(label="Usuário ou e-mail")
    password = forms.CharField(label="Senha", widget=forms.PasswordInput)

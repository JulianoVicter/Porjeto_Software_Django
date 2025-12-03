from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import OrganizacaoProfile, VoluntarioProfile


class VoluntarioInline(admin.StackedInline):
    model = VoluntarioProfile
    can_delete = False
    verbose_name_plural = 'Voluntários'
    fk_name = 'user'


class OrganizacaoInline(admin.StackedInline):
    model = OrganizacaoProfile
    can_delete = False
    verbose_name_plural = 'Organizações'
    fk_name = 'user'


class UsuarioAdmin(UserAdmin):
    inlines = [VoluntarioInline, OrganizacaoInline]
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')


admin.site.unregister(User)
admin.site.register(User, UsuarioAdmin)
admin.site.register(VoluntarioProfile)
admin.site.register(OrganizacaoProfile)

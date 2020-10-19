from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUsuarioCreateForm, CustomUsuarioChangeForm
from .models import CustomUsuario


@admin.register(CustomUsuario)
class CustomUsuarioAdmin(UserAdmin):
    add_form = CustomUsuarioCreateForm  # Formulário para criar Usuário
    form = CustomUsuarioChangeForm  # Formulário para editar Usuário
    model = CustomUsuario
    list_display = ('first_name', 'last_name', 'email', 'fone', 'is_staff')  # O que mostrar na tabela.

    fieldsets = (  # Dados de cadastro de usuário. Olhar o Django Admin para entender
        (None, {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('first_name', 'last_name', 'fone')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas Importantes', {'fields': ('last_login', 'date_joined')})
    )

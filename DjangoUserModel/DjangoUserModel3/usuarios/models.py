from django.db import models
# from django.contrib.auth.models import AbstractBaseUser  # Esse aqui é muito básico, não tem todas as funções
from django.contrib.auth.models import AbstractUser  # Esse tem funcionalidade prontas! O MELHOR!!!
from django.contrib.auth.models import BaseUserManager  # Criar um gerenciador para o usuário que vamos criar.


class UsuarioManager(BaseUserManager):
    user_in_migrations = True  # O model vai ser utilizado em migrations. Sem isso não vira tabela no BD.

    # Criar usuário
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("O e-mail é obrigatório")  # Corrigir maisculas/minusculas, retirar caracteres especiais...
        email = self.normalize_email(email)
        user = self.model(email=email, username=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return

    # Cria um usuário comum
    def create_user(self, email, password=None, **extra_field):
        # extra_field.setdefault('is_staff', True)  # Setando True para is_staff.
        extra_field.setdefault('is_superuser', False)  # Setando false para o is_superuser.
        return self._create_user(email, password, **extra_field)

    # Cria um super usuário
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError("Superuser precisa ter is_superuser=True")
        if extra_fields.get('is_staff') is not True:
            raise ValueError("Superuser precisa ter is_staff=True")

        return self._create_user(email, password, **extra_fields)


class CustomUsuario(AbstractUser):
    email = models.EmailField("E-mail", unique=True)  # Precisa ser único.
    fone = models.CharField("Telefone", max_length=15)
    is_staff = models.BooleanField("Membro da equipe", default=True)

    USERNAME_FIELD = 'email'  # O email vai ser o próprio username
    REQUIRED_FIELDS = ['first_name', 'last_name', 'fone']  # O próprio sistema exigir email e senha por padrão

    def __str__(self):
        return self.email

    objects = UsuarioManager()  # Indica que o UsuarioManager gerencia os objetos do model CustomUsuario

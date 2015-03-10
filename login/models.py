# -*- coding: utf-8 -*-

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class UsuarioManager(BaseUserManager):
    def create_user(self, email, username=None, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """        
        if not email:
            raise ValueError('e-mail é obrigatório!')

        if not password:
            raise ValueError('Senha inválida!')

        user = self.model(
            email=self.normalize_email(email)            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email,
            password=password            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Usuario(AbstractBaseUser):

    email = models.EmailField(
        verbose_name='e-mail',
        max_length=255,
        unique=True,
        db_index=True,
        error_messages={"unique" : u'Já existe cadastro com este e-mail. Caso perdeu sua senha, use o esqueci minha senha na tela inicial'},
    )

    username = models.CharField(max_length=100)

    typeaccount = models.CharField(max_length=20,blank=True)
    photo = models.CharField(max_length=200, blank=True)

    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    is_staff = models.BooleanField(('staff status'), default=False)

    is_active = models.BooleanField(('active'), default=True)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return True
    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_name(self):
        return self.username    

    def get_birthday(self):
        return self.birthday

    def get_typeaccount(self):
        return self.typeaccount

    def get_photo(self):
        return self.photo

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    # On Python 3: def __str__(self):
    def __unicode__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin

from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# id (primary key - automático)
# first_name (string), last_name (string), phone (string)
# email (email), created_date (date), description (text)
# category (foreign key), show (boolean), picture (imagem)

# Depois
# owner (foreign key)


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='Nome')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'

    

class Contact(models.Model):
    first_name = models.CharField(max_length=50,verbose_name='Nome')
    
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Sobrenome')
   
    phone = models.CharField(max_length=50, verbose_name='Telefone')
   
    email = models.EmailField(max_length=50, verbose_name='E-mail')
   
    created_date = models.DateTimeField(default=timezone.now, verbose_name='Data de Criação')
   
    description = models.TextField(blank=True, verbose_name='Descrição')
    
    show = models.BooleanField(default=True, verbose_name='Exibir')
    
    picture = models.ImageField(blank=True, upload_to='pictures/%Y/%m/', verbose_name='Foto')

    category = models.ForeignKey(Category, 
                                 on_delete=models.SET_NULL,
                                 blank= True, null = True,
                                 verbose_name='Categoria'
                                 )
    
    owner =models.ForeignKey(User, 
                            on_delete=models.SET_NULL,
                            blank= True, null = True,
                            verbose_name='Usuario'
                                 )
    

    # def clean(self):
    #     super().clean()
    #     if not self.phone.isdigit():
    #         raise ValidationError("O campo de telefone deve conter apenas números.")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    class Meta:
        verbose_name = 'Contato'
        verbose_name_plural = 'Contatos'
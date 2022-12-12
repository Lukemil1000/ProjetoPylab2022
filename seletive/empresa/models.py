from django.db import models


class Tecnologias(models.Model):
    tecnologia = models.CharField(max_length=30)

    def __str__(self):
        return self.tecnologia


class Empresa(models.Model):
    choice_nicho_mercado = (
        ('M', 'Marketing'),
        ('N', 'Nutrição'),
        ('D', 'Design')
    )
    nome = models.CharField(max_length=30)
    email = models.EmailField()
    cidade = models.CharField(max_length=30)
    endereco = models.CharField(max_length=30)
    caracteristica_empresa = models.TextField()
    nicho_mercado = models.CharField(max_length=3, choices=choice_nicho_mercado)
    logo = models.ImageField(upload_to="logo_empresa", null=True)
    tecnologias = models.ManyToManyField(Tecnologias)

    def __str__(self):
        return self.nome

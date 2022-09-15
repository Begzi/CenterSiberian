from django.db import models

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя')
    color = models.CharField(max_length=15, verbose_name='Цвет')

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'

class New(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    shortDescription = models.CharField(max_length=255, verbose_name='Краткое описание')
    description = models.TextField(verbose_name='Полное описание')

    type = models.ForeignKey('Type', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        verbose_name = 'Новости'
        verbose_name_plural = 'Новости'
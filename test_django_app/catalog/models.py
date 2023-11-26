from django.db import models
from djrichtextfield.models import RichTextField


class DateTimeStamp(models.Model):
    created = models.DateTimeField('Created', auto_now=True)
    updated = models.DateTimeField('Updated', auto_now_add=True)

    class Meta:
        abstract = True


# Create your models here.
class Category(DateTimeStamp):
    name = models.CharField('имя товару', max_length=25, unique=True)
    url = models.URLField('Url', blank=True)
    email = models.EmailField('Email', blank=True)
    description = RichTextField('Опиис', blank=True)
    activate = models.BooleanField('Active', default=False)

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField('Имя тега', max_length=25, unique=True)
    uuid = models.UUIDField('UUID')

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'
        ordering = ['-name']

    def __str__(self):
        return self.name

class Parametr(models.Model):
    name = models.CharField('Параметр товару', max_length=25, unique=True)

    class Meta:
        verbose_name = 'Параметр'
        verbose_name_plural = 'Параметри'

    def __str__(self):
        return self.name

class Goods(DateTimeStamp):
    name = models.CharField('Имя товару', max_length=25, unique=True)
    description = RichTextField('Опиис', blank=True)
    price = models.FloatField('Price', default=0)
    price_opt = models.IntegerField('Opt', default=0)
    activate = models.BooleanField('Active', default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='goods')
    tags = models.ManyToManyField(Tag, related_name='goods_tag')
    image = models.ImageField('Image', upload_to='image', blank=True)
    parametr = models.ForeignKey(Parametr, on_delete=models.CASCADE, related_name='parametr', null=True, blank=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'
        ordering = ['-name']

    def __str__(self):
        return self.name
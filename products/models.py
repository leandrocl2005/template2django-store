from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.


class Category(models.Model):
  name = models.CharField("Categoria", max_length=10)

  def __str__(self):
    return self.name


class Product(models.Model):
  name = models.CharField("Nome", max_length=30)
  photo = models.ImageField(upload_to='static/img', null=True, blank=True)
  summary = models.TextField("Sumário")
  description = models.TextField("Descrição")
  price = models.IntegerField()
  avaliability = models.BooleanField(default=True)
  popular = models.BooleanField(default=False)
  recommended = models.BooleanField(default=False)
  category = models.ForeignKey(Category,
                               related_name='product',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True)
  created_at = models.DateTimeField("Criado em", auto_now_add=True)

  @property
  def formatted_price(self):
    return "R$ {:.2f}".format(self.price / 100).replace('.', ',')

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('-created_at', )

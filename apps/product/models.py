from django.db import models
from apps.product.service import STATUS_CHOICES, CATEGORY_CHOICES
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, max_length=25)
    title_product = models.CharField(verbose_name='Название товара', max_length=30)
    title_company = models.CharField(verbose_name='Название компании', max_length=30, blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(verbose_name='Категория', choices=CATEGORY_CHOICES, max_length=25)
    price = models.IntegerField(verbose_name='Цена')
    number = models.CharField(verbose_name='Номер', max_length=10)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='products_photos/', blank=True, null=True)

    
class ProductImage(models.Model):
    image = models.ImageField(upload_to='products_photos/', blank=True, null=True)
    post = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')

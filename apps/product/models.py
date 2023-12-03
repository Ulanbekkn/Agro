from django.db import models
from apps.product.service import STATUS_CHOICES, CATEGORY_CHOICES
# from apps.account.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


class Product(models.Model):
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, max_length=25)
    title_product = models.CharField(verbose_name='Название товара', max_length=30)
    title_company = models.CharField(verbose_name='Название компании', max_length=30, blank=True, null=True)
    address = models.CharField(verbose_name='Адрес', max_length=100)
    images = models.ManyToManyField('Image', verbose_name='Фото', related_name='products', blank=True)
    description = models.TextField(verbose_name='Описание')
    category = models.CharField(verbose_name='Категория', choices=CATEGORY_CHOICES, max_length=25)
    price = models.IntegerField(verbose_name='Цена')
    number = models.CharField(verbose_name='Номер', max_length=10)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Title: {self.title_product}'

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'


class Image(models.Model):
    image = models.ImageField(upload_to='products_photos/')


class Comment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    time_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'User: {self.user.username}, Product: {self.product.title_product}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

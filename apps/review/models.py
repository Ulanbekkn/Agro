from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product



User = get_user_model()



class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites', verbose_name='Пост')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Автор')

    class Meta:
        ordering: ('-pk',)
        constraints = [models.UniqueConstraint(fields=['author', 'product'], name='unique_author_product'),]
        indexes = [models.Index(fields=['author', 'product'], name='inx_auth_product'),]

    def __str__(self) -> str:
        return f'{self.author}->{self.product}'

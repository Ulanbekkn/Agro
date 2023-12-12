from django.db import models
from django.contrib.auth import get_user_model
from apps.product.models import Product



User = get_user_model()



class Favorite(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='favorites', verbose_name='Пост')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='favorites', verbose_name='Автор')

    class Meta:
        ordering: ('-pk',)
        constraints = [models.UniqueConstraint(fields=['user', 'product'], name='unique_user_product'),]
        indexes = [models.Index(fields=['user', 'product'], name='inx_user_product'),]

    def __str__(self) -> str:
        return f'{self.user}->{self.product}'



# class Comment(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     text = models.CharField(max_length=255)
#     time_create = models.DateTimeField(auto_now_add=True)


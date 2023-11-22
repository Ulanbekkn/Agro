from django.db import models


class AboutUs(models.Model):
    title = models.CharField(verbose_name='Название', max_length=50)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'О нас'
        verbose_name_plural = 'О нас'


class ImageAgro(models.Model):
    title = models.CharField(verbose_name='Название фото', max_length=50)
    image = models.ImageField(verbose_name='Фотография', upload_to='photo_agro/')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Фотография'
        verbose_name_plural = 'Фотографии'


class SNS(models.Model):
    instagram = models.URLField(verbose_name='Instagram')
    facebook = models.URLField(verbose_name='Facebook')
    twitter = models.URLField(verbose_name='Twitter')

    def __str__(self):
        return self.instagram

    class Meta:
        verbose_name = 'Социальная сеть'
        verbose_name_plural = 'Социальные сети'



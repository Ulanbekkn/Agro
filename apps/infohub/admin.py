from django.contrib import admin

from apps.infohub.models import AboutUs, ImageAgro, SNS


@admin.register(AboutUs)
class AboutUsAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')


@admin.register(ImageAgro)
class ImageAgroAdmin(admin.ModelAdmin):
    list_display = ('title', 'image')


@admin.register(SNS)
class SNSAdmin(admin.ModelAdmin):
    list_display = ('instagram', 'twitter', 'facebook')


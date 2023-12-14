from django.contrib import admin
from .models import Favorite, Comment

admin.site.register(Favorite)
admin.site.register(Comment)
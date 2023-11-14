from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from phonenumbers import parse as parse_phone_number, is_valid_number

User = get_user_model()

def validate_phone_number(value):
    parsed_number = parse_phone_number(value, "KG")
    if not is_valid_number(parsed_number):
        raise ValidationError("Некорректный номер телефона.")
    if not value.startswith('0') and not value.startswith('+996'):
            raise ValidationError('Некорректный номер телефона1.')


class ProfileUser(models.Model):
    user = models.OneToOneField(User, 
                                on_delete=models.CASCADE, 
                                related_name='profiles_user', 
                                primary_key=True, 
                                verbose_name='Пользователь')
    fio = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=20, validators=[validate_phone_number], blank=True)
    email = models.EmailField(blank=True)
    image = models.ImageField(upload_to = 'images/', verbose_name = 'Изображение', blank=True)


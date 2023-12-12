from rest_framework.serializers import ModelSerializer, ReadOnlyField
from apps.review.models import Favorite
 







class FavoriteListSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCreateSerializer(ModelSerializer):
    author = ReadOnlyField(source='author.email')

    class Meta:
        model = Favorite
        fields = ('product', 'author')


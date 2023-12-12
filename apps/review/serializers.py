from rest_framework.serializers import ModelSerializer, ReadOnlyField
from apps.review.models import Favorite
 



class FavoriteListSerializer(ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'


class FavoriteCreateSerializer(ModelSerializer):
    user = ReadOnlyField(source='user.email')
    product = ReadOnlyField()

    class Meta:
        model = Favorite
        fields = ('product', 'user')


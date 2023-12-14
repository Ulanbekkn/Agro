from rest_framework.serializers import (ModelSerializer,
                                        ReadOnlyField,
                                        CharField,
                                        ValidationError)

from apps.review.models import Favorite, Comment
 



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





class CommentSerializer(ModelSerializer):
    user = CharField(source='user.email', read_only=True)
    product = ReadOnlyField(source='')


    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        user = request.user
        post = validated_data.get('post')
        comment = Comment.objects.create(**validated_data)
        return comment    
    
    def update(self, instance, validated_data):
        user = self.context['request'].user
        if instance.author != user:
            raise ValidationError('Вы не можете изменить комментарии другого автора')
        if 'author' in validated_data:
            raise ValidationError('Вы не можете изменить автора')
        instance.body = validated_data.get('body', instance.body)
        instance.save()
        return instance
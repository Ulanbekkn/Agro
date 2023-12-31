from rest_framework.serializers import ModelSerializer
from apps.product.models import *



class ProductImageSerializer(ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'



class ProductDetailSerializer(ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)


    class Meta:
        model = Product
        fields = '__all__'

        

class ProductListSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = ['id', 'price', 'title_product', 'image']        






# class ProductDetailSerializer(serializers.ModelSerializer):
#     user_nickname = serializers.CharField(source='user.username', read_only=True)
#     user = serializers.HiddenField(default=serializers.CurrentUserDefault())
#     title_company = serializers.CharField(min_length=2)
#     address = serializers.CharField(min_length=2)
#     number = serializers.CharField()
#     comments = CommentSerializer(many=True, required=False)

#     class Meta:
#         model = Product
#         fields = ('id', 'status', 'title_product', 'title_company', 'address', 'images', 'description', 'category',
#                   'price', 'number', 'user', 'user_nickname', 'comments')

#     @staticmethod
#     def validate_number(number):
#         if not number.startswith('0'):
#             raise serializers.ValidationError('Номер должен начинаться с нуля.')

#         if not number.isdigit() or len(number) != 10:
#             raise serializers.ValidationError('Номер должен состоять из 10 цифр, включая ведущий ноль.')

#         return number

#     @staticmethod
#     def validate_address(address):
#         parts = address.split(',')

#         if len(parts) != 2:
#             raise serializers.ValidationError('Адрес должен содержать название улицы, затем запятую и номер дома.')

#         street, house = parts

#         return address




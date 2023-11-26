from rest_framework import serializers
from .models import Category, Goods, Tag



class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'uuid']

# class CategoryNameSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Category
#         fields = ['name']


class GoodsSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)
    # category = CategoryNameSerializer(read_only=True)
    # category = serializers.CharField(source='category_name')


    class Meta:
        model = Goods
        fields = ['id', 'name', 'description', 'price', 'price_opt', 'activate', 'created', 'image', 'tags', 'category',
                  'parametr']



class CategorySerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=True, read_only=True)
    goods_count = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'activate', 'created', 'goods', 'goods_count']

    def get_goods_count(self, category):
            count = category.goods.count()
            return count

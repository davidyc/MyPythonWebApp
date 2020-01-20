from rest_framework import serializers
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish, _dish


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance


class DishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=50)
    discription = serializers.CharField()
    dishcategory = serializers.StringRelatedField()

    class Meta:
        model = Category
        fields = ['id', 'name']


from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Category, Dish, Ingredient, Week, ListDishesWeek, _weekDish, _dish


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class CategorySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Category.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class DishSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    discription = serializers.CharField(max_length=1000)
    dishcategory = CategorySerializer()

    def create(self, validated_data):
        category_data = validated_data.pop('dishcategory', None)         
        if category_data:
            category = Category.objects.get_or_create(**category_data)[0]
            validated_data['dishcategory'] = category                 
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.discription = validated_data.get('discription', instance.discription)
        category_data = validated_data.pop('dishcategory', None)         
        if category_data:
            category = Category.objects.get_or_create(**category_data)[0]
            validated_data['dishcategory'] = category         
        instance.dishcategory = category
        instance.save()
        return instance


class IngredientSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dish = DishSerializer()
    product = ProductSerializer()

    
    def create(self, validated_data):
        dish_data = validated_data.pop('dish', None)   
        prod_data = validated_data.pop('product', None)            
        if dish_data:
            dish = Dish.objects.get_or_create(**dish_data)[0]
            validated_data['dish'] = dish
        if prod_data:
            product = Product.objects.get_or_create(**prod_data)[0]
            validated_data['product'] = product                         
        return Dish.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.discription = validated_data.get('discription', instance.discription)
        category_data = validated_data.pop('dishcategory', None)         
        if category_data:
            category = Category.objects.get_or_create(**category_data)[0]
            validated_data['dishcategory'] = category         
        instance.dishcategory = category
        instance.save()
        return instance


class UserSerelization(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField(max_length=50)   

class WeekSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)   
    user = UserSerelization()
    
    def create(self, validated_data):
        week_data = validated_data.pop('name', None)        
        user_data = validated_data.pop('user', None)   
        if user_data:
            user = User.objects.get_or_create(**user_data)[0]
            validated_data['user'] = user         
            validated_data['name'] = week_data       
            
        return Week.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance
    
class ListDishesWeekSerelization(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    dish = DishSerializer()
    week = WeekSerializer()

    def create(self, validated_data):
        dish_data = validated_data.pop('dish', None)        
        week_data = validated_data.pop('week', None)  
        if week_data:            
            week = Week.objects.filter(name =  week_data['name'])               
            validated_data['week'] = week[0]      
            if dish_data:
                dish = Dish.objects.filter(name =  dish_data['name'])
                validated_data['dish'] = dish[0]             
        return ListDishesWeek.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        dish_data = validated_data.pop('dish', None)        
        week_data = validated_data.pop('week', None)  
        if week_data:            
            week = Week.objects.filter(name =  week_data['name'])               
            validated_data['week'] = week[0]      
            if dish_data:
                dish = Dish.objects.filter(name =  dish_data['name'])
                instance.dish  = dish[0]    
        instance.save()
        return instance
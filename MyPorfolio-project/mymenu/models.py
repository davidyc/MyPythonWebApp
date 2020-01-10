from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name
   
class Dish(models.Model):
    name = models.CharField(max_length=50)  
    discription = models.CharField(max_length=1000, blank=True, null=True) 
    dishcategory = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return "{} для {}".format(self.dish, self.product)


class Week(models.Model):
    name = models.CharField(max_length=50)      

    def __str__(self):
        return "Неделя {}".format(self.name)

class ListDishesWeek(models.Model):
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    week = models.ForeignKey(Week, on_delete=models.CASCADE)

    def __str__(self):
        return "Блюдо {} для {} ".format(self.dish, self.week)

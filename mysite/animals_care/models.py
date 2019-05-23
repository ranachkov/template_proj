from django.db import models


from accounts.models import ProfileOwner
# Create your models here.


class Food(models.Model):
    name = models.CharField(max_length=200)
    price = models.PositiveIntegerField()


    def __str__(self):
        return f"{self.name}"


class Animal(models.Model):
    user = models.ForeignKey(ProfileOwner, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    breed = models.CharField(max_length=200)
    description = models.TextField()
    age = models.PositiveIntegerField()
    image_url = models.URLField()
    favorite_food = models.ForeignKey(Food, on_delete=models.CASCADE, blank=True)

    def __str__(self):
        return f"{self.user} has {self.name}"



#class Toys(models.Model):
 #   name = models.CharField(max_length=200)
 #   type = models.CharField(max_length=200)
  #  price = models.PositiveIntegerField()
   # description = models.TextField()
    #image_url = models.URLField()
    #company

    #def __str__(self):
     #   return f"{self.name} has {self.price}"


#class Other_Products(models.Model):
 #   name = models.CharField(max_length=200)
  #  type = models.CharField(max_length=200)
   # price = models.PositiveIntegerField()
    #description = models.TextField()
    #image_url = models.URLField()
    #company

    #def __str__(self):
     #   return f"{self.name} has {self.price}"


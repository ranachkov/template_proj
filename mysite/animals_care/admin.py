from django.contrib import admin
from .models import Animal, Food, Company, Other_Products
# Register your models here.

admin.site.register(Animal)
admin.site.register(Food)
admin.site.register(Company)
admin.site.register(Other_Products)
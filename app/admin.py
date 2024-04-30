from django.contrib import admin
from app.models import Slider,Banner,Main_Category,Category,Sub_Category
from app.models import Product,Section,Product_Image,Product_Information,Color,Brand
# Register your models here.

class Product_Images(admin.TabularInline):
    model  = Product_Image

class Product_Informations(admin.TabularInline):
    model = Product_Information

class Product_Admin(admin.ModelAdmin):
    inlines = (Product_Images,Product_Informations)


admin.site.register(Slider)

admin.site.register(Banner)


admin.site.register(Main_Category)
admin.site.register(Category)
admin.site.register(Sub_Category)

admin.site.register(Section)
admin.site.register(Product,Product_Admin)
admin.site.register(Product_Image)
admin.site.register(Product_Information)
admin.site.register(Color)
admin.site.register(Brand)
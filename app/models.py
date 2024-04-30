from django.db import models
from ckeditor.fields import RichTextField
from django.utils.text import slugify
from django.db.models.signals import pre_save
# Create your models here.

class Slider(models.Model):

    DISCOUNT_DEAL = (('New Arrival','New Arrival'),
                     ('Hot Deal','Hot Deal'),
                     )

    image = models.ImageField(upload_to='media/',max_length= 200)

    brand_name = models.CharField(max_length=200)

    discount = models.IntegerField()
    sale = models.IntegerField()

    discount_deal = models.CharField(choices=DISCOUNT_DEAL,max_length= 200)

    link = models.CharField(max_length = 200)

    
    def __str__(self) -> str:
        return self.brand_name



class Banner(models.Model):

    brand_name = models.CharField(max_length=200)

    image = models.ImageField(upload_to='media/',max_length= 200)

    discount = models.IntegerField()

    quote = models.CharField(max_length=200)

    link = models.CharField(max_length = 200)

    def __str__(self) -> str:
        return self.brand_name



class Main_Category(models.Model):

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class Category(models.Model):
    main_category = models.ForeignKey(Main_Category,on_delete=models.CASCADE)

    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.main_category.name +"--"+ self.name
    

class Sub_Category(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.category.main_category.name +"--"+ self.category.name +"--"+ self.name



class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name
    
class Color(models.Model):
    name = models.CharField(max_length= 200)

class Brand(models.Model):
    name = models.CharField(max_length= 200)


class Product(models.Model):
    color = models.ForeignKey(Color,on_delete=models.CASCADE,null=True)
    brand = models.ForeignKey(Brand,on_delete=models.CASCADE,null=True)
    total_quantity = models.IntegerField()
    availability = models.IntegerField()
    brand_name = models.CharField(max_length=200)
    tax = models.IntegerField(null=True)
    packing_cost = models.IntegerField(null=True)
    image = models.CharField(max_length=200)
    section = models.ForeignKey(Section,on_delete=models.DO_NOTHING)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    price = models.IntegerField()
    discount = models.IntegerField()
    model = models.CharField(max_length=200)
    information = RichTextField()
    description = RichTextField()
    slug = models.SlugField(default='', max_length=500, null=True, blank=True)

    def __str__(self) -> str:
        return self.brand_name

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse("product_detail", kwargs={'slug': self.slug})

    class Meta:
        db_table = "app_Product"

def create_slug(instance, new_slug=None):
    slug = slugify(instance.brand_name)
    if new_slug is not None:
        slug = new_slug
    qs = Product.objects.filter(slug=slug).order_by('-id')
    exists = qs.exists()
    if exists:
        new_slug = "%s-%s" % (slug, qs.first().id)
        return create_slug(instance, new_slug=new_slug)
    return slug

def pre_save_post_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = create_slug(instance)

pre_save.connect(pre_save_post_receiver, Product)







class Product_Information(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    detail = models.CharField(max_length=200)
    specification = models.CharField(max_length=200)


class Product_Image(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE)
    image_url = models.CharField(max_length= 200)





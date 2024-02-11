from django.db import models

class Slider(models.Model):
    DISCOUNT_DEAL = (
        ('Hot Deals', 'Hot Deals'),
        ('New Arrivals', 'New Arrivals'),
    )

    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(choices=DISCOUNT_DEAL, max_length=200)
    Sales = models.IntegerField()
    Brand_name = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Link = models.CharField(max_length=200)

    def __str__(self):
        return self.Brand_name


class Banner(models.Model):
    Image = models.ImageField(upload_to='media/slider_imgs')
    Discount_Deal = models.CharField(max_length=200)
    Discount = models.IntegerField()
    Quote = models.CharField(max_length = 100)


    def __str__(self):
        return self.Quote



class Main_Categroy(models.Model):
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
    

class Categroy(models.Model):
    main_categroy = models.ForeignKey(Main_Categroy , on_delete = models.CASCADE )
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name +"--"+ self.main_categroy.name


class Sub_Categroy(models.Model):
    categroy  = models.ForeignKey(Categroy,on_delete = models.CASCADE)
    name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name






















        


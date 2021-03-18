from django.db import models

# Create your models here.
# class Product_category(models.Model):
#     Prod_cat_id = models.AutoField
#     pro_category = models.CharField(max_length=100)
#     sub_pro_category = models.CharField(max_length=100,unique=True)
#
#     def __str__(self):
#         return self.sub_pro_category


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=100)
    subcategory = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    desc = models.TextField(max_length=500)
    launch_date = models.DateField()
    product_image = models.ImageField(upload_to="media", default="")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    number = models.IntegerField(default=0)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name

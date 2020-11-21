from django.db import models

# Create your models here.
class Category(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT,null=True)
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    image = models.ImageField(upload_to='static/images')
    def __str__(self):
        return self.name

#TODO: python manage.py makemigrations
#      python manage.py migrate
#      python manage.py createsuperuser
# --> Go to admin : 127.0.0.1:8000/admin
# --> Create some products (using theme images)

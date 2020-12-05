from django.db import models

# Create your models here.
class Product(models.Model):
    code = models.CharField(max_length=30, unique=True)
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    def __str__(self): return self.name

# python manage.py makemigrations
# python manage.py migrate
# python manage.py createsuperuser
# Register Product in admin.py
# Go to 127.0.0.1:8000/admin --> add some products
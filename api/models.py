from django.db import models
from django.contrib.auth.models import AbstractUser

CATEGORY_CHOICES = (
    ('Electronics', 'Electronics'),
    ('Clothings', 'Clothings'),
    ('Accessories', 'Accessories'),
)


class User(AbstractUser):

    first_name = models.CharField(max_length=175)
    last_name = models.CharField(max_length=175)
    email = models.CharField(max_length=250, unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    phone = models.CharField(max_length=12, blank=True, null=True)
    gender = models.CharField(max_length=11, blank=True, null=True)
    session_token = models.CharField(max_length=35, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.first_name} {self.last_name} - {self.email}'


class Product(models.Model):

    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    description = models.TextField(max_length=500)
    color = models.CharField(max_length=50)
    category = models.CharField(max_length=35, choices=CATEGORY_CHOICES, default="Electronics")
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    stock = models.IntegerField()
    is_active = models.BooleanField(default=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name} - {self.stock} - {self.price}'
    
    def get_category(self):
        return self.category


        
        
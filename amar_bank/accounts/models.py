from django.db import models
from django.contrib.auth.models import User
from .constants import Account_Type, Gender_Type

# Create your models here.

class UserBankAccount(models.Model):
    user = models.OneToOneField(User, related_name='account', on_delete=models.CASCADE)
    account_type = models.CharField(max_length=10, choices=Account_Type)
    account_no = models.IntegerField(unique=True)
    balance = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    initial_deposite_date = models.DateField(auto_now_add=True)
    gender = models.CharField(max_length=10, choices=Gender_Type)
    birth_date = models.DateField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f"{self.user.username}, {self.user.email}"
    
class UserAddress(models.Model):
    user = models.OneToOneField(User, related_name='address', on_delete=models.CASCADE)
    street_address = models.CharField(max_length=150)
    postal_code = models.IntegerField()
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f"{self.user.username}, {self.user.email}"

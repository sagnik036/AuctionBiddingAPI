from operator import mod
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator 
# Create your models here.


class Auction(models.Model):
    name = models.CharField(
        max_length=10,
        blank=False
    )
    start_price = models.IntegerField(
        blank=False
    )
    start_time = models.DateTimeField(
        blank=False
    )
    end_time = models.DateTimeField(
        blank=False
    )
    current_bid_user_id = models.IntegerField(
        blank=True,
        null= True
    )
    current_bid_price = models.IntegerField(
        blank=True,
        null= True
    )
    is_active = models.BooleanField(
        blank=True,
        default=True
    )
    winner_user_id = models.IntegerField(
        null=True, 
        blank=True,
    )
    
    def __str__(self):
        return self.name
from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Product(models.Model):
    title = models.TextField()
    category = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
        )

from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.


User = get_user_model()


class Category(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.TextField()
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products'
    )
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    seller = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='products'
        )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
        )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # name for URL
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

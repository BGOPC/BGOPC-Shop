from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=55, unique=True, null=False)
    price = models.IntegerField(null=False)
    desc = models.TextField(null=False)
    rates = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1)
    ia = models.BooleanField(default=False, null=True)  # is active

    def __str__(self):
        return f"{self.title},{self.price}$: \n{self.desc}"

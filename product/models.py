from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=55, unique=True, null=False)
    price = models.IntegerField(null=False)
    desc = models.TextField(null=False)
    rates = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1)
    ia = models.BooleanField(default=False, null=True)  # is active
    slug = models.SlugField(default="", null=False, db_index=True, )
    # slug = models.SlugField(default="", null=False, db_index=True, editable=False)

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def __str__(self):
        return f"{self.title},{self.price}$: \n{self.desc}"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

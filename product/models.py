from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.

class ProductTag(models.Model):
    title = models.CharField(max_length=255, blank=True)

    class Meta:
        verbose_name = "product tag"
        verbose_name_plural = "product tags"
    def __str__(self):
        return self.title


class ProductCategory(models.Model):
    title = models.CharField(max_length=150, verbose_name="Category Name")
    url_title = models.CharField(max_length=150, verbose_name="Category Name in url")

    def __str__(self):
        return f"({self.title}, {self.url_title})"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=55, unique=True, null=False)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, null=True, related_name="Products")
    price = models.IntegerField(null=False)
    desc = models.TextField(null=False)
    rates = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True, default=1)
    ia = models.BooleanField(default=False, null=True)  # is active
    slug = models.SlugField(default="", null=False, db_index=True, blank=True)

    # slug = models.SlugField(default="", null=False, db_index=True, editable=False)

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def __str__(self):
        return f"{self.title},{self.price}$: \n{self.desc}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

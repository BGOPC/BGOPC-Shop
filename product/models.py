from turtle import title
from django.db import models
# from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from django.utils.text import slugify


# Create your models here.
class ProductBrand(models.Model):
    title = models.CharField(max_length=150,db_index=True)
    ia = models.BooleanField(default=True)
    def __str__(self):
        return f"{self.title}"
    class Meta:
        verbose_name = "Brand"
        verbose_name_plural = "Brands"

class ProductCategory(models.Model):
    title = models.CharField(max_length=150,db_index=True, verbose_name="Category Name")
    url_title = models.CharField(max_length=150,db_index=True, verbose_name="Category Name in url")
    ia = models.BinaryField(verbose_name="Is/ ISn't Active")
    is_deleted = models.BooleanField(default=False, null=True, verbose_name="is/isn't deleted")
    
    def __str__(self):
        return f"({self.title}, {self.url_title})"

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Product(models.Model):
    title = models.CharField(max_length=55, null=False)
    category = models.ManyToManyField (ProductCategory, related_name="Product_Categories")
    brand = models.ForeignKey(ProductBrand, on_delete=models.CASCADE, null=True)
    price = models.IntegerField(null=False)
    short_description = models.CharField(max_length=500)
    desc = models.TextField(null=False)
    ia = models.BooleanField(default=False, null=True, verbose_name="is/isn't active")  # is active
    is_deleted = models.BooleanField(default=False, null=True, verbose_name="is/isn't deleted")
    slug = models.SlugField(default="", null=False, db_index=True, blank=True, max_length=100, unique=True)

    # slug = models.SlugField(default="", null=False, db_index=True, editable=False)

    def get_absolute_url(self):
        return reverse('product', args=[self.slug])

    def __str__(self):
        return f"{self.title},{self.price}$: \n{self.short_description}"

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(
            self, force_insert=False, force_update=False, using=None, update_fields=None
    ):
        self.slug = slugify(self.title)
        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

class ProductTag(models.Model):
    title = models.CharField(max_length=255, blank=True)
    product = models.ForeignKey(Product, blank=True, null=True, on_delete=models.SET_NULL, related_name="product_tags" )

    class Meta:
        verbose_name = "product tag"
        verbose_name_plural = "product tags"
    def __str__(self):
        return self.title



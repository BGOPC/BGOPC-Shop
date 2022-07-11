from pyexpat.errors import messages
from tabnanny import verbose
from django.db import models

# Create your models here.
class Contact(models.Model):
    title = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    name = models.CharField(max_length=300)
    message = models.TextField(null=False, blank=True)
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    adminresponse = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Contact us"
        verbose_name = "Contact us List"

    def __str__(self):
        return f"{self.title} by {self.name}"
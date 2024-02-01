from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    product = models.ManyToManyField("Product", blank=True, related_name="articles")

    def __str__(self):
        return self.title


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    realized_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name

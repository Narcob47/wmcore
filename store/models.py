from django.db import models
from django.utils import timezone
from datetime import timedelta

class Category(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.title

class Book(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='books/images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, related_name='books', on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    file_upload = models.FileField(upload_to='books/files/')

    def __str__(self):
        return self.title

class Training(models.Model):
    CATEGORY_CHOICES = [
        ('old', 'Old'),
        ('latest', 'Latest'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='trainings/images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)
    category = models.CharField(max_length=6, choices=CATEGORY_CHOICES, default='latest')

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.category == 'latest' and self.date_created < timezone.now() - timedelta(days=7):
            self.category = 'old'
        super().save(*args, **kwargs)

class Audiobook(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='audiobooks/images/')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title

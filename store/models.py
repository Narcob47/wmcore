from django.db import models

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

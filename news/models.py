from django.db import models

class Newsletter(models.Model):
    title = models.CharField(max_length=200)
    heading = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='images/')
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=100)

    def __str__(self):
        return self.title

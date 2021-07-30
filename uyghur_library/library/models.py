from django.db import models



class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn = models.CharField(max_length=100)
    # image = models.ImageField(default='default.jpeg', upload_to='book_cover')

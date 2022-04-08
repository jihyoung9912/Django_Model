from unicodedata import category
from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=20)
    english_title = models.CharField(max_length=45)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.title
from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=200)
    pub_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def clean(self):
        # Проверка, что год публикации не позже текущего
        current_year = timezone.now().year
        if self.pub_year > current_year:
            raise ValidationError({'pub_year': 'Год публикации не может быть позже текущего.'})

    def __str__(self):
        return f"{self.name} ({self.pub_year})"

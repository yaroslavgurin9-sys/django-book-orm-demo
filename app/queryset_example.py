from .models import Book

# Книги, опубликованные после 2000 года, отсортированные по году
books = Book.objects.filter(pub_year__gt=2000).order_by('pub_year')

from django.contrib import admin
from books.models import Book, Tag, Comment, Author

# Register your models here.
admin.site.register(Book)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Author)

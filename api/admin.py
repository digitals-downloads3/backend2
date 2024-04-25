from django.contrib import admin
from .models import Book, Category, BookOfTheDay, QuoteOfTheDay, Article, AboutUs

# Register your models here.
class BookAdmin (admin.ModelAdmin):
    list_display = ('title', 'publish', 'category', 'status', 'is_featured')

    
admin.site.register(Article)
admin.site.register(Book, BookAdmin)
admin.site.register(BookOfTheDay)
admin.site.register(Category)
admin.site.register(QuoteOfTheDay)
admin.site.register(AboutUs)
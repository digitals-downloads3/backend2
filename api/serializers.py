from rest_framework import  serializers
from .models import Book, Category, BookOfTheDay, QuoteOfTheDay, Article, AboutUs

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookOfTheDayViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookOfTheDay
        fields = '__all__'

    
class QuoteOfTheDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = QuoteOfTheDay
        fields = '__all__'

    
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'


class AboutUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutUs
        fields = '__all__'

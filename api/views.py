from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Book, Category, BookOfTheDay, QuoteOfTheDay, Article, AboutUs
from .serializers import BookSerializer, CategorySerializer, BookOfTheDayViewSerializer, QuoteOfTheDaySerializer, ArticleSerializer, AboutUsSerializer
from django.urls import resolve
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from django.http import HttpResponse



# Create your views here.
class BookView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(status='p')
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'about', 'description', 'additional_information']

    





class BookDetail(RetrieveAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()



class ArticlePagination(PageNumberPagination):
    page_size = 12


class ArticleView(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(status='p')[:6]
    

class ArticleList(ListAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.filter(status='p')
    pagination_class = ArticlePagination


class ArticleDetail(RetrieveAPIView):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()


class CategoryView(ListAPIView):
    queryset = Category.objects.filter(status='p')
    serializer_class = CategorySerializer


class CategoryDetail(RetrieveAPIView):
    queryset = Category.objects.filter(status='p')
    serializer_class = CategorySerializer


class CategoryView(ListAPIView):
    serializer_class = BookSerializer
    def get_queryset(self):

        resolver_match = resolve(self.request.path_info)
        category = resolver_match.kwargs.get('category')
        query = Book.objects.filter(category=category, status='p')[:5]
        return query


class CustomPagination(PageNumberPagination):
    page_size = 8


class FeaturedListView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(status='p', is_featured=True)
    pagination_class = CustomPagination

    


class FeaturedView(ListAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.filter(status='p', is_featured=True)[:4]
        


class BookOfTheDayView(ListAPIView):
    serializer_class = BookOfTheDayViewSerializer
    queryset = BookOfTheDay.objects.all()


class QuoteOfTheDayView(APIView):
    def get(self, request, format=None):
        quote_of_the_day = QuoteOfTheDay.objects.first()
        
        if not quote_of_the_day:
            return Response(status=404)
        
        serializer = QuoteOfTheDaySerializer(quote_of_the_day)
        
        return Response(serializer.data)


class AboutUsView(APIView):
    def get(self, request, format=None):
        aboutUS = AboutUs.objects.first()
        
        if not aboutUS:
            return Response(status=404)
        
        serializer = AboutUsSerializer(aboutUS)
        
        return Response(serializer.data)


def General (request):
    return HttpResponse('<a href="https://digitalsdownloads.com">Enter</a>')
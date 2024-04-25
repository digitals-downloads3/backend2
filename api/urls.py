from django.urls import path
from .views import (
    BookView, 
    BookDetail, 
    CategoryView, 
    CategoryDetail, 
    CategoryView, 
    FeaturedView, 
    FeaturedListView, 
    BookOfTheDayView,
    QuoteOfTheDayView,
    ArticleView,
    ArticleDetail,
    ArticleList,
    AboutUsView,
    General,
)

app_name="api"
urlpatterns= [
    path('', General, name="home"),
    path('booklist/', BookView.as_view(), name="bookView"),
    path('book/<int:pk>/', BookDetail.as_view(), name="bookdetail"),
    path('articlelist/', ArticleView.as_view(), name="ArticleView"),
    path('article/<int:pk>/', ArticleDetail.as_view(), name="ArticleDetail"),
    path('category/', CategoryView.as_view(), name="categoryview"),
    path('category/<int:pk>/', CategoryDetail.as_view(), name="categoryDetail"),
    path('booklist/<str:category>/', CategoryView.as_view(), name="categorySearch"),
    path('featuredlist/', FeaturedView.as_view(), name="featuredbooks"),
    path('featured/', FeaturedListView.as_view(), name='featuredbookslist'),
    path('bookfftheday/', BookOfTheDayView.as_view(), name="BookOfTheDay"),
    path('quoteoftheday/', QuoteOfTheDayView.as_view(), name="QuoteOfTheDayView"),
    path('allarticlelist/', ArticleList.as_view(), name="ArticleList"),
    path('aboutus/', AboutUsView.as_view(), name="AboutUsView"),
]
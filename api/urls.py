from django.urls import path
from api.views import BookApi,apiView,GenreApi

urlpatterns = [
    path('',apiView,name='apis'),
    path('books/',BookApi.as_view(),name = "books"),
    path('books/<int:pk>/',BookApi.as_view(),name = "bookdetail"),
    path('genres/',GenreApi.as_view(),name = "genres"),
    path('genres/<int:pk>/',GenreApi.as_view(),name = "genre"),
]
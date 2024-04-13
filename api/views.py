from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Book,Genre
from api.serializers import BooksSerializer,GenreSerializer
from django.http import Http404



@api_view(['GET'])
def apiView(request):
    apis = {
        'view-books' : '/books/ method : [GET]',
        'add-books' : '/books/ method : [POST]',
        'book-detail' : '/books/<int:pk> method : [GET]',
        'update-book' : '/books/<int:pk>  method : [PUT]',
        'delete-book' : '/books/<int:pk> method : [DELETE]',
        'view-genres' : '/genres/ method : [GET]',
        'add-genres' : '/genres/ method : [POST]',
        'genre-detail' : '/genres/<int:pk> method : [GET]',
        'update-genre' : '/genres/<int:pk>  method : [PUT]',
        'delete-genre' : '/genres/<int:pk> method : [DELETE]',
    }
    return Response(apis)

class BookApi(APIView):
    def get_object(self, pk):
        try:
            return Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is not None:
            book = self.get_object(pk)
            serializer = BooksSerializer(book, many=False)
        else:
            book = Book.objects.all()
            serializer = BooksSerializer(book, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = BooksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        book = self.get_object(pk)
        serializer = BooksSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        book = self.get_object(pk)
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




class GenreApi(APIView):
    def get_object(self, pk):
        try:
            return Genre.objects.get(pk=pk)
        except Genre.DoesNotExist:
            raise Http404

    def get(self, request, pk=None, format=None):
        if pk is not None:
            genre = self.get_object(pk)
            serializer = GenreSerializer(genre, many=False)
        else:
            genre = Genre.objects.all()
            serializer = GenreSerializer(genre, many=True)
        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = GenreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None):
        genre = self.get_object(pk)
        serializer = GenreSerializer(genre, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        genre = self.get_object(pk)
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    


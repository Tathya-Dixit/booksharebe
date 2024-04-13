from rest_framework import serializers
from main.models import Book,Genre

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id','genre', 'title', 'author', 'description', 'price', 'image','created_by']

class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = "__all__"
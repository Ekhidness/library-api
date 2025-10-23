from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(read_only=True)
    author_id = serializers.PrimaryKeyRelatedField(
        queryset=Author.objects.all(),
        write_only=True,
        source='author'
    )

    class Meta:
        model = Book
        fields = '__all__'
        extra_kwargs = {
            'cover_image': {'required': False},
            'book_file': {'required': False},
        }
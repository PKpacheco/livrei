# coding: utf-8

from rest_framework import serializers
from .models import Book, BookImage


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        depth = 1
        fields = ['id', 'isbn', 'name', 'author', 'language',
                  'publishing_house', 'comments', 'category', 'year', 'images']


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ['id', 'description', 'featured_internal', 'image', ]

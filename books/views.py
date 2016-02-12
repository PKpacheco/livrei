# coding: utf-8

from django.shortcuts import render
from .serializer import BookSerializer, ImageSerializer
from .models import Book, BookImage

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BookView(APIView):

    def get(self, request, pk, format=None):
        if not Book.objects.filter(pk=pk).exists():
            serializer = BookSerializer([])
        else:
            book = Book.objects.get(pk=pk)
            serializer = BookSerializer(book)

        return Response(serializer.data)


class BookListViewSet(APIView):
    serializer_class = BookSerializer

    def get(self, request, format=None):
        _category = self.request.query_params.get('category', None)

        if _category:
            queryset = Book.objects.filter(category__id=_category)
        else:
            queryset = Book.objects.all()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)


class ImageViewSet(APIView):
    serializer_class = ImageSerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(BookImage.objects.all(), many=True)
        return Response(serializer.data)

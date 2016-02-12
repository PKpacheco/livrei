# coding: utf-8

from django.shortcuts import render
from .serializer import BookCategorySerializer
from .models import BookCategory

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class BookCategoryViewSet(APIView):
    serializer_class = BookCategorySerializer

    def get(self, request, format=None):
        serializer = self.serializer_class(BookCategory.objects.all(), many=True)
        return Response(serializer.data)

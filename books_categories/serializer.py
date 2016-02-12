#   coding: utf-8

from rest_framework import serializers
from .models import BookCategory


class BookCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCategory
        depth = 1
        fields = ['id', 'name', 'parent', ]

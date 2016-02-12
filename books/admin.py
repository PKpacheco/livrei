# coding: utf-8

from django.contrib import admin
from .models import Book, BookImage
from .forms import BookForm


class ImageInline(admin.TabularInline):
    model = BookImage
    fields = ['featured_internal', 'description', 'image', 'image_tag']
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return u'<img src="%s"/>' % obj.image.url

    image_tag.short_description = ''
    image_tag.allow_tags = True


class BookAdmin(admin.ModelAdmin):
    inlines = [ImageInline]
    form = BookForm

admin.site.register(Book, BookAdmin)

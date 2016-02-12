# coding: utf-8
from __future__ import unicode_literals

from django.db import models
from core.models import TimeStampedModel


class Book(TimeStampedModel):
    isbn = models.CharField(max_length=13, blank=True, null=True, verbose_name="ISBN")
    name = models.CharField(max_length=255, verbose_name="Nome")
    author = models.CharField(max_length=255, verbose_name="Autor")
    language = models.CharField(max_length=255, verbose_name="Idioma")
    publishing_house = models.CharField(max_length=255, blank=True, null=True, verbose_name="Editora")
    comments = models.CharField(max_length=255, blank=True, null=True, verbose_name="Comentários")
    category = models.ForeignKey('books_categories.BookCategory', verbose_name='Categoria')
    ano = models.CharField(max_length=4, blank=True, null=True, verbose_name="Ano")

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = "livro"
        verbose_name_plural = "livros"
        ordering = ['name']


class BookImage(TimeStampedModel):
    description = models.CharField(max_length=255, blank=True, null=True, verbose_name="Descrição")
    featured_internal = models.BooleanField(default=False, verbose_name='Foto de destaque')
    image = models.ImageField(upload_to='books/', verbose_name='Imagem')
    book = models.ForeignKey(Book, related_name='images')

    def __unicode__(self):
        return self.description

    class Meta:
        verbose_name = "Imagem do livro"
        verbose_name_plural = "Imagens do livro"

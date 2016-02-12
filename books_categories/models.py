# coding: utf-8

from __future__ import unicode_literals

from django.db import models
from django.utils.text import slugify


class BookCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name='Nome')
    parent = models.ForeignKey("BookCategory", null=True, blank=True, verbose_name='Categoria Pai')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria de Livro'
        verbose_name_plural = 'Categorias dos Livros'
        ordering = ['name']

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        self.slug = slugify(self.name)
        super(BookCategory, self).save(
            force_insert=False, force_update=False, using=None, update_fields=None)

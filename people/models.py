# coding: utf-8
from django.db import models
from core.models import TimeStampedModel


class Member(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="nome")
    image = models.ImageField(upload_to='people/', blank=True, null=True, verbose_name="imagem")
    email = models.EmailField(max_length=255, verbose_name="email")
    description = models.CharField(max_length=255, verbose_name="descrição")

    def __unicode__(self):
        return self.name

    class Meta:

        verbose_name = "membro"
        verbose_name_plural = "membros"
        ordering = ['name']

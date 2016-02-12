# coding: utf-8

from django.db import models
from core.models import TimeStampedModel


class Institution(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="nome")
    description = models.CharField(max_length=255, verbose_name="descrição")
    ddd = models.CharField(max_length=2, verbose_name="DDD")
    telephone = models.CharField(max_length=9, verbose_name="telefone")
    email = models.EmailField(max_length=255, verbose_name="email")
    adress = models.CharField(max_length=255, verbose_name="Endereco")
    #region = models.

    def __unicode__(self):
        return self.name

    class Meta:

        verbose_name = "Instituição"
        verbose_name_plural = "Instituições"
        ordering = ['name']

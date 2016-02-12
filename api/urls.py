# coding: utf-8
from django.conf.urls import include, url
from . import DefaultRouter

from institutions.views import InstitutionViewSet, InstitutionView
from books_categories.views import BookCategoryViewSet
from people.views import MemberViewSet, MemberView
from books.views import BookView, BookListViewSet, ImageViewSet


from rest_framework.authtoken import views


router = DefaultRouter()

helper_patterns = [
    url(r'^books/$', BookListViewSet.as_view(), name='books'),
    url(r'^books/(?P<pk>[0-9]+)/$', BookView.as_view(), name='get_book'),
    url(r'^books-categories/$', BookCategoryViewSet.as_view(), name='categories'),

    url(r'^people/$', MemberViewSet.as_view(), name='people'),
    url(r'^people/(?P<pk>[0-9]+)/$', MemberView.as_view(), name='get_people'),

    url(r'^institutions/$', InstitutionViewSet.as_view(), name='institution'),
    url(r'^institutions/(?P<pk>[0-9]+)/$', InstitutionView.as_view(), name='get_institution'),
]

urlpatterns = helper_patterns
urlpatterns.extend(router.urls)

from django.shortcuts import render
from .serializer import InstitutionSerializer
from .models import Institution

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class InstitutionView(APIView):

    def get(self, request, pk, format=None):
        if not Institution.objects.filter(pk=pk).exists():
            serializer = InstitutionSerializer([])
        else:
            institution = Institution.objects.get(pk=pk)
            serializer = InstitutionSerializer(institution)

        return Response(serializer.data)


class InstitutionViewSet (APIView):
    serializer_class = InstitutionSerializer

    def get(self, request, format=None):
        _institution = self.request.query_params.getlist('id', None)

        if _institution:
            queryset = Institution.objects.filter(id__in=_institution)
        else:
            queryset = Institution.objects.all()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

# Create your views here.

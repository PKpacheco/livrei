from django.shortcuts import render
from .serializer import MemberSerializer
from .models import Member

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class MemberView(APIView):

    def get(self, request, pk, format=None):
        if not Member.objects.filter(pk=pk).exists():
            serializer = MemberSerializer([])
        else:
            member = Member.objects.get(pk=pk)
            serializer = MemberSerializer(member)

        return Response(serializer.data)


class MemberViewSet (APIView):
    serializer_class = MemberSerializer

    def get(self, request, format=None):
        _member = self.request.query_params.getlist('id', None)

        if _member:
            queryset = Member.objects.filter(id__in=_member)
        else:
            queryset = Member.objects.all()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)

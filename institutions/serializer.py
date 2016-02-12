from rest_framework import serializers
from .models import Institution


class InstitutionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Institution
        depth = 1
        fields = ['id', 'name', 'ddd', 'telephone', 'description', 'email', 'adress']

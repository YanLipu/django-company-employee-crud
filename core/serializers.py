from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Company, Employe

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CompanySerializer(serializers.ModelSerializer):
    # grupo = GrupoSerializer()

    class Meta:
        model = Company
        fields = '__all__'

class EmployeSerializer(serializers.ModelSerializer): 
    company_name = serializers.CharField(source='company.name', read_only=True)
    class Meta:
        model = Employe
        fields = '__all__'


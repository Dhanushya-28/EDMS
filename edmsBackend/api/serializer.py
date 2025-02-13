from rest_framework import serializers
from .models import Employees,Department
from django.contrib.auth.models import User


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employees
        fields = "__all__"
    
    def to_representation(self, instance):
        self.fields['departmentId'] = DepartmentSerializer(read_only=True)
        return super(EmployeeSerializer, self).to_representation(instance)


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)



from django.contrib.auth import authenticate
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employees,Department
from .serializer import EmployeeSerializer,RegisterSerializer, LoginSerializer,DepartmentSerializer
from rest_framework.views import APIView

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                return Response({"message": "Login successful"}, status=status.HTTP_200_OK)
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(["POST"])
def add_employee(request):
    serializedData = EmployeeSerializer(data=request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data,
                        status=status.HTTP_201_CREATED)

    return Response(data=serializedData.errors,
                    status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def employees_list(request):
    employeeList = Employees.objects.all()
    serializedData = EmployeeSerializer(employeeList, many=True)
    return Response(data=serializedData.data,
                    status=status.HTTP_200_OK)

@api_view(["GET"])
def employees_details(request, id):
    employeeList = Employees.objects.get(pk=id)
    serializedData = EmployeeSerializer(employeeList)
    return Response(data=serializedData.data,
                    status=status.HTTP_200_OK)
@api_view(["PUT"])
def edit_employee(request, id):
    try:
        employeeList = Employees.objects.get(pk=id)
        serializedData = EmployeeSerializer(employeeList, data=request.data)
        print(serializedData)
        if serializedData.is_valid():
            serializedData.save()            
            return Response(data=serializedData.data,
                            status=status.HTTP_200_OK)
        return Response(data=serializedData.errors,
                        status=status.HTTP_400_BAD_REQUEST)
    except Employees.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["DELETE"])
def delete_employee(request,id):
    try:
        employeeList = Employees.objects.get(pk=id)
        employeeList.delete()
        return Response(status=status.HTTP_200_OK)
    except Employees.DoestNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(["GET"])
def all_department(request):
    departmentList = Department.objects.all()
    serializedData = DepartmentSerializer(departmentList, many=True)
    return Response(data=serializedData.data,
                    status=status.HTTP_200_OK)

@api_view(["POST"])
def create_department(request):
    serializedData = DepartmentSerializer(data=request.data)
    if serializedData.is_valid():
        serializedData.save()
        return Response(data=serializedData.data,
                        status=status.HTTP_201_CREATED)

    return Response(data=serializedData.errors,
                    status=status.HTTP_400_BAD_REQUEST)
 

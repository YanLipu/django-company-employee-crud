from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, permissions
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import Company, Employe
from .serializers import UserSerializer, CompanySerializer, EmployeSerializer
from . import authentication
import jwt
import datetime

class LoginController(APIView):
    def post(self, request):
        print(request.data)        
        username = request.data.get('username')
        password = request.data.get('password')
        print(username)
        print(password)
        user = User.objects.filter(username=username).first()
        # user = authenticate(username=username, password=password)
        if user is not None:
            print('entrou aqui')
            payload = dict(
                username=user.username,
                super_user=user.is_superuser,
                exp=datetime.datetime.utcnow() + datetime.timedelta(hours=24),
                iat=datetime.datetime.utcnow(),
            )
            token = jwt.encode(payload, settings.SECRET_JWT, algorithm="HS256")
            print(token)
            resp = Response({"username": user.username, "is_superuser": user.is_superuser}, status=status.HTTP_200_OK)
            resp.set_cookie(key='jwt', value=token, httponly=True)
            # login(request, user)
            return resp
        else:
            return Response({"error": "invalid username or password"}, status=status.HTTP_403_FORBIDDEN)

class LogoutController(APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        resp = Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "user logged off"}
        
        return resp

class UserController(APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        usuario = User.objects.all()
        serializer = UserSerializer(usuario, many=True)
        return Response(serializer.data)

class CompanyController(APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self,request):
        grupos = Company.objects.all()
        serializer = CompanySerializer(grupos, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)
    
        serializer = CompanySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)
        
        company = self.get_object(id)
        if company is None:
            return Response(
                {"error": "Company not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = CompanySerializer(company, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)
        company = self.get_object(id)
        if company is None:
            return Response(
                {"error": "Company not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        company.delete()
        return Response(
                {"message": "Company deleted succesfully."},
                status=status.HTTP_204_NO_CONTENT
            )

    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return None

class EmployeController(APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request):
        # usuario = Employe.objects.all()
        usuario = Employe.objects.select_related('company')
        print(usuario)
        serializer = EmployeSerializer(usuario, many=True)
        print(serializer)
        return Response(serializer.data)

    def post(self, request):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)

        serializer = EmployeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, id):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)
        
        employe = self.get_object(id)
        if employe is None:
            return Response(
                {"error": "Employe not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = EmployeSerializer(employe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        payload = authentication.GetTokenParameters.token_payload(self, request)
        super_user = payload.get('super_user')
        if not super_user:
            return Response({"error": "user not allowed"}, status=status.HTTP_403_FORBIDDEN)
        employe = self.get_object(id)
        if employe is None:
            return Response(
                {"error": "Employe not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        employe.delete()
        return Response(
                {"message": "Employe deleted succesfully."},
                status=status.HTTP_204_NO_CONTENT
            )

    def get_object(self, pk):
        try:
            return Employe.objects.get(pk=pk)
        except Employe.DoesNotExist:
            return None
        
class GetCompanyIdController(APIView):
    
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        company = self.get_object(id)
        serializer = CompanySerializer(company)
        return Response(serializer.data)
    
    def get_object(self, pk):
        try:
            return Company.objects.get(pk=pk)
        except Company.DoesNotExist:
            return None
        
class GetEmployeIdController(APIView):

    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, id):
        employee = self.get_object(id)
        serializer = EmployeSerializer(employee)
        return Response(serializer.data)
    
    def get_object(self, pk):
        try:
            return Employe.objects.get(pk=pk)
        except Employe.DoesNotExist:
            return None
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Student
from .serializers import StudentSerializer
# from django.contrib.auth.models import User
# Create your views here.

class StudentApi(APIView):
    def get(self, request):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many = True)
        # user = User.objects.get(username='admin',password = 'password') 
        # print(user.username)
        return Response({
            'status': 'True',
            'data': serializer.data
        })
        
        
    def put(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'True',
                'data': serializer.data
            })
        else:
            return Response({
                'status': 'False',
                'data': serializer.errors
            })
class LoginAPIView(APIView):
    def post(self, request):
        user_object = authenticate(username = username, password = password)
        if user_obj:
            token, _=Token.objects.get_or_create(user=user_obj)
            print(token)
            return Response({
                'status': 'True',
                "data":{'token':''}
            })
            return Response({
                "status": False,
                'data':(),
                'message': 'Invalid credentials'
            })
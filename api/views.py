# from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from .models import User
from .serializer import UserSerializer

# Create your views here.
# @api_view(['GET'])
# def get_users(request):
#     users = User.objects.all()
#     serializer = UserSerializer(users, many=True)
#     return Response(serializer.data)
 
# @api_view(['POST'])
# def create_user(request):
#     serializer = UserSerializer(data=request.data) 
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_REQUEST)

# @api_view(['GET','PUT','DELETE'])
# def user_detail(request,pk):
#     try:
#         user = User.objects.get(pk=pk)    
#     except User.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = UserSerializer(user)
#         return Response(serializer.data)
    
#     elif request.method == 'PUT':
#         serializer = UserSerializer(user, data = request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD-REQUEST)    

#     elif request.method == 'DELETE':
#         user.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
class access_user(ModelViewSet):
    queryset = User.objects.all()
    # print(queryset)
    serializer_class = UserSerializer
    
    def list(self, request):
        try:
            admin = User.objects.all()
            # print(admin)
            serializer = self.get_serializer(admin,many=True)
            api_response = {
                                'status': 'success',
                                'code': status.HTTP_200_OK,
                                'message': 'All admins',
                                'all_admins': serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_msg = 'An error occurred while fetching ecords: '
            error_response = {
                                'status': 'error',
                                'code': status.HTTP_500_INTERNAL_SERVER_ERROR,
                                'message': error_msg,
            }
            return Response(error_response)

    def create(self, request):
        try:
            serializer = self.get_serializer(data=request.data)        
            serializer.is_valid(raise_exception = True)
            serializer.save()
            api_response = {
                'status': 'success',
                'code': status.Http_201_CREATED,
                'message': 'Admin added successfully',
                'new_admin':serializer.data,
            }
            return Response(api_response)
        except Exception as e:
            error_msg = 'An error occured:'
            error_response={
                'status': 'error',
                'code': status.HTTP_400_BAD_REQUEST,
                'message': error_msg
            }    
            return Response(error_response)
    
def destroy(self, request):
    try:
        instance = self.get_object()  # No need to pass 'pk' explicitly
        instance.delete()
        api_response = {
                    'status': 'success',
                    'code': status.HTTP_204_NO_CONTENT,
                    'message': 'Admin deleted successfully'
            }
        return Response(api_response, status=status.HTTP_204_NO_CONTENT)
    except User.DoesNotExist:
        error_response = {
            'status': 'error',
            'code': status.HTTP_404_NOT_FOUND,
            'message': 'User not found'
        }
        return Response(error_response, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        error_msg = 'An error occurred: {}'.format(str(e))
        error_response = {
            'status': 'error',
            'code': status.HTTP_400_BAD_REQUEST,
            'message': error_msg,
        }
        return Response(error_response, status=status.HTTP_400_BAD_REQUEST)
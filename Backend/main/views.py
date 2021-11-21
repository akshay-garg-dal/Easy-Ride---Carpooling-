
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from main.serializers import UserSerializer
from django.contrib.auth.models import User

# Create your views here.

@api_view(['GET', 'POST'])
def test(request):

    if request.method == 'GET':

        return Response("this is a test123")

    # elif request.method == 'POST':
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_all_users(request):

    if request.method == 'GET':

        users = User.objects.all()
        serrialized = UserSerializer(users, many=True)
        
        return Response(serrialized.data)

    # elif request.method == 'POST':
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .serializers import UserSerializer
from .producer import publish
import random


class UserViewset(viewsets.ViewSet):
    def list(self, request): #/api/users GET
        users = User.objects.all()
        serializer = UserSerializer(users, many = True)
        return Response(serializer.data)

    def create(self, request):    #/api/users POST
        serializer = UserSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        publish('user_created', serializer.data)
        return Response(serializer.data, status = status.HTTP_201_CREATED)

    def retrieve(self, request, pK=None): #/api/users/:id
        user = User.objects.get(id=pK)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def update(self, request, pK=None):
        user = User.objects.get(id=pK)
        serializer = UserSerializer(instance = user, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        publish('user_updated', serializer.data)
        return Response(serializer.data)

    def destroy(self, request, pK=None):
        user = User.objects.get(id=pK)
        user.delete()
        publish('user_deleted', pK)
        return Response(status=HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _):
        users = User.objects.all()
        user = random.choice(users)
        return Response({
            'id': user.id
        })

# Create your views here.

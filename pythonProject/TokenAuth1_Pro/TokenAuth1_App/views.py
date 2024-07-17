from django.shortcuts import render
from django.contrib.auth.models import User
from .models import CustomUser
from .serializers import CustomUserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


# Create your views here.

# user = User.objects.all()
# for user in user:
#     token = Token.objects.get_or_create(user=user)
#     print(token)

# token = Token.objects.all()
# print(token)




class CustomUserListView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    def get(self,request,id=None):
        if id is not None:
            queryset = CustomUser.objects.get(id = id)
            if queryset:
                serializer = CustomUserSerializer(queryset)
                return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST,'data':'queryset not found','message':'failure'})
        else:
            queryset = CustomUser.objects.all()
            serializer = CustomUserSerializer(queryset,many=True)
            if serializer:
                return Response({'status':status.HTTP_200_OK,'data':serializer.data,'message':'success'})
            return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors,'message':'failure'})

    def post(self,request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            #token, created = Token.objects.get_or_create(user = request.data['username'])

            user = serializer.save()
            #return Response({'status':status.HTTP_201_CREATED,'data':serializer.data,'message':'success'})

            # token= Token.objects.get_or_create(user = user)
            return Response({'status':status.HTTP_201_CREATED,'data':serializer.data,'message':'created'})
        return Response({'status':status.HTTP_400_BAD_REQUEST,'error':serializer.errors,'message':'not created'})

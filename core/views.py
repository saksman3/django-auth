from django.core import exceptions
from django.shortcuts import render
from rest_framework import serializers

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework.exceptions import AuthenticationFailed
import jwt, datetime
from .serializers import UserSerializer
from .models import User

#Create Register View
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

#Create Login View
class LoginView(APIView):
    
    def auth(self):
        import requests
        url = 'https://auth.carto.com/oauth/token'
        my_data = {
                "grant_type":"client_credentials",
                "client_id":"LKlPopJ7DMRMzd0RddzsNKoNuZ5PfKw5",
                "client_secret":"99lLDhjvEOoGOZniCvUhsrhI0nI21bJINDAwyxX7QqgrpODC7bl18oeIR4bKhZAK",
                "audience":"carto-cloud-native-api"
                }
        response = requests.post(url,data=my_data)
        json_data = response.json()
        access_token = json_data['access_token']
        return access_token

    def post(self, request):
        email = request.data['email']
        password = request.data['password']
        
        #get user
        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not Found')
        if not user.check_password(password):
            raise AuthenticationFailed("Incorrect User Password")
        payload = {
            'id' : user.id,
            'exp' : datetime.datetime.now() + datetime.timedelta(minutes=60),
            'iat' : datetime.datetime.now()
        }
        token = jwt.encode(payload,'secret',algorithm='HS256')

        response = Response()
        response.set_cookie(key='token',value=token,httponly=True)
        access_token = self.auth()
        response.data = {
            'token':token,
            'access_token':access_token
        }
        return response

class UserView(APIView):
    def get(self,request):
        token = request.COOKIES.get('token')

        if not token:
            raise AuthenticationFailed("Unauthenticated")
        try:
            payload = jwt.decode(token,'secret',algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed("Session Expired.")
        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self,request):
        response = Response()
        response.delete_cookie('token')
        response.data={
            "message":"success"
        }
        return response
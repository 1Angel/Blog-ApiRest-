from django.contrib import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from users.models import Account
from users.API.serializers import RegistrationSerializer


@api_view(['POST'])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data = {}

        if serializer.is_valid():
            account = serializer.save()
            data['reponse'] = 'el registro fue exitoso'
            data['username'] = account.username
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['email'] = account.email
            data['phone_number'] = account.phone_number

            return Response(data)

        else:
            return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def login(request):
    data = {}
    if request.method =='POST':
        email = request.data.get('email')
        password = request.data.get('password')

        account = auth.authenticate(email=email, password=password)
        if account is not None:
            data['response'] = 'el login fue exitoso'
            data['username'] = account.username
            data['first_name'] = account.first_name
            data['last_name'] = account.last_name
            data['email'] = account.email
            data['phone_number'] = account.phone_number
            refresh = RefreshToken.for_user(account)

            data['token'] = {
                'access': str(refresh.access_token)
            }
            return Response(data)
        else:
            data['response'] = 'credenciales incorrectas'
            return Response(data, status.HTTP_500_INTERNAL_SERVER_ERROR)
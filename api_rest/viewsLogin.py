from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User
from django.contrib.auth.hashers import check_password
from rest_framework.authtoken.models import Token

@api_view(['POST'])
def ini_user(request):
    data = JSONParser().parse(request)

    usuario = data['username']
    clave = data['password']

    try:
        user = User.objects.get(username = usuario)
    except User.DoesNotExist:
        return Response("Usuario y/o contraseña incorrecto/s") # A futuro que no especifique en que se equivoco ("Usuario y/o clave incorrecta") 

    pass_valido = check_password(clave, user.password)
    if not pass_valido:
        return Response("Usuario y/o contraseña incorrecto/s")

    #Crear el token
    token,created = Token.objects.get_or_create(user = user)
    return Response(token.key)
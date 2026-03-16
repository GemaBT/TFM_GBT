"""
from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def inicio(request):
    return Response({"mensaje": "Hola, esta es mi primera API con Django"})

@api_view(['GET'])
def usuarios(request):
    return Response([
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Carlos"}
    ])

"""
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def inicio(request):
    return Response({"mensaje": "Hola, esta es mi primera API con Django"})

@api_view(['GET'])
def usuarios(request):
    return Response([
        {"id": 1, "nombre": "Ana"},
        {"id": 2, "nombre": "Carlos"}
    ])
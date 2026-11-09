from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Versement
from .serializers import VersementSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def createVersement(request):
  serializer = VersementSerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_versement(request):
  versements = Versement.objects.all()
  serializer = VersementSerializer(versements, many=True)  # !!!
  return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH', 'DELETE'])
def DetailsUpdateDeleteVersement(request, pk):
  versement = get_object_or_404(Versement, pk=pk)
  if request.method == 'GET':
    serializer = VersementSerializer(versement)
    return Response(serializer.data, status=status.HTTP_200_OK)
  
  elif request.method == 'PATCH':
    # partial=True allows editing only specified fields without requiring all fields
    serializer = VersementSerializer(versement, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
  elif request.method == 'DELETE':
    versement.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)
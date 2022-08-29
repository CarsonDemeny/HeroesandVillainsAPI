from rest_framework.decorators import api_view
from .models import Super
from .serializers import SuperSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status

# Create your views here.
@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        super = Super.objects.all()
        serializer = SuperSerializer(super,many=True)
        return Response(serializer.data, status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = SuperSerializer(data = request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status.HTTP_201_CREATED)


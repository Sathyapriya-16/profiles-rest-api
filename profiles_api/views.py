from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status
from profiles_api import serializers

class HelloApiView(APIView):
    """Test API View"""
    serializer_class = serializers.HelloSerializer
    def get(self, request, format=None):
        """Returns alist of  APIView"""
        an_apiview = [
            'Uses HTTP methoda as function(get, post, patch, put, delete)',
            'Is similiar to a traditional Djnago view',
            'Gives you the most control over you applocation logic',
            'Is mapped manually to URLs',
    ]
    return Response({'message':'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name"""
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            name=serializer.validated_data.get('name')
            message = f 'Hello {name}'
            return Response({'message': message})
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self, request, pk=None):
        """Handle updating object"""
        return Response({'method': 'PUT'})
    def patch(self, request, pk=None):
        """Handle partial update of an object"""
        return Response({'method': 'PATCH'})
    def delete(self, request, pk=None):
        """Delete object"""
        return Response({'method': 'DELETE'})



# Create your views here.

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from foodapp import models
from foodapp import serializers

class FoodViewer(APIView):
    
    def post(self, request):
        serializer = serializers.FoodListSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def get(self, request):
        categories = models.FoodCategory.objects.all()    
        serializer = serializers.FoodListSerializer(categories, many=True)
        return Response(serializer.data)
 

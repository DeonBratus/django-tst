from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers
import json

class FoodViewer(APIView):
    
    def get(self, request):
        data = {
            "msg": 'message'
        }
        return Response(data=data)

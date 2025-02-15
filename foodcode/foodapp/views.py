from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from foodapp import models
from foodapp import serializers


class FoodViewer(APIView):
    
    def get(self, request):
        food_items = models.Food.objects.filter(is_publish=True)
        food_categories = models.FoodCategory.objects.all()
        
        categories_data = serializers.FoodListSerializer(food_categories, many=True).data
        filtered_categories = []
        
        for category in categories_data:
            category_foods = food_items.filter(category_id=category['id'])
            if category_foods.exists():
                category_data = {key: category[key] for key in ('id', 'name_ru', 'name_en', 'name_ch', 'order_id')}
                category_data['foods'] = serializers.FoodSerializer(category_foods, many=True).data
                filtered_categories.append(category_data)
        
        response_data = {
            "categories": filtered_categories,
        }
        return Response(response_data)


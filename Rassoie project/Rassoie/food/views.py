from .serializers import FoodSerializer
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .models import Food

# Create your views here.

class FoodAPI(APIView):
    def get(self, request, id=None):
        data = Food.objects.all()
        food_serializer = FoodSerializer(data, many=True)
        return Response({"message":food_serializer.data})

    def post(self, request, id=None):
        data = JSONParser().parse(request)
        food_serializer = FoodSerializer(data= data)
        if food_serializer.is_valid():
            food_serializer.save()
            return Response({"food added":food_serializer.data})
        return Response({"message":food_serializer.errors})

    def put(self, request, id=None):
        if id:
            instance = Food.objects.get(food_id = id)
            parse_data = JSONParser().parse(request)
            food_serializer = FoodSerializer(instance, parse_data)
            if food_serializer.is_valid():
                food_serializer.save()
                return Response(food_serializer.data)
            else:
                return Response({"Output":"Invalid data. Please try again!"})
        return Response({"Output":"Please enter the ID"})
            
            

    def delete(self, request, id=None):
        if id:
            try:
                Food.objects.filter(
                    pk=id
                ).delete()
            except:
                return Response({"Error":"Food Data not found"})
        else:
            try:
                Food.objects.all().delete()
            except Exception as e:
                return Response({"error":"Something Went Wrong . Please Try Again!"})
        return Response({"Output":"Food Data deleted"})


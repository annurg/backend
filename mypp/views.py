from django.shortcuts import render, HttpResponse
from .models import City, Year
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CitySerializer, YearSerializer, DefaultSerializer
# Create your views here.
import json
@api_view(['GET'])
def main(request):
	if request.method == 'GET':    
		city = City.objects.all()
		city_avg = []
		for i in city:
			temp = [int(x.temperature) for x in i.cities.all()]
			city_avg.append({"name": i,
			 "temperature": sum(temp)/i.cities.all().count(),
			 })
		serializer = DefaultSerializer(city_avg, many=True,context={'request': request})
		# print(serializer, year)
		return 	Response(serializer.data)

@api_view(['GET'])
def year(request):
	if request.method == 'GET':    
		year = Year.objects.all()
		serializer = YearSerializer(year, many=True,context={'request': request})
		# print(serializer, year)
		return 	Response(serializer.data)

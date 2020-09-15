from rest_framework import serializers, relations
from .models import City, Year

class CitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = City
        fields = ('name')

class YearSerializer(serializers.HyperlinkedModelSerializer):
    city = serializers.CharField(source='city.name')
    class Meta:
        model = Year
        depth = 1
        fields = ('year', 'temperature', 'city')

class DefaultSerializer(serializers.Serializer):
	name = serializers.CharField(max_length=30)
	temperature = serializers.FloatField()
	
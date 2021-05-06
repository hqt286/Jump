from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    street = serializers.CharField()
    city = serializers.CharField()
    stateName = serializers.CharField()
    stateCode = serializers.CharField()
    county = serializers.CharField()
    zipCode = serializers.CharField()
    countryName = serializers.CharField()
    countryCode = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()

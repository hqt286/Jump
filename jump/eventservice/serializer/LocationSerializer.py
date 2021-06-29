from rest_framework import serializers


class LocationSerializer(serializers.Serializer):
    venueName = serializers.CharField()
    street = serializers.CharField()
    city = serializers.CharField()
    stateName = serializers.CharField()
    stateCode = serializers.CharField()
    county = serializers.CharField()
    zipCode = serializers.CharField()
    countryName = serializers.CharField()
    countryCode = serializers.CharField()
    latitude = serializers.DecimalField(max_digits=10, decimal_places=5)
    longitude = serializers.DecimalField(max_digits=10, decimal_places=5)

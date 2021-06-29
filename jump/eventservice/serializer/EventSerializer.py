from rest_framework import serializers
from eventservice.serializer.LocationSerializer import LocationSerializer


class EventSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    createdBy = serializers.CharField()
    createdOn = serializers.DateTimeField()
    eventTime = serializers.DateTimeField()
    title = serializers.CharField(max_length=255)
    description = serializers.CharField()
    location = LocationSerializer()

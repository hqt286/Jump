from django.http import JsonResponse
from eventservice.entity.Event import Event
from eventservice.entity.Location import Location
from eventservice.serializer.EventSerializer import EventSerializer
from eventservice.dao.DanceEventDAO import DanceEventDAO
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
import json

from rest_framework.response import Response


@api_view(['GET'])
def queryEvent(request, id):
    """
    Different way of querying an event will go in here. Assume all the method is GET
    """
    print("> queryEvent")
    event = DanceEventDAO.getById(id)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data, safe=False)


@api_view(['POST'])
def createEvent(request):
    """
    Endpoint for update or create a event
    TODO: If the event already id, reject it
    Think of a way to use geo location to store location
    https://acloudguru.com/blog/engineering/location-based-search-results-with-dynamodb-and-geohash
    """
    print("> createEvent")
    location = Location("June St")
    event = Event(createdBy="Tran", location=location)
    DanceEventDAO.create(event=event)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def updateEvent():
    pass


@api_view(['DELETE'])
def deleteEvent(request, id):
    """
    Endpoint for remove an event. This is only when the user want to remove an event
    """
    print("< deleteEvent")
    DanceEventDAO.removeById(int(id))
    return Response(status=status.HTTP_200_OK)


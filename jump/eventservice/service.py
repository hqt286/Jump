from django.http import JsonResponse
from eventservice.entity.Event import Event
from eventservice.entity.Location import Location
from eventservice.serializer.EventSerializer import EventSerializer
from eventservice.dao.DanceEventDAO import DanceEventDAO
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
import json
from dateutil import parser
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

    print("> createEvent")
    f = open("/home/hungtran/Desktop/bs/randomDances.json")
    allData = json.load(f)

    events = list()
    id = 0
    for data in allData['data']:
        dateTime = data["dateTime"]
        genre = data["danceGenres"]
        eventName = data["eventTitle"]
        venueName = data["location"]["venueName"]
        street = data["location"]["street"]
        city = data["location"]["city"]
        state = data["location"]["state"]
        zipCode = data["location"]["zipCode"]
        latitude = float(data["location"]["latitude"])
        longtitude = float(data["location"]["longtitude"])
        dateTime = parser.parse(dateTime)
        location = Location(venueName=venueName, street=street, city=city, stateName="Virginia", stateCode=state, county="", zipCode=zipCode, countryName="The United State Of America", countryCode="1", latitude=latitude, longitude=longtitude)
        event = Event(id=id, createdBy="Generator", location=location, eventTime=dateTime, title=eventName, description="")
        # DanceEventDAO.create(event=event)
        id = id + 1
        events.append(event)

    """
    Store 300 data points in the data base
    location, genre, time
    """
    """
    Endpoint for update or create a event
    Think of a way to use geo location to store location
    https://acloudguru.com/blog/engineering/location-based-search-results-with-dynamodb-and-geohash
    """
    serializer = EventSerializer(events, many=True)
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


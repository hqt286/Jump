from django.http import JsonResponse
from eventservice.entity.Event import Event
from eventservice.entity.Location import Location
from eventservice.serializer.EventSerializer import EventSerializer
from eventservice.dao.DanceEventDAO import DanceEventDAO


def queryEvents(request):
    """
    Different way of querying an event will go in here. Assume all the method is GET
    """
    if request.method != 'GET':
        return

    id = 123
    event = DanceEventDAO.getById(id)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data, safe=False)


def createEvent(request):
    """
    Endpoint for update or create a event
    """
    if request.method != 'POST' or request.method != "PUT":
        return

    location = Location("June St12")
    event = Event(createdBy="Tran1", location=location)
    DanceEventDAO.createOrUpdate(event=event)
    serializer = EventSerializer(event)
    return JsonResponse(serializer.data, safe=False)


def removeEvent(request):
    """
    Endpoint for remove an event. This is only when the user want to remove an event
    """
    DanceEventDAO.removeById(ID)

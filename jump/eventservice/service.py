from django.http import JsonResponse
from eventservice.entity.Event import Event
from eventservice.entity.Location import Location
from eventservice.serializer.EventSerializer import EventSerializer


def event_query(request):

    if request.method == 'GET':
        location = Location("June St")
        event = Event(createdBy="Tran", location=location)
        serializer = EventSerializer(event)
        return JsonResponse(serializer.data, safe=False)

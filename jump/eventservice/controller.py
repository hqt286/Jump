from django.urls import path
from eventservice import service
from django.conf.urls import url

DANCE_SERVICE_ENDPOINT = 'api/dance-service/'
QUERY_EVENT = DANCE_SERVICE_ENDPOINT + 'query-event'
CREATE_EVENT = DANCE_SERVICE_ENDPOINT + 'create-event'
DELETE_EVENT = DANCE_SERVICE_ENDPOINT + "delete-event"
urlpatterns = [
    url(QUERY_EVENT + r'/(?P<id>[0-9]+)$', service.queryEvent),
    path(CREATE_EVENT, service.createEvent),
    path(DELETE_EVENT, service.deleteEvent),
    url(DELETE_EVENT + r'/(?P<id>[0-9]+)$', service.deleteEvent),
    # path(QUERY_EVENT + "/<int:id>", service.removeEvent)
]

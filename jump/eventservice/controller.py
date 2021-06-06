from django.urls import path
from eventservice import service

DANCE_SERVICE_ENDPOINT = 'api/dance-service/'
QUERY_EVENT = DANCE_SERVICE_ENDPOINT + 'event-query'
urlpatterns = [
    path(QUERY_EVENT, service.queryEvents),
    path(QUERY_EVENT, service.createEvent),
    path(QUERY_EVENT + "/<int:id>", service.removeEvents)
]
urlpatterns = format_suffix_patterns(urlpatterns)

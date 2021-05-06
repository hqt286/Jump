from django.urls import path
from eventservice import service

DANCE_SERVICE_ENDPOINT = 'api/dance-service/'
QUERY_EVENT = DANCE_SERVICE_ENDPOINT + 'event-query'
urlpatterns = [
    path(QUERY_EVENT, service.event_query)
]

from eventservice.entity.Location import Location
from datetime import datetime


class Event:
    id: int
    createdBy: str
    createdOn: datetime
    title: str
    description: str
    location: Location
    eventTime: datetime

    def __init__(self, id=None, createdBy=None, eventTime=None, title=None, description=None, location=None):
        self.id = id
        self.createdBy = createdBy
        self.createdOn = datetime.now()
        self.eventTime = eventTime
        self.title = title
        self.description = description
        self.location = location

    # organizer

    def __str__(self) -> str:
        return super().__str__()

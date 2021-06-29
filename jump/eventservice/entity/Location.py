from django_core.utils import numbers


class Location:
    street: str
    city: str
    stateName: str
    stateCode: str
    county: str
    zipCode: str
    countryName: str
    countryCode: str
    latitude: numbers
    longitude: numbers

    def __init__(self, venueName,street=None, city=None, stateName=None, stateCode=None, county=None, zipCode=None,
                 countryName=None, countryCode=None, latitude=None, longitude=None):
        self.venueName = venueName
        self.street = street
        self.city = city
        self.stateName = stateName
        self.stateCode = stateCode
        self.county = county
        self.zipCode = zipCode
        self.countryName = countryName
        self.countryCode = countryCode
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self) -> str:
        return super().__str__()

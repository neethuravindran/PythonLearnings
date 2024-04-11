#Create a script called location that return the location parameters of any location you want.

from geopy.geocoders import Nominatim


def get_user_query():
    return input("Enter Location:  ")
    
def searchlocationdetails(query):
    # Initialize Nominatim API
    geolocator = Nominatim(user_agent="LocationApp")
    location = geolocator.geocode(query)
    print(location)
    print("The latitude of the location is: ", location.latitude)
    print("The longitude of the location is: ", location.longitude)
    cordinates = location.latitude, location.longitude
    location = geolocator.reverse(cordinates)
    address = location.raw['address']
    # Traverse the data
    city = address.get('city', '')
    state = address.get('state', '')
    country = address.get('country', '')
    print("The city is:: ", city)
    print("The state is: ", state)
    print("The country is: ", country)


if __name__ == "__main__":
    user_query = get_user_query()
    searchlocationdetails(user_query)
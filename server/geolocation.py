import requests
from timezonefinder import TimezoneFinder
from datetime import datetime
import pytz

def get_coordinates(city, state, api_key):
    """Get latitude and longitude of a location using a Geocoding API."""
    url = f"https://api.opencagedata.com/geocode/v1/json?q={city},{state}&key={api_key}"

    response = requests.get(url)

    data = response.json()
    
    if data['results']:
        location = data['results'][0]['geometry']
        return location['lat'], location['lng']
    else:
        raise ValueError("Invalid location. Unable to fetch coordinates.")

def adjust_time_for_timezone(lat, lng, dob, time):
    """Adjust the birth time for the local timezone."""
    tf = TimezoneFinder()
    timezone_str = tf.timezone_at(lat=lat, lng=lng)
    if timezone_str:
        local_timezone = pytz.timezone(timezone_str)
        naive_datetime = datetime.strptime(f"{dob} {time}", "%Y-%m-%d %H:%M:%S")
        local_datetime = local_timezone.localize(naive_datetime)
        utc_datetime = local_datetime.astimezone(pytz.utc)
        return utc_datetime
    else:
        raise ValueError("Could not determine timezone.")

if __name__ == "__main__":
    # Example usage
    api_key = "9e148c461c1843ecab4da2b9881e55b2"
    city = input("Enter city: ")
    state = input("Enter state: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    time = input("Enter time (HH:MM:SS): ")

    lat, lng = get_coordinates(city, state, api_key)
    adjusted_time = adjust_time_for_timezone(lat, lng, dob, time)

    print(f"Coordinates: Latitude={lat}, Longitude={lng}")
    print(f"Adjusted Time (UTC): {adjusted_time}")

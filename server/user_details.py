import ephem
import math
from db_connection import db
from geolocation import get_coordinates, adjust_time_for_timezone

# Function to determine zodiac sign based on celestial longitude
def get_zodiac(degrees):
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    index = int(degrees // 30)  # Each sign spans 30 degrees
    return zodiac_signs[index]

# Function to calculate the Ascendant (Lagna)
def calculate_ascendant(birth_date, lat, lon):
    observer = ephem.Observer()
    observer.date = birth_date
    observer.lat = str(lat)   # Latitude
    observer.lon = str(lon)   # Longitude

    # Get Sidereal Time at Birth
    sidereal_time = observer.sidereal_time()

    # Convert Sidereal Time to Degrees (Multiply by 15 because 1 hour = 15 degrees)
    sidereal_degrees = float(sidereal_time) * (180 / math.pi)

    # Add Longitude (correcting for Earth's rotation)
    ascendant_longitude = (sidereal_degrees + lon) % 360

    # Determine Ascendant Sign
    ascendant_sign = get_zodiac(ascendant_longitude)

    return ascendant_sign, ascendant_longitude

# Function to assign planets to houses
def assign_planets_to_houses(planets_positions, ascendant_sign):
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]

    # Map houses to zodiac signs based on ascendant
    ascendant_index = zodiac_signs.index(ascendant_sign)
    houses = {}
    
    for i in range(12):
        house_number = i + 1
        houses[house_number] = zodiac_signs[(ascendant_index + i) % 12]

    # Assign planets to houses
    planets_in_houses = {}
    for planet, (sign, degrees) in planets_positions.items():
        for house, house_sign in houses.items():
            if sign == house_sign:
                planets_in_houses[planet] = house
                break

    return houses, planets_in_houses

# Function to calculate planetary positions using ephem
def calculate_planetary_positions(birth_date):
    observer = ephem.Observer()
    observer.date = birth_date

    # List of planets
    planets = {
        "Sun": ephem.Sun(),
        "Moon": ephem.Moon(),
        "Mercury": ephem.Mercury(),
        "Venus": ephem.Venus(),
        "Mars": ephem.Mars(),
        "Jupiter": ephem.Jupiter(),
        "Saturn": ephem.Saturn(),
        "Uranus": ephem.Uranus(),
        "Neptune": ephem.Neptune(),
        "Pluto": ephem.Pluto(),
    }

    planetary_positions = {}

    for planet_name, planet_body in planets.items():
        planet_body.compute(observer)  # Compute planet's position for the observer's date and time

        # Longitude is the ecliptic position of the planet in degrees (0° to 360°)
        ecliptic_longitude = math.degrees(planet_body.ra) % 360

        # Determine the zodiac sign based on the longitude
        zodiac_sign = get_zodiac(ecliptic_longitude)

        # Store the planet's position and its zodiac sign
        planetary_positions[planet_name] = (zodiac_sign, ecliptic_longitude)

    return planetary_positions


# Function to insert user details and perform calculations
def insert_user_details(name, dob, time, gender, state, city):
    API_KEY = "9e148c461c1843ecab4da2b9881e55b2"

    # Get location coordinates
    lat, lng = get_coordinates(city, state, API_KEY)

    # Adjust time for the local timezone
    adjusted_time = adjust_time_for_timezone(lat, lng, dob, time)

    # Calculate Ascendant and houses
    birth_date = f"{dob} {adjusted_time.strftime('%H:%M:%S')}"
    ascendant_sign, ascendant_longitude = calculate_ascendant(birth_date, lat, lng)

    # Calculate planetary positions
    planetary_positions = calculate_planetary_positions(birth_date)

    # Assign planets to houses
    houses, planets_in_houses = assign_planets_to_houses(planetary_positions, ascendant_sign)

    # Prepare data for database insertion
    user_data = {
        "name": name,
        "dob": dob,
        "time": time,
        "adjusted_time": adjusted_time.strftime("%H:%M:%S"),
        "gender": gender,
        "state": state,
        "city": city,
        "latitude": lat,
        "longitude": lng,
        "ascendant": {
            "sign": ascendant_sign,
            "longitude": ascendant_longitude,
        },
        "houses": houses,
        "planetary_positions": planetary_positions,
        "planets_in_houses": planets_in_houses,
    }

    # Insert into database
    db['user_details'].insert_one(user_data)
    print("User details and astrology data inserted successfully.")

# Main script to handle user input
if __name__ == "__main__":
    print("Connected to Astra DB:", db.list_collection_names())

    # Take user input
    name = input("Enter your name: ")
    dob = input("Enter your date of birth (YYYY-MM-DD): ")
    time = input("Enter the time (HH:MM:SS): ")
    gender = input("Enter your gender: ")
    state = input("Enter your state: ")
    city = input("Enter your city: ")

    # Insert user details
    insert_user_details(name, dob, time, gender, state, city)

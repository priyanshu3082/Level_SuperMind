import swisseph as swe
from datetime import datetime

def calculate_planetary_positions(dob, time, lat, lng):
    # Convert date of birth (dob) and time to Julian Date (JD)
    birth_date = datetime.strptime(dob + " " + time, "%Y-%m-%d %H:%M:%S")
    jd = swe.julday(birth_date.year, birth_date.month, birth_date.day, birth_date.hour + birth_date.minute / 60 + birth_date.second / 3600)
    
    planetary_positions = {}

    # Define planet IDs as per Swiss Ephemeris
    planets = {
        'Sun': 0,
        'Moon': 1,
        'Mercury': 2,
        'Venus': 3,
        'Mars': 4,
        'Jupiter': 5,
        'Saturn': 6,
        'Uranus': 7,
        'Neptune': 8,
        'Pluto': 9
    }

    for planet, planet_id in planets.items():
        # Calculate position for each planet at the given JD
        result = swe.calc_ut(jd, planet_id)
        
        # Check if result contains longitude and latitude
        lon, lat = result[:2]  # Only extract longitude and latitude if there are 2 values
        dist = result[2] if len(result) > 2 else None  # Default distance to None if not available
        
        planetary_positions[planet] = {
            'longitude': lon,
            'latitude': lat,
            'distance': dist
        }

    return planetary_positions


def calculate_ascendant_and_houses(dob, time, lat, lng):
    # Convert date of birth and time to Julian Date (JD)
    birth_date = datetime.strptime(dob + " " + time, "%Y-%m-%d %H:%M:%S")
    jd = swe.julday(birth_date.year, birth_date.month, birth_date.day, birth_date.hour + birth_date.minute / 60 + birth_date.second / 3600)
    
    # Use Swiss Ephemeris to calculate the Ascendant and Houses
    ascendant = swe.houses(jd, lat, lng, b'A')  # b'A' means "Placidus house system"
    
    # Debugging: Print the ascendant data
    print("Ascendant data:", ascendant)
    
    # First position of the Ascendant in the Placidus system
    ascendant_position = ascendant[0][0] if ascendant and len(ascendant) > 0 else None
    
    houses = {}
    try:
        # Ensure we retrieve all 12 house cusps
        for i in range(12):
            house_key = f'House_{i+1}'
            houses[house_key] = ascendant[1][i]  # House cusp positions
    except IndexError:
        print("Error accessing house cusp positions")

    return {'ascendant': ascendant_position, 'houses': houses}

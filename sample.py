import ephem
import math

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

# Example Birth Details (Samastipur, Bihar, India)
birth_date = "2001/11/17 17:17"  # Format: YYYY/MM/DD HH:MM
latitude = 25.8593  # Latitude of Samastipur
longitude = 85.7781  # Longitude of Samastipur

# Calculate Ascendant (Lagna)
ascendant_sign, ascendant_longitude = calculate_ascendant(birth_date, latitude, longitude)
print(f"Ascendant (Lagna): {ascendant_sign} ({ascendant_longitude:.2f}°)")

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

# Example planetary positions (from Step 4 output)
planets_positions = {
    "Sun": ("Scorpio", 224.67),
    "Moon": ("Aries", 15.23),
    "Mercury": ("Scorpio", 212.45),
    "Venus": ("Sagittarius", 245.78),
    "Mars": ("Capricorn", 289.65),
    "Jupiter": ("Gemini", 90.34),
    "Saturn": ("Taurus", 54.23),
    "Uranus": ("Aquarius", 310.12),
    "Neptune": ("Capricorn", 289.98),
    "Pluto": ("Sagittarius", 269.34),
}

# Get house assignments
houses, planets_in_houses = assign_planets_to_houses(planets_positions, ascendant_sign)

# Display Houses
print("\nHouse Sign Mappings:")
for house, sign in houses.items():
    print(f"House {house}: {sign}")

# Display Planet Positions in Houses
print("\nPlanets in Houses:")
for planet, house in planets_in_houses.items():
    print(f"{planet} is in House {house}")

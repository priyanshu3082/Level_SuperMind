# import ephem

# # Get today's date
# today = ephem.now()

# # Compute the position of the Sun
# sun = ephem.Sun(today)

# print("Sun's Right Ascension:", sun.ra)
# print("Sun's Declination:", sun.dec)

import ephem

# Function to determine zodiac sign based on celestial longitude
def get_zodiac(degrees):
    zodiac_signs = [
        "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
        "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    index = int(degrees // 30)  # Each sign spans 30 degrees
    return zodiac_signs[index]

# Set the date of birth
birth_date = "2001/11/17 17:17"  # YYYY/MM/DD HH:MM format
observer = ephem.Observer()

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
    "Pluto": ephem.Pluto()
}

# Calculate positions and zodiac signs
for planet_name, planet in planets.items():
    planet.compute(birth_date)  # Compute the planet's position at birth time
    ecliptic_longitude = float(planet.hlong) * (180 / ephem.pi)  # Convert radians to degrees
    zodiac_sign = get_zodiac(ecliptic_longitude)  # Get zodiac sign
    print(f"{planet_name}: {zodiac_sign} ({ecliptic_longitude:.2f}°)")


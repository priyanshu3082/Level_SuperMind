import ephem
from opencage.geocoder import OpenCageGeocode
import datetime

# OpenCage API Key (Replace with your key)
OPENCAGE_API_KEY = "9e148c461c1843ecab4da2b9881e55b2"

# Function to get latitude and longitude
def get_lat_long(city, state):
    geocoder = OpenCageGeocode(OPENCAGE_API_KEY)
    query = f"{city}, {state}"
    results = geocoder.geocode(query)
    
    if results:
        lat = results[0]['geometry']['lat']
        lon = results[0]['geometry']['lng']
        return lat, lon
    else:
        return None, None

# Function to validate date and time format
def validate_datetime(date_str, time_str):
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")  # Validate date
        datetime.datetime.strptime(time_str, "%H:%M:%S")  # Validate time
        return True
    except ValueError:
        return False

# Function to calculate planetary positions and nakshatras
def get_planet_positions(date, time, lat, lon):
    planets = {
        "Sun": ephem.Sun(),
        "Moon": ephem.Moon(),
        "Mars": ephem.Mars(),
        "Mercury": ephem.Mercury(),
        "Jupiter": ephem.Jupiter(),
        "Venus": ephem.Venus(),
        "Saturn": ephem.Saturn(),
        "Rahu": ephem.Neptune(),  # Approximation for Rahu
        "Ketu": ephem.Uranus()    # Approximation for Ketu
    }
    
    datetime_str = f"{date} {time}"
    obs = ephem.Observer()
    obs.lat, obs.lon = str(lat), str(lon)
    obs.date = ephem.Date(datetime_str)

    planet_positions = {}
    for name, body in planets.items():
        body.compute(obs)
        # Calculate house position based on right ascension (RA)
        house_number = int((body.ra / (2 * ephem.pi)) * 12) + 1
        house_number = house_number if house_number <= 12 else house_number - 12
        nakshatra = ephem.constellation(body)  # Nakshatra and sign
        planet_positions[name] = {
            "house": house_number,
            "nakshatra": nakshatra[1],  # Zodiac sign
            "degrees": round(body.ra * (180 / ephem.pi), 2)  # Degrees
        }

    return planet_positions

# Function to determine the Ascendant (Lagna)
def calculate_ascendant(date, time, lat, lon):
    obs = ephem.Observer()
    obs.lat, obs.lon = str(lat), str(lon)
    obs.date = ephem.Date(f"{date} {time}")

    sun = ephem.Sun()
    sun.compute(obs)
    ascendant_sign = ephem.constellation(sun)[1]
    return ascendant_sign

# Function to generate Yogas (simple examples)
def calculate_yogas(planet_positions):
    yogas = []

    # Example Yogas (you can add more complex rules)
    if "Jupiter" in planet_positions and planet_positions["Jupiter"]["house"] == 9:
        yogas.append("Raja Yoga: Jupiter in the 9th house indicates good fortune and success.")

    if "Venus" in planet_positions and planet_positions["Venus"]["house"] == 7:
        yogas.append("Dhana Yoga: Venus in the 7th house signifies wealth and good relationships.")

    if "Saturn" in planet_positions and planet_positions["Saturn"]["house"] == 10:
        yogas.append("Karma Yoga: Saturn in the 10th house indicates discipline and career growth.")

    if not yogas:
        yogas.append("No significant yogas identified.")
    
    return yogas

# Function to display Dasha Periods (simplified)
def calculate_dasha():
    return {
        "Current Dasha": "Jupiter",
        "Next Dasha": "Saturn",
        "Following Dasha": "Mercury"
    }

# Main program
def main():
    print("🔮 Welcome to the Kundali Generator 🔮")
    
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
    tob = input("Enter your Time of Birth (HH:MM:SS in 24-hour format): ")
    state = input("Enter your State: ")
    city = input("Enter your City: ")

    # Validate date-time input
    if not validate_datetime(dob, tob):
        print("❌ Error: Invalid date or time format. Use YYYY-MM-DD for date and HH:MM:SS for time.")
        return

    lat, lon = get_lat_long(city, state)
    if lat is None:
        print("❌ Error: Unable to fetch latitude and longitude. Check city and state input.")
        return

    # Calculate Kundli data
    planet_positions = get_planet_positions(dob, tob, lat, lon)
    ascendant = calculate_ascendant(dob, tob, lat, lon)
    yogas = calculate_yogas(planet_positions)
    dasha = calculate_dasha()

    # Display Kundli Report
    print("\n### Kundali Report ###")
    print(f"👤 Name: {name}")
    print(f"📅 Date of Birth: {dob}")
    print(f"🕒 Time of Birth: {tob}")
    print(f"📍 Birth Location: {city}, {state} (Lat: {lat}, Lon: {lon})")

    print(f"\n🌟 Ascendant (Lagna): {ascendant}")
    print("\n🌌 Planetary Positions:")
    for planet, details in planet_positions.items():
        print(f"⭐ {planet}: House {details['house']}, Nakshatra: {details['nakshatra']}, Degrees: {details['degrees']}°")

    print("\n📖 Yogas Identified:")
    for yoga in yogas:
        print(f"- {yoga}")

    print("\n📅 Dasha Periods:")
    for period, planet in dasha.items():
        print(f"{period}: {planet}")

# Run the program
if __name__ == "__main__":
    main()

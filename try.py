import ephem
import requests
from opencage.geocoder import OpenCageGeocode
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
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

# Function to get planetary positions
def get_planet_positions(date, time, lat, lon):
    planets = {
        "Sun": ephem.Sun(),
        "Moon": ephem.Moon(),
        "Mars": ephem.Mars(),
        "Mercury": ephem.Mercury(),
        "Jupiter": ephem.Jupiter(),
        "Venus": ephem.Venus(),
        "Saturn": ephem.Saturn(),
        "Rahu": ephem.Neptune(),  # Approximation
        "Ketu": ephem.Uranus()     # Approximation
    }
    
    try:
        datetime_str = f"{date} {time}"  # Combine date and time
        obs = ephem.Observer()
        obs.lat, obs.lon = str(lat), str(lon)
        obs.date = ephem.Date(datetime_str)  # Correct conversion

        planet_positions = {}
        for name, body in planets.items():
            body.compute(obs)
            planet_positions[name] = (ephem.constellation(body), round(body.ra, 2), round(body.dec, 2))
        
        return planet_positions
    except ValueError as e:
        print("❌ Error: Invalid date-time format. Please use YYYY-MM-DD HH:MM:SS")
        exit()

# Function to determine zodiac sign
def get_zodiac(planet_positions):
    zodiac_mapping = {}
    for planet, (constellation, ra, dec) in planet_positions.items():
        zodiac_mapping[planet] = constellation[1]  # Extracts only the zodiac sign
    return zodiac_mapping

# Function to generate Kundali chart
def draw_kundali(planet_positions, zodiac_signs, name):
    img_size = 500
    img = Image.new("RGB", (img_size, img_size), "white")
    draw = ImageDraw.Draw(img)
    font = ImageFont.load_default()

    # Draw square grid for Kundali
    draw.rectangle([(0, 0), (img_size, img_size)], outline="black", width=3)
    draw.line([(0, 0), (img_size, img_size)], fill="black", width=3)
    draw.line([(img_size, 0), (0, img_size)], fill="black", width=3)

    house_positions = {
        "I": (220, 220), "II": (320, 120), "III": (420, 20),
        "IV": (220, 20), "V": (20, 20), "VI": (20, 120),
        "VII": (20, 220), "VIII": (20, 320), "IX": (20, 420),
        "X": (220, 420), "XI": (420, 420), "XII": (420, 320)
    }

    # Draw house numbers
    for house, pos in house_positions.items():
        draw.text(pos, house, fill="black", font=font)

    # Place planets in respective houses
    for planet, zodiac in zodiac_signs.items():
        pos = house_positions.get(zodiac, (200, 200))
        draw.text((pos[0] + 10, pos[1] + 10), planet[:3], fill="blue", font=font)

    kundali_path = f"{name}_kundali.png"
    img.save(kundali_path)
    print(f"✅ Kundali chart saved as {kundali_path}")

# Main program
def main():
    print("🔮 Welcome to the Kundali Generator 🔮")
    
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
    tob = input("Enter your Time of Birth (HH:MM:SS in 24-hour format): ")
    gender = input("Enter your Gender (Male/Female): ")
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

    planet_positions = get_planet_positions(dob, tob, lat, lon)
    zodiac_signs = get_zodiac(planet_positions)

    draw_kundali(planet_positions, zodiac_signs, name)

    # Print Kundali Report
    print("\n### Kundali Report ###")
    print(f"👤 Name: {name}")
    print(f"📅 Date of Birth: {dob}")
    print(f"🕒 Time of Birth: {tob}")
    print(f"⚧ Gender: {gender}")
    print(f"📍 Birth Location: {city}, {state} (Lat: {lat}, Lon: {lon})")

    print("\n🌌 Planetary Positions and Zodiac Signs:")
    for planet, (constellation, ra, dec) in planet_positions.items():
        print(f"⭐ {planet}: {constellation[1]} (RA: {ra}, Dec: {dec})")

    print("\n📖 Interpretation:")
    print("- ☀️ The Sun determines your core personality.")
    print("- 🌙 The Moon controls emotions and mind.")
    print("- 🔥 Mars signifies energy and aggression.")
    print("- 🧠 Mercury affects intelligence and communication.")
    print("- 🪐 Jupiter represents wisdom and growth.")
    print("- 💕 Venus governs love and beauty.")
    print("- ⏳ Saturn indicates karma and discipline.")
    print("- 🌑 Rahu & Ketu signify past-life karma and destiny.")

    print("\n✅ Your detailed Kundali chart is saved as an image.")

# Run the program
if __name__ == "__main__":
    main()

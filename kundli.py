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
    
    datetime_str = f"{date} {time}"
    obs = ephem.Observer()
    obs.lat, obs.lon = str(lat), str(lon)
    obs.date = datetime_str

    planet_positions = {}
    for name, body in planets.items():
        body.compute(obs)
        planet_positions[name] = (ephem.constellation(body), round(body.ra, 2), round(body.dec, 2))
    
    return planet_positions

# Function to determine zodiac sign
def get_zodiac(planet_positions):
    zodiac_mapping = {}
    for planet, (constellation, ra, dec) in planet_positions.items():
        zodiac_mapping[planet] = constellation[1]  # Extracts only the zodiac sign
    return zodiac_mapping

# Function to generate Kundali chart
def draw_kundali(planet_positions, zodiac_signs, name):
    try:
        img = Image.open("kundali_template.png")
    except FileNotFoundError:
        img = Image.new("RGB", (500, 500), "white")  # Creates a blank white image

    draw = ImageDraw.Draw(img)

    font = ImageFont.load_default()
    house_positions = {
        "I": (250, 250),
        "II": (350, 150),
        "III": (450, 50),
        "IV": (250, 50),
        "V": (50, 50),
        "VI": (50, 150),
        "VII": (50, 250),
        "VIII": (50, 350),
        "IX": (50, 450),
        "X": (250, 450),
        "XI": (450, 450),
        "XII": (450, 350),
    }

    # Draw house numbers
    for house, pos in house_positions.items():
        draw.text(pos, house, fill="black", font=font)

    # Place planets in respective houses
    for planet, zodiac in zodiac_signs.items():
        position = house_positions.get(zodiac, (200, 200))
        draw.text((position[0] + 20, position[1] + 20), planet[:3], fill="blue", font=font)

    img.save(f"{name}_kundali.png")
    print(f"Kundali chart saved as {name}_kundali.png")

# Main program
def main():
    name = input("Enter your name: ")
    dob = input("Enter your Date of Birth (YYYY-MM-DD): ")
    tob = input("Enter your Time of Birth (HH:MM:SS in 24-hour format): ")
    gender = input("Enter your Gender (Male/Female): ")
    state = input("Enter your State: ")
    city = input("Enter your City: ")

    # Get Latitude & Longitude
    lat, lon = get_lat_long(city, state)
    if lat is None:
        print("Error: Unable to fetch latitude and longitude. Check city and state input.")
        return

    # Get Planetary Positions
    planet_positions = get_planet_positions(dob, tob, lat, lon)

    # Determine Zodiac Signs
    zodiac_signs = get_zodiac(planet_positions)

    # Draw Kundali Chart
    draw_kundali(planet_positions, zodiac_signs, name)

    # Print Explanation
    print("\n### Kundali Report ###")
    print(f"Name: {name}")
    print(f"Date of Birth: {dob}")
    print(f"Time of Birth: {tob}")
    print(f"Gender: {gender}")
    print(f"Birth Location: {city}, {state} (Lat: {lat}, Lon: {lon})")

    print("\nPlanetary Positions and Zodiac Signs:")
    for planet, (constellation, ra, dec) in planet_positions.items():
        print(f"{planet}: {constellation[1]} (RA: {ra}, Dec: {dec})")

    print("\n### Interpretation ###")
    print("Your Kundali chart has been generated based on your planetary positions. Each planet influences different aspects of your life.")
    print("- The Sun determines your core personality.")
    print("- The Moon controls emotions and mind.")
    print("- Mars signifies energy and aggression.")
    print("- Mercury affects intelligence and communication.")
    print("- Jupiter represents wisdom and growth.")
    print("- Venus governs love and beauty.")
    print("- Saturn indicates karma and discipline.")
    print("- Rahu & Ketu signify past-life karma and destiny.")

    print("\nYour detailed Kundali chart is saved as an image.")

# Run the program
if __name__ == "__main__":
    main()

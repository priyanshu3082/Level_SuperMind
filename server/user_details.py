from geolocation import get_coordinates, adjust_time_for_timezone
from astrology_calculations import calculate_planetary_positions, calculate_ascendant_and_houses
from db_connection import db

API_KEY = "9e148c461c1843ecab4da2b9881e55b2"

def insert_user_details(name, dob, time, gender, state, city):
    """Insert user details into the user_details collection."""
    # Get location coordinates
    lat, lng = get_coordinates(city, state, API_KEY)
    
    # Adjust time for the local timezone
    adjusted_time = adjust_time_for_timezone(lat, lng, dob, time)
    
    # Calculate planetary positions and ascendant
    planetary_positions = calculate_planetary_positions(dob, adjusted_time.strftime("%H:%M:%S"), lat, lng)
    ascendant_and_houses = calculate_ascendant_and_houses(dob, adjusted_time.strftime("%H:%M:%S"), lat, lng)
    
    # Insert into database
    user_data = {
        "name": name,
        "dob": dob,
        "original_time": time,
        "adjusted_time_utc": adjusted_time,
        "gender": gender,
        "state": state,
        "city": city,
        "latitude": lat,
        "longitude": lng,
        "planetary_positions": planetary_positions,
        "ascendant_and_houses": ascendant_and_houses
    }
    db['user_details'].insert_one(user_data)
    print("User details and astrology data inserted successfully.")

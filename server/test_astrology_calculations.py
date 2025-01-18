import swisseph as swe
from datetime import datetime
from astrology_calculations import calculate_planetary_positions, calculate_ascendant_and_houses

def test_astrology_calculations():
    # Test data
    dob = "1990-01-01"
    time = "12:00:00"
    lat = 34.0522  # Latitude for Los Angeles
    lng = -118.2437  # Longitude for Los Angeles

    # Test planetary positions
    planetary_positions = calculate_planetary_positions(dob, time, lat, lng)
    print("Planetary Positions:", planetary_positions)

    # Test ascendant and houses
    ascendant_and_houses = calculate_ascendant_and_houses(dob, time, lat, lng)
    print("Ascendant and Houses:", ascendant_and_houses)

# Run the test
if __name__ == "__main__":
    test_astrology_calculations()

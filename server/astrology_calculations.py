import swisseph as swe

def calculate_planetary_positions(dob, time, lat, lng):
    """Calculate planetary positions at the given date, time, and location."""
    # Parse date and time
    date_time = f"{dob} {time}"
    
    # Convert to Julian Day
    jd = swe.julday(int(dob[:4]), int(dob[5:7]), int(dob[8:10]),
                    float(time[:2]) + float(time[3:5]) / 60 + float(time[6:]) / 3600)
    
    # Calculate planetary positions
    planets = ["Sun", "Moon", "Mercury", "Venus", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto"]
    positions = {}
    
    for planet_id, planet_name in zip(range(swe.SUN, swe.PLUTO + 1), planets):
        lon, lat, dist = swe.calc_ut(jd, planet_id)
        positions[planet_name] = {"longitude": lon, "latitude": lat, "distance": dist}
    
    return positions

def calculate_ascendant_and_houses(dob, time, lat, lng):
    """Calculate ascendant and house positions."""
    jd = swe.julday(int(dob[:4]), int(dob[5:7]), int(dob[8:10]),
                    float(time[:2]) + float(time[3:5]) / 60 + float(time[6:]) / 3600)
    ascmc, cusps = swe.houses(jd, lat, lng, b'A')  # A = Placidus house system
    return {
        "ascendant": ascmc[0],
        "houses": cusps[:12]
    }

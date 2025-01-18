import matplotlib.pyplot as plt
import numpy as np

# Define the zodiac signs and house placements
zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]

# Example planetary positions (House assignments from Step 5)
planets_in_houses = {
    "Sun": 9, "Moon": 2, "Mercury": 9, "Venus": 10, "Mars": 11,
    "Jupiter": 4, "Saturn": 3, "Uranus": 12, "Neptune": 11, "Pluto": 10
}

# Create a circular chart
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(-1, 1)
ax.set_ylim(-1, 1)

# Draw the circle
circle = plt.Circle((0, 0), 1, color='black', fill=False, linewidth=2)
ax.add_patch(circle)

# Draw 12 equal sections for zodiac signs
for i in range(12):
    angle = i * (360 / 12)
    x = np.cos(np.radians(angle))
    y = np.sin(np.radians(angle))
    ax.plot([0, x], [0, y], color="black", linewidth=2)

# Place zodiac labels
for i, sign in enumerate(zodiac_signs):
    angle = (i + 0.5) * (360 / 12)  # Midpoint of each section
    x = 0.75 * np.cos(np.radians(angle))
    y = 0.75 * np.sin(np.radians(angle))
    ax.text(x, y, sign, fontsize=10, ha='center', va='center', fontweight='bold')

# Place planets in their houses
for planet, house in planets_in_houses.items():
    angle = (house - 1) * (360 / 12) + 15  # Adjust to position planets within sections
    x = 0.5 * np.cos(np.radians(angle))
    y = 0.5 * np.sin(np.radians(angle))
    ax.text(x, y, planet, fontsize=12, ha='center', va='center', color="red")

# Hide axes
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

plt.title("Birth Chart (Kundali)")
plt.show()

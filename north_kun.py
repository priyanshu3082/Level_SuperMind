import matplotlib.pyplot as plt

# Define the house positions in North Indian format
house_positions = {
    1: (2, 3),  2: (1, 3),  3: (1, 2),  4: (1, 1),
    5: (2, 1),  6: (3, 1),  7: (3, 2),  8: (3, 3),
    9: (2, 4),  10: (1, 4), 11: (3, 4), 12: (3, 5)
}

# Example planetary positions (House assignments)
planets_in_houses = {
    "Sun": 9, "Moon": 2, "Mercury": 9, "Venus": 10, "Mars": 11,
    "Jupiter": 4, "Saturn": 3, "Uranus": 12, "Neptune": 11, "Pluto": 10
}

# Create the figure and axis
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(0, 4)
ax.set_ylim(0, 5)

# Draw the square for the chart
plt.plot([1, 3, 3, 1, 1], [1, 1, 4, 4, 1], 'black', linewidth=2)

# Draw the diagonal lines for diamond shape
plt.plot([1, 2, 3, 2, 1], [1, 2, 1, 0, 1], 'black', linewidth=2)
plt.plot([1, 2, 3, 2, 1], [4, 3, 4, 5, 4], 'black', linewidth=2)

# Draw inner cross lines
plt.plot([2, 2], [1, 4], 'black', linewidth=2)
plt.plot([1, 3], [2.5, 2.5], 'black', linewidth=2)

# Label the houses (1-12)
for house, (x, y) in house_positions.items():
    ax.text(x, y, str(house), fontsize=12, ha='center', va='center', fontweight="bold")

# Place planets in respective houses
for planet, house in planets_in_houses.items():
    px, py = house_positions[house]
    ax.text(px, py - 0.2, planet, fontsize=10, ha='center', va='center', color="red")

# Hide axes
ax.set_xticks([])
ax.set_yticks([])
ax.axis("off")

plt.title("North Indian Kundali Chart")
plt.show()

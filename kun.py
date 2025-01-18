import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Define house labels
house_labels = {1: "I", 2: "II", 3: "III", 4: "IV", 5: "V", 6: "VI",
                7: "VII", 8: "VIII", 9: "IX", 10: "X", 11: "XI", 12: "XII"}

# Example planetary positions (House assignments)
planets_in_houses = {
    "Sun": 1, "Moon": 2, "Mercury": 3, "Venus": 4, "Mars": 5,
    "Jupiter": 7, "Saturn": 9, "Rahu": 11, "Ketu": 6
}

# Function to create a square Kundli chart
def plot_kundli(house_labels, planets_in_houses):
    # Set up the plot
    fig, ax = plt.subplots(figsize=(8, 8))
    ax.set_xlim(-1, 1)
    ax.set_ylim(-1, 1)
    ax.axis('off')

    # Define the key points for the diamond layout
    diamond_points = {
        1: (0, 0.6), 2: (0.3, 0.3), 3: (0.6, 0), 4: (0.3, -0.3),
        5: (0, -0.6), 6: (-0.3, -0.3), 7: (-0.6, 0), 8: (-0.3, 0.3),
        9: (0.6, 0.6), 10: (0.6, -0.6), 11: (-0.6, -0.6), 12: (-0.6, 0.6)
    }

    # Connect points to form houses
    lines = [
        [diamond_points[1], diamond_points[9], diamond_points[3], diamond_points[10], diamond_points[1]],  # Top
        [diamond_points[5], diamond_points[10], diamond_points[7], diamond_points[11], diamond_points[5]],  # Bottom
        [diamond_points[1], diamond_points[8], diamond_points[7], diamond_points[12], diamond_points[1]],  # Left
        [diamond_points[3], diamond_points[9], diamond_points[11], diamond_points[6], diamond_points[3]],  # Right
    ]

    # Draw the diamond shapes for the grid
    for line in lines:
        poly = Polygon(line, closed=True, edgecolor='black', fill=None, linewidth=2)
        ax.add_patch(poly)

    # Add house numbers to the chart
    for house, pos in diamond_points.items():
        ax.text(pos[0], pos[1], house_labels.get(house, ""), fontsize=12, ha="center", va="center", fontweight="bold")

    # Add planets in their respective houses
    for planet, house in planets_in_houses.items():
        pos = diamond_points[house]
        ax.text(pos[0], pos[1] - 0.05, planet, fontsize=10, ha="center", va="center", color="red")

    plt.title("Vedic Kundli Chart", fontsize=16, fontweight="bold")
    plt.show()

# Plot the Kundli
plot_kundli(house_labels, planets_in_houses)

from matplotlib import pyplot as plt
from matplotlib.colors import Normalize
import numpy as np

# Number of biospheres to plot
num_biospheres = 42

# Age of the universe in billion years
age_of_universe = 13.7 

# Estimated death of the universe in billion years
death_of_universe = 22 

# Diameter of the universe in billion light years
diameter_of_universe = 93 

# Set up 3D figure and axes
plt.style.use("dark_background")
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# Set limits of the plot
ax.set_xlim(-diameter_of_universe/2, diameter_of_universe/2)
ax.set_ylim(-diameter_of_universe/2, diameter_of_universe/2)
ax.set_zlim(0, death_of_universe)


# Set the labels for each plot axis
ax.set_xlabel("X-Space in Billions of Light Years")
ax.set_ylabel("Y-Space in Billions of Light Years")
ax.set_zlabel("Z-Time in Billions of Light Years Since Big Bang")

# Create a colormap for plot 
cmap = plt.get_cmap('viridis')

# Expanding at the speed of light would allow for a max expansion radius equal to the years to reach the death of the universe. 
min_cone_radius = 0
max_cone_radius = death_of_universe
# Use the Normalize class to map the radius values to the colormap
norm = Normalize(vmin=0, vmax=death_of_universe)

# Loop through and plot each biosphere
for i in range(num_biospheres):

    # This will represent the end of the expanding biosphere
    max_radius_expansion = np.random.uniform(min_cone_radius, max_cone_radius)
    # Shift the starting postions, representative of when and where the biosphere begins
    z_shift = np.random.uniform(0, age_of_universe)
    x_shift = np.random.uniform(-diameter_of_universe/2, diameter_of_universe/2)
    y_shift = np.random.uniform(-diameter_of_universe/2, diameter_of_universe/2)

    # Create the mesh in polar coordinates
    radius = np.linspace(0, max_radius_expansion, 16)
    theta = np.linspace(0, 2*np.pi, 32)
    radius, theta = np.meshgrid(radius, theta)

    # Express the mesh in the cartesian system
    x = radius*np.cos(theta)
    y = radius*np.sin(theta) 
    z = np.sqrt(x**2 + y**2)

    # Shift coordinates
    x += x_shift
    y += y_shift
    z += z_shift

    # Set the color of the cone, based on it's outer radius
    colors = cmap(norm(radius))

    # Plot a cone surface, representing the expanding bioshere
    ax.plot_surface(x, 
                    y, 
                    z, 
                    alpha=0.8, 
                    antialiased=True,
                    facecolors=colors)

# Show plot
plt.show()

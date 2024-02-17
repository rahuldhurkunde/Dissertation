import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import rc

rc('font', family='serif', weight = 'bold')
rc('text', usetex=True)

# Define the angles
theta = np.linspace(0, np.pi, 500)
phi = np.linspace(0, 2*np.pi, 500)
theta, phi = np.meshgrid(theta, phi)

# Antenna pattern functions (simplified)
F_plus = 0.5 * (1 + np.cos(theta)**2) * np.cos(2*phi)
F_cross = np.cos(theta) * np.sin(2*phi)

# Convert to Cartesian coordinates for the plot
x = F_cross * np.sin(theta) * np.cos(phi)
y = F_cross * np.sin(theta) * np.sin(phi)
z = F_cross * np.cos(theta)

# Plotting
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Create a color map based on z values
color_map = plt.get_cmap('viridis')
norm = plt.Normalize(z.min(), z.max())
colors = color_map(norm(z))

# Plot the surface with the color gradient
surf = ax.plot_surface(x, y, z, facecolors=colors, alpha=0.4)

# Add a color bar
mappable = plt.cm.ScalarMappable(cmap=color_map, norm=norm)
mappable.set_array(z)
#fig.colorbar(mappable, ax=ax, shrink=0.5, aspect=5)

# Hide the axes' panes (background)
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False

# Hide the axes' lines
ax.xaxis.line.set_visible(False)
ax.yaxis.line.set_visible(False)
ax.zaxis.line.set_visible(False)

ax.set_title(r'$F_{\times}(\alpha,\delta)$')
ax.set_xlabel('$x$')
ax.set_ylabel('$y$')
ax.set_zlabel('$z$')

plt.show()


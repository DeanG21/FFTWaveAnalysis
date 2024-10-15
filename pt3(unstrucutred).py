import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L = 0.5 + 1098/10000
num_elements = 200
time_steps = 10
dt = 0.00001


# Variable tension and mass per unit length along the string
tension = np.linspace(100, 10, num_elements)  # Tension decreasing from base to tip
mu = np.linspace(0.01, 0.02, num_elements)    # Mass per unit length increasing from base to tip


# Spatial discretization
x = np.linspace(0, L, num_elements)
dx = L / (num_elements-1)

# Arrays for displacements
y = np.zeros(num_elements)
y_new = np.zeros(num_elements)
y_old = np.zeros(num_elements)

# For the middle pluck scenario
d0 = 0.03  # displacement
d0_loc = 0.1  # For middle pluck

# Set the initial displacement
y[np.where(x <= d0_loc*L)] = d0/(d0_loc*L) * x[np.where(x <= d0_loc*L)]
y[np.where(x > d0_loc*L)] = -d0/((1.0-d0_loc)*L) * (x[np.where(x > d0_loc*L)] - L)

y_old = y.copy()

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, y, 'r', lw=4)

def update(frame):
    global y, y_old, y_new, mu, tension, dt, dx
    c2 = tension / mu  # Speed squared, now an array
    for i in range(1, num_elements - 1):
        y_new[i] = (2*y[i] - y_old[i] + c2[i] * dt**2 / dx**2 * (y[i+1] - 2*y[i] + y[i-1]))
    
    # Free boundaries condition
    y_new[0] = y_new[1]
    y_new[-1] = y_new[-2]
    
    # Swap arrays for the next step
    y_old, y, y_new = y, y_new, y_old
    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, update, frames=time_steps, blit=True, interval=0.1)

ax.set_xlim(0, L)
ax.set_ylim(-0.06, 0.06)  # Adjust based on maximum expected displacement
ax.set_xlabel('Position along the string (m)')
ax.set_ylabel('Displacement (m)')
ax.set_title('Wave Propagation on a Varying Tension and µ String')
ax.grid(True)

plt.tight_layout()
plt.show()



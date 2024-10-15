import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L = 3  # Length of the string
num_elements = 200  # Number of elements or segments
time_steps = 2000  # Number of time steps to simulate
dt = 0.001  # Time step size
c = 10  # Wave speed on the string

def initial_displacement(x):
    return np.exp(-40*(x - L/4)**2) #change to L/2 for pluck in middle 

# Define the spatial discretization
dx = L / num_elements

# Define arrays to hold the string displacements
y = np.zeros(num_elements)
y_new = np.zeros(num_elements)
y_old = np.zeros(num_elements)

# Set the initial displacement
y += initial_displacement(np.linspace(0, L, num_elements))
y_old += y

# Setup the figure and axis for the animation
fig, ax = plt.subplots(figsize=(10, 6))
ax.set_xlim(0, L)
ax.set_ylim(-1, 1)
line, = ax.plot(np.linspace(0, L, num_elements), y, 'r', lw=2)

def animate(t):
    global y, y_new, y_old
    for i in range(1, num_elements - 1):
        y_new[i] = (2*y[i] - y_old[i] + c**2 * dt**2 / dx**2 * (y[i+1] - 2*y[i] + y[i-1]))
    y_old = y.copy()
    y = y_new.copy()
    
    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, animate, frames=time_steps, interval=dt*1000, repeat=False)
plt.xlabel('Position along the string')
plt.ylabel('Displacement')
plt.title('Wave Propagation on a String')
plt.grid(True)
plt.show()

# Calculate the Courant number
courant_number = c * dt / dx
# Print the Courant number
print(f"Courant number: {courant_number}")
# Check if the Courant number satisfies the CFL condition for stability
if courant_number <= 1:
    print("The simulation is likely stable (CFL condition is satisfied).")
else:
    print("Warning: The simulation may be unstable (CFL condition is not satisfied).")
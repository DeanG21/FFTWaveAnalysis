import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# parameters 
L = 0.5 + 1098/10000 
num_elements = 200  
time_steps = 1  
dt = 0.00001  
tension = 100  
mu = 0.01  
c = np.sqrt(tension/mu) 

# Set up the spatial domain for the simulation
x = np.linspace(0, L, num_elements)  
dx = L / num_elements  

# Initialize arrays to store the string's displacement
y = np.zeros(num_elements)  
y_new = np.zeros(num_elements)  
y_old = np.zeros(num_elements)  

# initial conditions for the plucked string
d0 = 0.01  
d0_loc = 0.1  # Location of the pluck as a fraction of the string length

# initial displacement profile based on the pluck location
y[np.where(x <= d0_loc*x[-1])] = d0/(d0_loc*x[-1]) * x[np.where(x <= d0_loc*x[-1])]
y[np.where(x > d0_loc*x[-1])] = -d0/((1.0-d0_loc)*x[-1]) * (x[np.where(x > d0_loc*x[-1])] - x[-1])
y_old = y.copy()  

# Set up the plotting environment
fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x, y, 'r')  

# Define the update function for the animation
def update(frame):
    global y, y_old, y_new, c, dt, dx
    # Update the string displacement using the finite difference method
    for i in range(1, num_elements - 1):
        y_new[i] = (2*y[i] - y_old[i] + c**2 * dt**2 / dx**2 * (y[i+1] - 2*y[i] + y[i-1]))
    y_old = y.copy()
    y = y_new.copy()
    line.set_ydata(y)
    return line,

# Create an animation
ani = FuncAnimation(fig, update, frames=time_steps, blit=True, interval=1)

# Set up the axes and labels
ax.set_xlim(0, L)
ax.set_ylim(-0.012, 0.012)  
ax.set_xlabel('Position along the string (m)')
ax.set_ylabel('Displacement (m)')
ax.set_title('Wave Propagation on a Plucked String')
ax.grid(True) 

plt.tight_layout()  
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

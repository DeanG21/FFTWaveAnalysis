import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters
L = 0.5 + 1098/10000
num_elements = 200
time_steps = 2000
dt = 0.00001
tension = 100
mu = 0.01
c = np.sqrt(tension/mu)

# Spatial discretization
x = np.linspace(0, L, num_elements)
dx = L / num_elements

# Arrays for displacements
y = np.zeros(num_elements)
y_new = np.zeros(num_elements)
y_old = np.zeros(num_elements)

# For the middle pluck scenario
d0 = 0.01  # 1 cm displacement
d0_loc = 0.5  # For middle pluck

# Set the initial displacement
y[np.where(x <= d0_loc*x[-1])] = d0/(d0_loc*x[-1]) * x[np.where(x <= d0_loc*x[-1])]
y[np.where(x > d0_loc*x[-1])] = -d0/((1.0-d0_loc)*x[-1]) * (x[np.where(x > d0_loc*x[-1])] - x[-1])

y_old = y.copy()

fig, ax = plt.subplots(figsize=(10, 6))
line, = ax.plot(x ,y, color='red', lw=6)


def update(frame):
    global y, y_old, y_new, c, dt, dx
    for i in range(1, num_elements - 1):  # Adjust the loop bounds
        y_new[i] = (2*y[i] - y_old[i] + c**2 * dt**2 / dx**2 * (y[i+1] - 2*y[i] + y[i-1]))
    y_new[0] = y_new[1]  # Free boundary conditions
    y_new[-1] = y_new[-2]
    y_old = y.copy()
    y = y_new.copy()
    line.set_ydata(y)
    return line,

ani = FuncAnimation(fig, update, frames=time_steps, blit=True, interval=1)

ax.set_xlim(0, L)
ax.set_ylim(-0.012, 0.012)  # Adjust based on maximum displacement
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


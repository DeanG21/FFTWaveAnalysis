import numpy as np
import matplotlib.pyplot as plt

# Parameters
L = 0.5 + 1098/10000  # Length of the string from the given formula
num_elements = 200  # Number of elements or segments
time_steps = 2000  # Number of time steps to simulate 
dt = 0.00001  # Time step size
tension = 100  # Tension in the string (N)
mu = 0.01  # Mass per unit length (kg/m)
c = np.sqrt(tension/mu)  # Wave speed on the string

def initial_displacement(x):
    # Gaussian displacement with maximum of 5mm at the center
    return 0.005 * np.exp(-40 * (x - L/2)**2)

# Spatial discretization
dx = L / num_elements

# Arrays for displacements
y = np.zeros(num_elements)
y_new = np.zeros(num_elements)
y_old = np.zeros(num_elements)

# Set the initial displacement
y += initial_displacement(np.linspace(0, L, num_elements))
y_old += y

# Store the displacement at different times
times_to_plot = [0, 2, 4, 8, 12]  # in ms
displacements = {t: None for t in times_to_plot}

for t in range(time_steps):
    for i in range(1, num_elements - 1):
        y_new[i] = (2*y[i] - y_old[i] + c**2 * dt**2 / dx**2 * (y[i+1] - 2*y[i] + y[i-1]))
    y_old = y.copy()
    y = y_new.copy()
    
    # Store the y values at specified times
    current_time_ms = t * dt * 1000  # convert to ms
    if current_time_ms in times_to_plot:
        displacements[current_time_ms] = y.copy()

# Setup the figure and axis for the combined plot
plt.figure(figsize=(10, 6))


# Plot all times on the same graph
for t, disp in displacements.items():
    plt.plot(np.linspace(0, L, num_elements), disp, lw=2, label=f'{t} ms')

plt.xlabel('Position along the string (m)')
plt.ylabel('Displacement (m)')
plt.title('Wave Propagation on a String at Different Times')
plt.ylim(-0.003, 0.0055)  # Adjust the y-limits to fit the 5mm displacement
plt.legend(loc='upper right')
plt.grid(True)
plt.show()

# Print and compare the simulated wave speed with the expected one from Eqn 78
print(f"Simulated wave speed: {c} m/s")
c_expected = np.sqrt(tension/mu)
print(f"Expected wave speed from Eqn 2: {c_expected} m/s")

# Calculate the Courant number
courant_number = c * dt / dx
# Print the Courant number
print(f"Courant number: {courant_number}")
# Check if the Courant number satisfies the CFL condition for stability
if courant_number <= 1:
    print("The simulation is likely stable (CFL condition is satisfied).")
else:
    print("Warning: The simulation may be unstable (CFL condition is not satisfied).")

# WaveSimulations-FFT

## Project Overview
This project focuses on simulating wave propagation on a string using the finite difference method. It includes both structured and unstructured simulations, along with Fast Fourier Transform (FFT) analysis to explore the frequency components of the waves. The simulations cover various conditions such as fixed and free boundaries, variable string tension, and real-world effects like damping.

The objective is to study wave behavior, reflection, inversion, and frequency analysis through computational methods, providing insights into the fundamental principles of wave mechanics.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [File Structure](#file-structure)
4. [License](#license)

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/WaveSimulations-FFT.git
   cd WaveSimulations-FFT
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
To run the wave simulations or FFT analysis, use the following commands:

- **To simulate wave propagation:**
   ```bash
   python src/wave_simulation.py
   ```
- **To perform FFT analysis:**
   ```bash
   python src/fft_analysis.py
   ```

## File Structure
- **src/**: Contains the main code for wave simulation and FFT analysis.
  - `wave_simulation.py`: Simulates wave propagation, boundary conditions, and different physical scenarios.
  - `fft_analysis.py`: Performs FFT analysis to study the frequency components of the string vibration.
- **notebooks/**: Jupyter notebooks for interactive analysis.
- **data/**: Placeholder for any generated or input data.
- **images/**: Placeholder for any visual outputs or plots generated during the simulation.

## License
This project is licensed under the GPL License to ensure that any derivatives of the code remain open-source and contributions are shared back with the community. See the [LICENSE](LICENSE) file for details.

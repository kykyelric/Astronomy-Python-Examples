import numpy as np
import matplotlib.pyplot as plt

def planck_equation(wavelength, temp):
    """
    Calculate the spectral radiance of a black body using Planck's law.
    
    Parameters:
    wavelength (array-like): Wavelength(s) in meters.
    temp (float): Temperature of the black body in Kelvin.
    
    Returns:
    array-like: Spectral radiance at each wavelength.
    """
    # Constants (SI units)
    h = 6.62607015e-34  # Planck's constant (J * s)
    c = 299792458       # Speed of light (m/s)
    k = 1.380649e-23    # Boltzmann constant (J/K)
    
    # Planck's equation parts
    part1 = (2 * h * c**2) / (wavelength**5)
    part2 = np.exp((h * c) / (wavelength * temp * k)) - 1
    spectral_radiance = part1 / part2  # Planck's law
    
    return spectral_radiance

def plot_planck(spectral_radiance, temp, wavelength_range, save_name='frame.png'):
    """
    Plot the spectral radiance of a black body as a function of wavelength.
    
    Parameters:
    spectral_radiance (array-like): Spectral radiance at each wavelength.
    temp (float): Temperature of the black body in Kelvin.
    wavelength_range (array-like): Wavelength range corresponding to the radiance.
    save_name (str): Name of the file to save the plot.
    """
    # Find the maximum spectral radiance and its corresponding wavelength
    max_radiance = np.max(spectral_radiance)
    peak_wavelength_index = np.argmax(spectral_radiance)
    peak_wavelength = wavelength_range[peak_wavelength_index]

    # Plot the blackbody function and the peak wavelength
    plt.plot(wavelength_range, spectral_radiance, label='Blackbody Function')
    plt.plot([peak_wavelength, peak_wavelength], [0, max_radiance], 'r--', label=f'Peak Wavelength = {round(peak_wavelength, 10)} m')
    plt.xlabel('Wavelength (m)')
    plt.ylabel('Spectral Radiance (W m$^{-3}$ sr$^{-1}$)')
    plt.ylim(0, 7e13)
    plt.title(f'Blackbody Function for T = {temp} K')
    plt.legend()
    plt.savefig(save_name)
    plt.close()

# Test parameters
temp_range = np.arange(4500, 7025, 25)
wavelength_range = np.linspace(100e-9, 2e-6, 1000)  # Range of wavelengths (100 nm to 2 µm)
save_path = '/Users/kykyelric/Sync/Astronomy-Python-Examples/planck_anim/Frames/'

# Loop through temperature range and generate plots
for i, temp in enumerate(temp_range):
    # Calculate spectral radiance using Planck's equation
    spectral_radiance = planck_equation(wavelength_range, temp)
    
    # Generate the file name for saving the plot
    file_name = f'frame{str(i).zfill(3)}.png'
    save_name = save_path + file_name
    
    # Plot and save the figure
    plot_planck(spectral_radiance, temp, wavelength_range, save_name)

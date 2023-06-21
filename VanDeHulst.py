

import numpy as np
import matplotlib.pyplot as plt

# Define the parameters
n_nucleus = 1.42
n_cytoplasm = 1.38
d_nucleus_1 = 6e-6
d_nucleus_2 = 8e-6

# Define the range of wavelengths to consider
wavelengths = np.linspace(300e-9, 800e-9, 501)

# Calculate the size parameter for each nucleus at each wavelength
k_1 = 2*np.pi*n_nucleus*d_nucleus_1 / wavelengths
k_2 = 2*np.pi*n_nucleus*d_nucleus_2 / wavelengths

# Calculate the complex refractive index of each nucleus at each wavelength
m_1 = n_nucleus / n_cytoplasm * (1 + 1j*2/3*(k_1**3)/(n_nucleus**2))
m_2 = n_nucleus / n_cytoplasm * (1 + 1j*2/3*(k_2**3)/(n_nucleus**2))

# Calculate the total scattering cross-section of each nucleus at each wavelength
sigma_1 = (2*np.pi/wavelengths)**4 * np.abs((m_1**2 - 1) / (m_1**2 + 2))**2 * d_nucleus_1**6
sigma_2 = (2*np.pi/wavelengths)**4 * np.abs((m_2**2 - 1) / (m_2**2 + 2))**2 * d_nucleus_2**6

# Plot the results
plt.plot(wavelengths*1e9, sigma_1*1e12, label='Normal')
plt.plot(wavelengths*1e9, sigma_2*1e12, label='Leukemic')
plt.xlabel('Wavelength (nm)')
plt.ylabel('Scattering Cross-Section (um^2)')
plt.legend()
plt.show()

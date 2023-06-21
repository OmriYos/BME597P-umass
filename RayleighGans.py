
import numpy as np
import matplotlib.pyplot as plt


particle_sizes = [5e-9, 50e-9, 500e-9] # in meters
lambda_range = np.arange(300e-9, 801e-9, 1e-9) # in meters
theta = 180
m = 1.05 # relative refractive index
V = 299792458 # m/s

def rayleigh_gans_intensity(lambda_, particle_size):
    radius = particle_size / 2
    k = 2*np.pi/lambda_
    u = 2*k*particle_size*np.sin(theta/2)
    p = ((3 * (np.sin(u) - u * np.cos(u)) / u**3)**2)
    intensity = ((np.pi**2)*(V**2)/(radius**2)*(lambda_**4))*((m - 1)**2)*(np.cos(theta)**2)*p
    return intensity
    

fig, ax = plt.subplots()
for particle_size in particle_sizes:
    intensity = rayleigh_gans_intensity(lambda_range, particle_size)
    ax.semilogy(lambda_range, intensity, label=f"{particle_size*1e9} nm")
ax.set_yscale('log')
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Intensity")
ax.set_title("Rayleigh-Gans Scattering for theta = 180")
ax.legend(title="Particle size")

plt.show()



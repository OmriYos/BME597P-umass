import numpy as np
import matplotlib.pyplot as plt
import math

########### Define variables ########### 

Pcw = 1.5 # power in mW
n = 1.37 # refractive index
Cn = 3E8 / n # Speed of light in medium
A = 3.2 # given
g = 0.89
mu_a = 0.02  # 1/mm
mu_s = 9
mu_s_prime = mu_s * (1 - g)  # units: 1/mm
mu_t_prime = mu_a + mu_s_prime
Phi_0 = (Cn * Pcw) / (4 * math.pi * (Cn / 3 * (mu_a + mu_s_prime))) # coefficient 
a_prime = mu_s_prime/mu_t_prime 
mu_eff = np.sqrt(3 * mu_a * (mu_a + mu_s_prime))

############ Define r ranges ############

r_min = 1.0 # in mm
r_max = 30.0  
dr = 0.1  
r_array = np.arange(r_min, r_max + dr, dr)  # for deep
r1_array = np.sqrt( (1/mu_s_prime)**2 + r_array**2 ) # for surface
r2_array = np.sqrt( (2*(2*A/(3*mu_t_prime))  + (1/mu_s_prime))**2 + r_array**2) # for surface

########### Calculate fluence rate for all r ###############

Phi_r = Phi_0 * np.exp(-mu_eff * r_array)/r_array  # calculate the fluence rate at each distance
Phi_r_surface = Phi_0*a_prime * ( np.exp(-mu_eff*r1_array)/r1_array - np.exp(-mu_eff*r2_array)/r2_array )

########### plot fluence rate vs. distance ################
fig, ax = plt.subplots()
ax.semilogy(r_array, Phi_r, label='Deep Brain')
ax.semilogy(r_array, Phi_r_surface, label='Surface Brain')
ax.set_xlabel('Distance from fiber tip (mm)')
ax.set_ylabel('Fluence rate (W/m^2)')
ax.set_title('Fluence rate vs. distance from fiber tip')
ax.legend()
plt.show()
#testing

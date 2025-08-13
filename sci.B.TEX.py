# population_dynamics_sets.py

import matplotlib.pyplot as plt
import numpy as np
import os

# Create output folder
os.makedirs('figures', exist_ok=True)

# Time array
t = np.linspace(0, 30, 300)

# Example population dynamics functions
def susceptible_prey(t, omega):
    return 2 * np.sin(omega * t) + 1

def infected_prey(t, f):
    return np.sin(f * t)

def predator(t, g):
    return 0.5 * np.cos(g * t) + 0.5

# Parameter sets
params = [
    {'omega': 0.25, 'f': 0.10, 'g': 0.20},
    {'omega': 0.50, 'f': 0.50, 'g': 0.60},
    {'omega': 0.85, 'f': 0.95, 'g': 0.90}
]

# Create subplots
fig, axs = plt.subplots(3, 1, figsize=(12, 10))

for i, param in enumerate(params):
    omega = param['omega']
    f = param['f']
    g = param['g']
    
    Y_s = susceptible_prey(t, omega)
    Y_i = infected_prey(t, f)
    Z = predator(t, g)
    
    axs[i].plot(t, Y_s, label='Susceptible Prey $Y_s(t)$', color='green')
    axs[i].plot(t, Y_i, label='Infected Prey $Y_i(t)$', color='red')
    axs[i].plot(t, Z, label='Predator $Z(t)$', color='orange', linestyle='--')
    
    axs[i].set_title(f'Population Dynamics - Set {i+1}: $\\Omega={omega}$, $f={f}$, $g={g}$')
    axs[i].set_xlabel('Time')
    axs[i].set_ylabel('Population')
    axs[i].legend()
    axs[i].grid(True)

plt.tight_layout()
plt.savefig('figures/population_dynamics_sets.png', dpi=300)
plt.show()

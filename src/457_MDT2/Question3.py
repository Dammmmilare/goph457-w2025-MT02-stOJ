import numpy as np
import matplotlib.pyplot as plt

# Given data
d = 45.2 / 1000  # Diameter in meters
h = 143.8 / 1000  # Height in meters

data = np.array([
    [0.00000, 0.00000, 0.0],
    [0.00233, -0.00011, 1965.7],
    [0.00484, -0.00023, 3877.8],
    [0.00755, -0.00035, 5544.7],
    [0.01182, -0.00051, 7771.6],
    [0.01784, -0.00073, 10657.9],
    [0.01362, -0.00055, 7723.5],
    [0.01098, -0.00043, 5808.5],
    [0.00770, -0.00031, 3906.7],
    [0.00380, -0.00015, 1973.3],
    [0.00000, 0.00000, 0.0]
])

# Convert displacement to meters
dh = data[:, 0] / 1000  # Axial displacement (m)
dr = data[:, 1] / 1000  # Radial displacement (m)
f = data[:, 2]  # Force (N)

# Geometry and stress/strain calculations
r = d / 2
a = np.pi * r**2  # Cross-sectional area

epsilon_a = dh / h  # Axial strain
epsilon_r = dr / r  # Radial strain
sigma_a = f / a     # Axial stress

# Plotting
plt.figure(figsize=(12, 5))

# Axial Stress vs. Axial Strain
plt.subplot(1, 2, 1)
plt.plot(epsilon_a[:6], sigma_a[:6], 'b-', marker='o', label='Loading')
plt.plot(epsilon_a[5:], sigma_a[5:], 'r-', marker='o', label='Unloading')
plt.xlabel("Axial Strain")
plt.ylabel("Axial Stress (Pa)")
plt.title("Axial Stress vs. Axial Strain")
plt.grid(True)
plt.legend()

# Radial Strain vs. Axial Strain
plt.subplot(1, 2, 2)
plt.plot(epsilon_a[:6], epsilon_r[:6], 'b-', marker='o', label='Loading')
plt.plot(epsilon_a[5:], epsilon_r[5:], 'r-', marker='o', label='Unloading')
plt.xlabel("Axial Strain")
plt.ylabel("Radial Strain")
plt.title("Radial Strain vs. Axial Strain")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# Output results
for i in range(len(epsilon_a)):
    print(f"dH={dh[i]:.6f}, dR={dr[i]:.6f}, F={f[i]:.2f}, εa={epsilon_a[i]:.6f}, εr={epsilon_r[i]:.6f}, σa={sigma_a[i]:.2f}")

# Estimate Young's Modulus (E)
e_slope, e_intercept = np.polyfit(epsilon_a[:5], sigma_a[:5], 1)
youngs_modulus = e_slope

# Estimate Poisson's Ratio (v)
v_slope, v_intercept = np.polyfit(epsilon_a[:5], epsilon_r[:5], 1)
poissons_ratio = -v_slope

print(f"\nEstimated Young's Modulus: {youngs_modulus / 1e9:.2f} GPa")
print(f"Estimated Poisson's Ratio: {poissons_ratio:.2f}")

# Plausibility check
youngs_modulus_range = (10, 80)  # GPa
poissons_ratio_range = (0.1, 0.3)

print("\nPlausibility Check:")
if youngs_modulus_range[0] <= youngs_modulus / 1e9 <= youngs_modulus_range[1]:
    print("Young's Modulus is plausible for granite.")
else:
    print("Young's Modulus is NOT plausible for granite.")

if poissons_ratio_range[0] <= poissons_ratio <= poissons_ratio_range[1]:
    print("Poisson's Ratio is plausible for granite.")
else:
    print("Poisson's Ratio is NOT plausible for granite.")

# Elastic parameters
bulk_modulus = youngs_modulus / (3 * (1 - 2 * poissons_ratio))
shear_modulus = youngs_modulus / (2 * (1 + poissons_ratio))
lame_parameter = (youngs_modulus * poissons_ratio) / ((1 + poissons_ratio) * (1 - 2 * poissons_ratio))
p_wave_modulus = lame_parameter + 2 * shear_modulus

print(f"\nEstimated Bulk Modulus (K): {bulk_modulus / 1e9:.2f} GPa")
print(f"Estimated Shear Modulus (G): {shear_modulus / 1e9:.2f} GPa")
print(f"Estimated Lamé Parameter (λ): {lame_parameter / 1e9:.2f} GPa")
print(f"Estimated P-wave Modulus (M): {p_wave_modulus / 1e9:.2f} GPa")

# Density
mass = 0.66263  # kg
volume = np.pi * (d / 2)**2 * h
density = mass / volume

# Wave velocities
p_wave_velocity = np.sqrt(p_wave_modulus / density)
s_wave_velocity = np.sqrt(shear_modulus / density)

print(f"\nEstimated Density: {density:.2f} kg/m^3")
print(f"Estimated P-wave Velocity (vp): {p_wave_velocity / 1000:.2f} km/s")
print(f"Estimated S-wave Velocity (vs): {s_wave_velocity / 1000:.2f} km/s")

# vs/vp ratios
vs_vp_ratio_velocities = s_wave_velocity / p_wave_velocity
vs_vp_ratio_poissons = np.sqrt((1 - 2 * poissons_ratio) / (2 - 2 * poissons_ratio))

print(f"vs/vp ratio (from velocities): {vs_vp_ratio_velocities:.2f}")
print(f"vs/vp ratio (from Poisson's ratio): {vs_vp_ratio_poissons:.2f}")

# Final plausibility check
vp_range = (4.5, 5.5)  # km/s
vs_range = (2.5, 3.0)  # km/s
vs_vp_range = (0.57, 0.65)

print("\nPlausibility Check (Velocities):")
if vp_range[0] <= p_wave_velocity / 1000 <= vp_range[1]:
    print("P-wave velocity is plausible for granite.")
else:
    print("P-wave velocity is NOT plausible for granite.")

if vs_range[0] <= s_wave_velocity / 1000 <= vs_range[1]:
    print("S-wave velocity is plausible for granite.")
else:
    print("S-wave velocity is NOT plausible for granite.")

print("\nPlausibility Check (vs/vp ratio):")
if vs_vp_range[0] <= vs_vp_ratio_velocities <= vs_vp_range[1] and vs_vp_range[0] <= vs_vp_ratio_poissons <= vs_vp_range[1]:
    print("vs/vp ratio is plausible for granite.")
else:
    print("vs/vp ratio is NOT plausible for granite.")

# Set Poisson's ratio to 0.5 for an incompressible material
poissons_ratio_incompressible = 0.5

# Calculate the Bulk Modulus (K), Shear Modulus (G), and P-wave Modulus (M) using the incompressible Poisson's ratio
bulk_modulus_incompressible = youngs_modulus / (3 * (1 - 2 * poissons_ratio_incompressible))
shear_modulus_incompressible = youngs_modulus / (2 * (1 + poissons_ratio_incompressible))
lame_parameter_incompressible = (youngs_modulus * poissons_ratio_incompressible) / \
                                ((1 + poissons_ratio_incompressible) * (1 - 2 * poissons_ratio_incompressible))
p_wave_modulus_incompressible = lame_parameter_incompressible + 2 * shear_modulus_incompressible

# For incompressible material, P-wave velocity (v_p) tends to infinity, and S-wave velocity (v_s) becomes zero
p_wave_velocity_incompressible = np.inf  # As K -> infinity
s_wave_velocity_incompressible = 0.0  # As G -> 0

# Output the results for the incompressible case
print(f"\nIncompressible Material (Poisson's Ratio = 0.5):")
print(f"Bulk Modulus (K) (theoretically infinite): {bulk_modulus_incompressible / 1e9:.2f} GPa")
print(f"Shear Modulus (G) (zero for incompressible material): {shear_modulus_incompressible / 1e9:.2f} GPa")
print(f"P-wave Modulus (M): {p_wave_modulus_incompressible / 1e9:.2f} GPa")
print(f"P-wave Velocity (v_p): Infinite")
print(f"S-wave Velocity (v_s): 0 km/s")
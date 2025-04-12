import numpy as np
import matplotlib.pyplot as plt

print("Question 2 - Electrical Properties\n")

# Given data
s = np.array([1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0])  # Electrode spacing [m]
delta_v = np.array([481, 237, 139, 88, 59, 40, 27, 20, 15, 12, 9, 8, 6]) / 1000  # ΔV [V] converted from mV
a = 0.5     # Electrode spacing for inner potential electrodes [m]
i_0 = 0.005 # Current input [A]

# Part a: Geometric factor
print("Part a: Geometric Factor Derivation\n")
print("   The geometric factor (G) for the Schlumberger array is derived as follows:")
print("   ΔV = I0 * ρa * G  → G = a / (π * s * (s + a))\n")
print("   The full answer to part a can be found in the pdf document where the diagrams are contained.\n")

#part b: Ratio for Jx calculation
print("Part b: Ratio for Jx calculation\n")
print("   The full answer to part b can be found in the pdf document where the diagrams are contained.\n")

# Part c: VESR Electrical resistivity method
print("   Part c: VESR Electrical Resistivity Method\n")
print("   Water depth = 4 meters\n")
print("   Explaining the method applied and how/ why it works?\n")
print("   For this data collection method we applied the vertical electrical resistivity sounding by the schlumberger array method.\n")
print("   This method is a geophysical technique that is used to investigate subsurface electrical resistivity variations with depth and used for mineral exploration and subsurface or groundwater exploration.\n")
print("   It works by connecting two and injecting current into the ground and measuring the potential difference between the other two electrodes and systematically increasing the spacing between the current electrodes while keeping the potential electrodes fixed, thereby measuring the subsurface resistivity by varying depths.\n")
print("   The full answer to part c can be found in the excel document where the tables and diagrams are contained.\n")
print("   Sorry for the inconvenience\n")
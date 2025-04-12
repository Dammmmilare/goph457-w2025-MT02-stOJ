import numpy as np

# Question 1 - Flow Nets for Potential Fields
print("Question 1 - Flow Nets for Potential Fields\n")

# Part a: Description of flux, potential variable, and material parameter
print("Part a: Description and definition (SI units) of flux variable f, potential variable φ, and material parameter α:\n")

print("i. Steady state groundwater flow")
print("   - Flux variable (f): Darcy flux (specific discharge)")
print("     SI units: m/s (meters per second)")
print("   - Potential variable (φ): Hydraulic head")
print("     SI units: m (meters)")
print("   - Material parameter (α): Hydraulic conductivity")
print("     SI units: m/s (meters per second)\n")

print("ii. Steady state electrical conduction")
print("   - Flux variable (f): Current density")
print("     SI units: A/m^2 (amperes per square meter)")
print("   - Potential variable (φ): Electric potential (voltage)")
print("     SI units: V (volts)")
print("   - Material parameter (α): Electrical conductivity")
print("     SI units: S/m (siemens per meter)\n")

# Part b: Isotropy, homogeneity, and changes to equations
print("Part b: Concepts of isotropy and homogeneity; how equations change:\n")

print("   - Isotropy: Material properties are the same in all directions.")
print("   - Homogeneity: Material properties are the same at all points.\n")

alpha_isotropic = 5  # Example scalar value
alpha_anisotropic = np.array([[5, 1], [1, 3]])  # Example tensor

print("   Isotropic conductivity (scalar α):", alpha_isotropic)
print("   Anisotropic conductivity (tensor α):\n", alpha_anisotropic)
print("\n   Changes to equations:")
print("   - Anisotropic: f = -α ⋅ ∇φ,   ∇ ⋅ (α ⋅ ∇φ) + s = 0   (α is a tensor)")
print("   - Heterogeneous: ∇ ⋅ (α(x, y, z) ⋅ ∇φ) + s = 0   (α varies with position), Laplace equation no longer applies\n")

# Part c: Flow net construction assumptions and rules
print("Part c: Assumptions and rules for constructing flow nets:\n")

# i. Definition of equipotentials and flow lines
print("i. Equipotentials are lines of constant potential φ (e.g., hydraulic head or electric potential).")
print("   Flow lines represent the direction of flux f (e.g., Darcy flux or current density).")

# ii. Relationship between equipotentials and flow lines
print("ii. Equipotentials and flow lines are orthogonal (perpendicular) to each other in isotropic media.")

# iii. Common boundary conditions
print("iii. Common boundary conditions:")
print("   - Constant head (Dirichlet): equipotentials follow the boundary.")
print("   - No-flow (Neumann): flow lines are parallel to the boundary.")

# iv. Curvilinear squares
print("iv. In isotropic materials, flow nets should form 'curvilinear squares' between equipotentials and flow lines.\n")

# Part d: Conceptual flow net descriptions for three conductivity cases
print("Part d: Cross-borehole tomography - Flow net sketches (conceptual description):\n")

print("Case I: α1 = α2")
print(" - Uniform conductivity across all layers.")
print(" - Flow lines and equipotentials are symmetric and evenly spaced.")
print(" - Flux is distributed uniformly between source and sink.\n")

print("Case II: α1 = 0.1 * α2 (target layer is more conductive)")
print(" - Most of the flux is concentrated in the central high conductivity layer (α2).")
print(" - Equipotentials are closely spaced in α2 due to the high gradient.")
print(" - Flow lines bend toward α2, flattening vertically after scaling.\n")

print("Case III: α1 = 10 * α2 (target layer is less conductive)")
print(" - Low conductivity layer (α2) resists flow.")
print(" - Flow lines curve around α2 into adjacent layers (α1).")
print(" - Equipotentials are sparse in α2; flux is diverted away.\n")

print("Note: These are qualitative representations—actual sketches must be drawn by hand or visualized using software.\n")

# Part e: Comparing tomography estimates for Cases II and III
print("Part e: Which case provides better estimates for α2?\n")

flux_case_ii = 0.8  # Approx. 80% of flux goes through α2
flux_case_iii = 0.2  # Approx. 20% of flux goes through α2

print("   Flux through target layer (Case II):", flux_case_ii)
print("   Flux through target layer (Case III):", flux_case_iii)

if flux_case_iii < flux_case_ii:
    print("   → Case III estimate is more affected by adjacent layers.")
    print("   → Therefore, Case II provides a more accurate estimate of α2 since more flux passes through it.\n")

print("--------------------------------------------------\n")

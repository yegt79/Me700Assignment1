# Base class for Elasto-Plastic Material Model
class ElastoPlasticMaterial:
    def __init__(self, E, nu, sigma_yield):
        self.E = E  # Elastic modulus
        self.nu = nu  # Poisson's ratio
        self.sigma_yield = sigma_yield  # Yield stress
        self.plastic_strain = 0.0  # Plastic strain (initial value)
        self.stress = 0.0  # Stress (initial value)

    def compute_stress(self, strain):
        raise NotImplementedError("This method should be implemented in subclasses.")

# Kinematic Hardening Model
class KinematicHardeningElastoPlastic(ElastoPlasticMaterial):
    def __init__(self, E, nu, sigma_yield, C, alpha_init=0.0):
        super().__init__(E, nu, sigma_yield)
        self.C = C  # Hardening modulus
        self.alpha = alpha_init  # Initial backstress

    def compute_stress(self, strain):
        elastic_stress = self.E * strain
        if elastic_stress > self.sigma_yield + self.alpha:
            plastic_strain_increment = (elastic_stress - self.sigma_yield - self.alpha) / self.E
            self.alpha += self.C * plastic_strain_increment
            self.plastic_strain += plastic_strain_increment
            return self.sigma_yield + self.alpha
        else:
            return elastic_stress

# Isotropic Hardening Model
class IsotropicHardeningElastoPlastic(ElastoPlasticMaterial):
    def __init__(self, E, nu, sigma_yield, H, sigma_eq_init=0.0):
        super().__init__(E, nu, sigma_yield)
        self.H = H  # Hardening modulus
        self.sigma_eq = sigma_eq_init  # Initial equivalent stress

    def compute_stress(self, strain):
        elastic_stress = self.E * strain
        if elastic_stress > self.sigma_yield + self.sigma_eq:
            plastic_strain_increment = (elastic_stress - self.sigma_yield - self.sigma_eq) / self.E
            self.sigma_eq += self.H * plastic_strain_increment
            self.plastic_strain += plastic_strain_increment
            return self.sigma_yield + self.sigma_eq
        else:
            return elastic_stress

# Example 1: Simple Elastic Material Behavior
def example_1():
    material = KinematicHardeningElastoPlastic(210e9, 0.3, 250e6, 0)  # No hardening (C=0)
    strain = 0.01
    stress = material.compute_stress(strain)
    print(f"Example 1 - Stress (Elastic Behavior): {stress:.2f} Pa")

# Example 2: Material with Kinematic Hardening Under Strain
def example_2():
    material = KinematicHardeningElastoPlastic(210e9, 0.3, 250e6, 200e6)
    strain = 0.02
    stress = material.compute_stress(strain)
    print(f"Example 2 - Stress with Kinematic Hardening: {stress:.2f} Pa")

# Example 3: Isotropic Hardening Behavior
def example_3():
    material = IsotropicHardeningElastoPlastic(210e9, 0.3, 250e6, 100e6)
    strain = 0.015
    stress = material.compute_stress(strain)
    print(f"Example 3 - Stress with Isotropic Hardening: {stress:.2f} Pa")

# Example 4: Comparing Kinematic and Isotropic Hardening
def example_4():
    kinematic_material = KinematicHardeningElastoPlastic(210e9, 0.3, 250e6, 200e6)
    isotropic_material = IsotropicHardeningElastoPlastic(210e9, 0.3, 250e6, 100e6)

    strain = 0.015
    kinematic_stress = kinematic_material.compute_stress(strain)
    isotropic_stress = isotropic_material.compute_stress(strain)

    print(f"Example 4 - Stress with Kinematic Hardening: {kinematic_stress:.2f} Pa")
    print(f"Example 4 - Stress with Isotropic Hardening: {isotropic_stress:.2f} Pa")

# Example 5: Simulating a Larger Strain
def example_5():
    material = KinematicHardeningElastoPlastic(210e9, 0.3, 250e6, 300e6)
    strain = 0.05
    stress = material.compute_stress(strain)
    print(f"Example 5 - Stress with Large Strain (Kinematic Hardening): {stress:.2f} Pa")

# Running all the examples
def run_all_examples():
    example_1()
    example_2()
    example_3()
    example_4()
    example_5()

# Run the examples
run_all_examples()

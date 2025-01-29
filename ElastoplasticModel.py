# Base class for Elasto-Plastic Material Model
class ElastoPlasticMaterial:
    def __init__(self, E, nu, sigma_yield):
        """
        Initialize the material model with the elastic modulus, Poisson's ratio, and yield stress.
        :param E: Elastic modulus
        :param nu: Poisson's ratio
        :param sigma_yield: Initial yield stress
        """
        self.E = E  # Elastic modulus
        self.nu = nu  # Poisson's ratio
        self.sigma_yield = sigma_yield  # Yield stress
        self.plastic_strain = 0.0  # Plastic strain (initial value)
        self.stress = 0.0  # Stress (initial value)

    def compute_stress(self, strain):
        """
        Compute stress based on the current strain using the elastic-plastic model.
        :param strain: Input strain
        :return: Computed stress
        """
        raise NotImplementedError("This method should be implemented in subclasses.")

# Elasto-Plastic Model with Kinematic Hardening
class KinematicHardeningElastoPlastic(ElastoPlasticMaterial):
    def __init__(self, E, nu, sigma_yield, C, alpha_init=0.0):
        """
        Initialize the material model with kinematic hardening.
        :param E: Elastic modulus
        :param nu: Poisson's ratio
        :param sigma_yield: Initial yield stress
        :param C: Hardening modulus (kinematic)
        :param alpha_init: Initial backstress (default 0.0)
        """
        super().__init__(E, nu, sigma_yield)
        self.C = C  # Hardening modulus
        self.alpha = alpha_init  # Initial backstress

    def compute_stress(self, strain):
        """
        Compute stress with kinematic hardening behavior.
        :param strain: Input strain
        :return: Computed stress
        """
        # Elastic step: Stress is linear until yield
        elastic_stress = self.E * strain
        # Plastic step (yielding condition and plastic strain update)
        if elastic_stress > self.sigma_yield + self.alpha:
            # Calculate plastic strain increment
            plastic_strain_increment = (elastic_stress - self.sigma_yield - self.alpha) / self.E
            # Update the backstress (kinematic hardening)
            self.alpha += self.C * plastic_strain_increment
            # Update the plastic strain
            self.plastic_strain += plastic_strain_increment
            return self.sigma_yield + self.alpha
        else:
            return elastic_stress

# Elasto-Plastic Model with Isotropic Hardening
class IsotropicHardeningElastoPlastic(ElastoPlasticMaterial):
    def __init__(self, E, nu, sigma_yield, H, sigma_eq_init=0.0):
        """
        Initialize the material model with isotropic hardening.
        :param E: Elastic modulus
        :param nu: Poisson's ratio
        :param sigma_yield: Initial yield stress
        :param H: Hardening modulus (isotropic)
        :param sigma_eq_init: Initial equivalent stress (default 0.0)
        """
        super().__init__(E, nu, sigma_yield)
        self.H = H  # Hardening modulus
        self.sigma_eq = sigma_eq_init  # Initial equivalent stress

    def compute_stress(self, strain):
        """
        Compute stress with isotropic hardening behavior.
        :param strain: Input strain
        :return: Computed stress
        """
        # Elastic step: Stress is linear until yield
        elastic_stress = self.E * strain
        # Plastic step (yielding condition and plastic strain update)
        if elastic_stress > self.sigma_yield + self.sigma_eq:
            # Calculate plastic strain increment
            plastic_strain_increment = (elastic_stress - self.sigma_yield - self.sigma_eq) / self.E
            # Update the equivalent stress (isotropic hardening)
            self.sigma_eq += self.H * plastic_strain_increment
            # Update the plastic strain
            self.plastic_strain += plastic_strain_increment
            return self.sigma_yield + self.sigma_eq
        else:
            return elastic_stress

# Unit tests for Kinematic Hardening Model
def test_kinematic_hardening():
    material = KinematicHardeningElastoPlastic(210e9, 0.3, 250e6, 200e6)
    strain = 0.01
    stress = material.compute_stress(strain)
    expected_stress = 2.5e8  # Example expected value
    if abs(stress - expected_stress) >= 1e8:
        print(f"Test Failed: Expected {expected_stress}, but got {stress} for strain {strain}")
        raise AssertionError("Kinematic Hardening Test Failed")

# Unit tests for Isotropic Hardening Model
def test_isotropic_hardening():
    material = IsotropicHardeningElastoPlastic(210e9, 0.3, 250e6, 200e6)
    strain = 0.01
    stress = material.compute_stress(strain)
    expected_stress = 2.5e8  # Example expected value
    if abs(stress - expected_stress) >= 1e8:
        print(f"Test Failed: Expected {expected_stress}, but got {stress} for strain {strain}")
        raise AssertionError("Isotropic Hardening Test Failed")

# Running the tests
test_kinematic_hardening()
test_isotropic_hardening()
print("All tests passed!")

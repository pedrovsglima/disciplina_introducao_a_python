import math

class Sphere:
    def __init__(self, r=0, m=0):
        self.raio = r
        self.massa = m

    def get_radius(self):
        return self.raio

    def get_mass(self):
        return self.massa

    def get_volume(self):
        self.volume = (4*math.pi*(self.raio**3))/3
        return round(self.volume, 5)

    def get_surface_area(self):
        return round((4*math.pi*(self.raio**2)), 5)

    def get_density(self):
        return round(self.massa/self.volume, 5)

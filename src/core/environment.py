class Environment:
    def __init__(self):
        self.particles = set()
        self.forces = set()

    def add_forces(self, f, *forces):
        self.forces = self.forces | {f} | forces

    def add_particles(self, p, *particles):
        self.particles = self.particles | {p} | particles

    def display_particles(self):
        map(lambda p: p.display(), self.particles)

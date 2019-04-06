from src.constants import physic_constants
from src.core.forces.force import ForceInterface


class GravitationForce(ForceInterface):
    def calc(self, **kwargs):
        return kwargs['m'] * physic_constants.G

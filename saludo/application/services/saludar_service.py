from saludo.domain.persona import Persona
from saludo.application.ports.saludar_use_case import SaludarUseCase


class SaludarService(SaludarUseCase):
    def saludar(self, nombre):
        persona = Persona(nombre)
        return f"hola {persona.nombre}"
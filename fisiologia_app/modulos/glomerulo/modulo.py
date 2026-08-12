# modulos/glomerulo/modulo.py
from telas.tela_modulo_base import TelaModuloBase
from .simulador import SimuladorGlomerulo
from .exercicios import ExerciciosGlomerulo
from .material_teorico import MaterialTeoricoGlomerulo


class ModuloGlomerulo(TelaModuloBase):
    """Módulo: Determinantes da Filtração Glomerular."""

    def __init__(self):
        super().__init__(nome_modulo="Filtração Glomerular")

        self.adicionar_pagina("simulador", "🧪  Simulador", SimuladorGlomerulo())
        self.adicionar_pagina("exercicios", "📝  Exercícios", ExerciciosGlomerulo())
        self.adicionar_pagina("teoria", "📘  Material teórico", MaterialTeoricoGlomerulo())

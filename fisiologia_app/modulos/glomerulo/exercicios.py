# modulos/glomerulo/exercicios.py
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QFrame
)
from .grafico import Grafico


class ExerciciosGlomerulo(QWidget):
    """Exercício prático: o aluno insere pares (Qa, FPN) calculados por ele
    mesmo e visualiza a relação entre as duas variáveis em um gráfico."""

    def __init__(self):
        super().__init__()

        self.dados_Qa = []
        self.dados_FPN = []

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(16)

        titulo = QLabel("Exercício — Relação FPN x Qa")
        titulo.setObjectName("tituloTela")
        subtitulo = QLabel(
            "Calcule a FPN para diferentes valores de Qa (mantendo os demais parâmetros "
            "fixos) e adicione os pontos abaixo para visualizar a relação entre as duas "
            "variáveis."
        )
        subtitulo.setWordWrap(True)
        subtitulo.setStyleSheet("color:#6B7280;")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        card_grafico = QFrame()
        card_grafico.setObjectName("cardModulo")
        layout_grafico = QVBoxLayout(card_grafico)
        layout_grafico.setContentsMargins(16, 16, 16, 16)
        self.grafico = Grafico()
        self.grafico.setMinimumHeight(320)
        layout_grafico.addWidget(self.grafico)

        layout.addWidget(card_grafico, stretch=1)

        entradas = QHBoxLayout()
        self.input_Qa = QLineEdit()
        self.input_Qa.setPlaceholderText("Qa (nL/min)")
        self.input_FPN = QLineEdit()
        self.input_FPN.setPlaceholderText("FPN calculado")

        botao_adicionar = QPushButton("Adicionar ponto")
        botao_adicionar.clicked.connect(self.adicionar_ponto)

        entradas.addWidget(QLabel("Qa:"))
        entradas.addWidget(self.input_Qa)
        entradas.addWidget(QLabel("FPN:"))
        entradas.addWidget(self.input_FPN)
        entradas.addWidget(botao_adicionar)

        layout.addLayout(entradas)

    def adicionar_ponto(self):
        try:
            qa = float(self.input_Qa.text())
            fpn = float(self.input_FPN.text())
        except ValueError:
            return

        self.dados_Qa.append(qa)
        self.dados_FPN.append(fpn)
        self.grafico.plotar(self.dados_Qa, self.dados_FPN)

        self.input_Qa.clear()
        self.input_FPN.clear()

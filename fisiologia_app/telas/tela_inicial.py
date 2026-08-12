# telas/tela_inicial.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QFrame, QGraphicsDropShadowEffect
)
from PySide6.QtGui import QColor


class TelaInicial(QWidget):
    """Tela de abertura do app: um card central com o nome do app
    e três ações -> Módulos, Sobre, Sair."""

    ir_para_modulos = Signal()
    ir_para_sobre = Signal()
    sair = Signal()

    def __init__(self):
        super().__init__()

        layout_externo = QVBoxLayout(self)
        layout_externo.setAlignment(Qt.AlignCenter)

        card = QFrame()
        card.setObjectName("cardInicial")
        card.setFixedWidth(420)

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(40)
        sombra.setXOffset(0)
        sombra.setYOffset(12)
        sombra.setColor(QColor(31, 41, 55, 60))
        card.setGraphicsEffect(sombra)

        layout_card = QVBoxLayout(card)
        layout_card.setContentsMargins(40, 48, 40, 48)
        layout_card.setSpacing(10)

        titulo = QLabel("Fisiologia")
        titulo.setObjectName("tituloApp")
        titulo.setAlignment(Qt.AlignCenter)

        subtitulo = QLabel("Simuladores interativos para o estudo de fisiologia")
        subtitulo.setObjectName("subtituloApp")
        subtitulo.setAlignment(Qt.AlignCenter)
        subtitulo.setWordWrap(True)

        layout_card.addWidget(titulo)
        layout_card.addWidget(subtitulo)
        layout_card.addSpacing(24)

        botao_modulos = QPushButton("Módulos")
        botao_modulos.setMinimumHeight(46)
        botao_modulos.clicked.connect(self.ir_para_modulos.emit)

        botao_sobre = QPushButton("Sobre")
        botao_sobre.setObjectName("botaoSecundario")
        botao_sobre.setMinimumHeight(46)
        botao_sobre.clicked.connect(self.ir_para_sobre.emit)

        botao_sair = QPushButton("Sair")
        botao_sair.setObjectName("botaoPerigo")
        botao_sair.setMinimumHeight(46)
        botao_sair.clicked.connect(self.sair.emit)

        layout_card.addWidget(botao_modulos)
        layout_card.addWidget(botao_sobre)
        layout_card.addSpacing(14)
        layout_card.addWidget(botao_sair)

        layout_externo.addWidget(card)

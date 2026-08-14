# telas/tela_selecao_modulos.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame,
    QGridLayout, QGraphicsDropShadowEffect, QScrollArea
)
from PySide6.QtGui import QColor


class CardModulo(QFrame):
    """Card clicável que representa um módulo disponível."""

    clicado = Signal(str)

    def __init__(self, chave, titulo, descricao, disponivel=True):
        super().__init__()
        self.chave = chave
        self.setObjectName("cardModulo")
        self.setFixedSize(260, 160)
        self.setCursor(Qt.PointingHandCursor if disponivel else Qt.ForbiddenCursor)

        sombra = QGraphicsDropShadowEffect()
        sombra.setBlurRadius(24)
        sombra.setYOffset(6)
        sombra.setColor(QColor(31, 41, 55, 35))
        self.setGraphicsEffect(sombra)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(22, 20, 22, 20)
        layout.setSpacing(8)

        titulo_lbl = QLabel(titulo)
        titulo_lbl.setStyleSheet("font-size:16px; font-weight:700;")
        titulo_lbl.setWordWrap(True)

        desc_lbl = QLabel(descricao)
        desc_lbl.setWordWrap(True)
        desc_lbl.setStyleSheet("color:#6B7280; font-size:12.5px;")

        layout.addWidget(titulo_lbl)
        layout.addWidget(desc_lbl)
        layout.addStretch()

        if not disponivel:
            selo = QLabel("Em breve")
            selo.setStyleSheet(
                "color:#9CA3AF; font-size:11px; font-weight:600; "
                "background-color:#F3F4F6; border-radius:6px; padding:3px 8px;"
            )
            selo.setFixedWidth(70)
            layout.addWidget(selo)
            self.setEnabled(True)

        self.disponivel = disponivel

    def mousePressEvent(self, event):
        if self.disponivel:
            self.clicado.emit(self.chave)
        super().mousePressEvent(event)


class TelaSelecaoModulos(QWidget):
    """Grade com os módulos disponíveis no app."""

    voltar = Signal()
    modulo_escolhido = Signal(str)

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(48, 36, 48, 36)
        layout.setSpacing(20)

        topo = QHBoxLayout()
        botao_voltar = QPushButton("← Voltar")
        botao_voltar.setObjectName("botaoSecundario")
        botao_voltar.setFixedWidth(120)
        botao_voltar.clicked.connect(self.voltar.emit)
        topo.addWidget(botao_voltar)
        topo.addStretch()

        titulo = QLabel("Escolha um módulo")
        titulo.setObjectName("tituloTela")

        subtitulo = QLabel("Selecione o tema que deseja estudar")
        subtitulo.setStyleSheet("color:#6B7280;")

        area_rolagem = QScrollArea()
        area_rolagem.setWidgetResizable(True)
        conteudo = QWidget()
        self.grid = QGridLayout(conteudo)
        self.grid.setSpacing(20)
        area_rolagem.setWidget(conteudo)

        modulos = [
            ("glomerulo", "Determinantes da Filtração Glomerular",
             "Explore como fluxo plasmático, pressão hidrostática, Kf e proteínas "
             "plasmáticas afetam a FPN.", True),
            ("cardio", "Metabolismo da Água - Disturbio", "Em desenvolvimento.", False),
            ("respiratorio", "Metabolismo da Água - Sistema", "Em desenvolvimento.", False),
        ]

        for i, (chave, titulo_mod, desc, disponivel) in enumerate(modulos):
            card = CardModulo(chave, titulo_mod, desc, disponivel)
            card.clicado.connect(self.modulo_escolhido.emit)
            self.grid.addWidget(card, i // 3, i % 3, Qt.AlignLeft | Qt.AlignTop)

        self.grid.setRowStretch(len(modulos) // 3 + 1, 1)
        self.grid.setColumnStretch(3, 1)

        layout.addLayout(topo)
        layout.addWidget(titulo)
        layout.addWidget(subtitulo)
        layout.addWidget(area_rolagem)

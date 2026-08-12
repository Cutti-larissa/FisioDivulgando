# telas/tela_sobre.py
from PySide6.QtCore import Qt, Signal
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QFrame, QTextEdit


class TelaSobre(QWidget):
    """Tela explicativa sobre o projeto."""

    voltar = Signal()

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

        titulo = QLabel("Sobre o projeto")
        titulo.setObjectName("tituloTela")

        card = QFrame()
        card.setObjectName("cardModulo")
        layout_card = QVBoxLayout(card)
        layout_card.setContentsMargins(28, 24, 28, 24)

        texto = QTextEdit()
        texto.setReadOnly(True)
        texto.setFrameShape(QFrame.NoFrame)
        texto.setHtml(
            """
            <p style="font-size:14px; line-height:1.6;">
            O <b>Fisiologia</b> é um aplicativo de simuladores interativos criado para apoiar
            o ensino e o estudo de Fisiologia. A ideia é permitir que conceitos que costumam
            ser abstratos — como os determinantes da filtração glomerular, curvas de pressão
            e outros fenômenos fisiológicos — possam ser explorados de forma visual e
            experimental, ajustando parâmetros em tempo real e observando o efeito nas
            variáveis calculadas.
            </p>
            <p style="font-size:14px; line-height:1.6;">
            Cada assunto é organizado como um <b>módulo</b> independente, com seu próprio
            simulador, exercícios práticos e material teórico de apoio. Novos módulos podem
            ser adicionados conforme o conteúdo da disciplina avança.
            </p>
            <p style="font-size:14px; line-height:1.6;">
            Este projeto foi desenvolvido como uma ferramenta de apoio didático, unindo
            programação e fisiologia para tornar o aprendizado mais intuitivo.
            </p>
            """
        )

        layout_card.addWidget(texto)

        layout.addLayout(topo)
        layout.addWidget(titulo)
        layout.addWidget(card)

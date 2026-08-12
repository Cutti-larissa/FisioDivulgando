# modulos/glomerulo/material_teorico.py
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QFrame, QTextEdit


class MaterialTeoricoGlomerulo(QWidget):
    """Texto de apoio teórico sobre os determinantes da filtração glomerular."""

    def __init__(self):
        super().__init__()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(16)

        titulo = QLabel("Material Teórico")
        titulo.setObjectName("tituloTela")
        layout.addWidget(titulo)

        card = QFrame()
        card.setObjectName("cardModulo")
        layout_card = QVBoxLayout(card)
        layout_card.setContentsMargins(24, 20, 24, 20)

        texto = QTextEdit()
        texto.setReadOnly(True)
        texto.setFrameShape(QFrame.NoFrame)
        texto.setHtml(
            """
            <h3 style="color:#3730A3;">Filtração Glomerular</h3>
            <p style="line-height:1.6;">
            A taxa de filtração glomerular depende do equilíbrio entre as forças que
            favorecem a filtração e as que se opõem a ela, resumido na
            <b>Força de Filtração Efetiva</b> (PEUF) e na <b>Fração de Filtração
            Nefronal</b> (FPN).
            </p>

            <h4 style="color:#4361EE;">Fluxo Plasmático Renal (Qa)</h4>
            <p style="line-height:1.6;">
            Representa a quantidade de plasma que chega ao glomérulo por unidade de
            tempo. Aumentos em Qa tendem a elevar discretamente a FPN, pois mais plasma
            está disponível para ser filtrado.
            </p>

            <h4 style="color:#4361EE;">Pressão Hidrostática Líquida (ΔP)</h4>
            <p style="line-height:1.6;">
            É a diferença entre a pressão hidrostática capilar glomerular (que empurra
            líquido para fora do capilar) e a pressão hidrostática da cápsula de Bowman
            (que se opõe à filtração). Quanto maior o ΔP, maior a PEUF.
            </p>

            <h4 style="color:#4361EE;">Coeficiente de Filtração (Kf)</h4>
            <p style="line-height:1.6;">
            Reflete a permeabilidade e a área de superfície disponível para filtração na
            membrana glomerular. É diretamente proporcional à FPN.
            </p>

            <h4 style="color:#4361EE;">Pressão Oncótica (proteínas plasmáticas)</h4>
            <p style="line-height:1.6;">
            Gerada pelas proteínas plasmáticas, se opõe à filtração ao "puxar" líquido de
            volta para o capilar. Quanto maior a concentração de proteínas, maior a
            pressão oncótica e menor a PEUF resultante.
            </p>

            <h4 style="color:#4361EE;">Fórmulas utilizadas no simulador</h4>
            <p style="line-height:1.6;">
            PEUF = ΔP − π (pressão oncótica)<br>
            FPN = Kf × PEUF × (Qa / 125)<sup>0.3</sup>, quando PEUF &gt; 0
            </p>
            """
        )

        layout_card.addWidget(texto)
        layout.addWidget(card)

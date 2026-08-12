# modulos/glomerulo/simulador.py
from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSlider, QLineEdit,
    QPushButton, QFrame, QScrollArea, QGridLayout
)
from .modelo import Glomerulo


class GrupoParametro(QFrame):
    """Card com rótulo + slider + campo numérico para um parâmetro."""

    def __init__(self, titulo, unidade, minimo, maximo, valor_inicial):
        super().__init__()
        self.setObjectName("grupoParametro")

        layout = QVBoxLayout(self)
        layout.setContentsMargins(18, 14, 18, 14)
        layout.setSpacing(6)

        cabecalho = QHBoxLayout()
        self.label_titulo = QLabel(titulo)
        self.label_titulo.setStyleSheet("font-weight:600;")
        self.label_valor = QLabel()
        self.label_valor.setStyleSheet(f"color:#4361EE; font-weight:700;")
        cabecalho.addWidget(self.label_titulo)
        cabecalho.addStretch()
        cabecalho.addWidget(self.label_valor)

        linha_controle = QHBoxLayout()
        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(minimo)
        self.slider.setMaximum(maximo)
        self.slider.setValue(valor_inicial)

        self.input = QLineEdit()
        self.input.setFixedWidth(70)
        self.input.setAlignment(Qt.AlignCenter)

        linha_controle.addWidget(self.slider, stretch=1)
        linha_controle.addWidget(self.input)

        layout.addLayout(cabecalho)
        layout.addLayout(linha_controle)

        self.unidade = unidade
        self._atualizar_label_valor(valor_inicial)

    def _atualizar_label_valor(self, valor):
        self.label_valor.setText(f"{valor} {self.unidade}".strip())


class SimuladorGlomerulo(QWidget):
    """Conteúdo do simulador de determinantes da filtração glomerular,
    pronto para ser embutido dentro de uma página de módulo (sem janela
    própria, sem título de janela)."""

    def __init__(self):
        super().__init__()
        self.glom = Glomerulo()

        area_rolagem = QScrollArea()
        area_rolagem.setWidgetResizable(True)
        conteudo = QWidget()
        area_rolagem.setWidget(conteudo)

        layout_raiz = QVBoxLayout(self)
        layout_raiz.setContentsMargins(0, 0, 0, 0)
        layout_raiz.addWidget(area_rolagem)

        layout = QVBoxLayout(conteudo)
        layout.setContentsMargins(32, 28, 32, 28)
        layout.setSpacing(18)

        titulo = QLabel("Determinantes da Filtração Glomerular")
        titulo.setObjectName("tituloTela")
        subtitulo = QLabel(
            "Ajuste o fluxo plasmático renal (Qa), a pressão hidrostática líquida (ΔP), "
            "o coeficiente de filtração (Kf) e a concentração de proteínas plasmáticas "
            "para observar o efeito sobre a PEUF e a FPN."
        )
        subtitulo.setWordWrap(True)
        subtitulo.setStyleSheet("color:#6B7280;")

        layout.addWidget(titulo)
        layout.addWidget(subtitulo)

        # --- Parâmetros ---
        self.grupo_Qa = GrupoParametro("Fluxo Plasmático Renal (Qa)", "nL/min", 50, 500, 125)
        self.grupo_deltaP = GrupoParametro("Pressão Hidrostática Líquida (ΔP)", "mmHg", 10, 70, 40)
        self.grupo_Kf = GrupoParametro("Coeficiente de Filtração (Kf)", "", 1, 20, 8)
        self.grupo_proteina = GrupoParametro("Proteína Plasmática", "g/dL", 1, 10, 7)

        self.grupo_Qa.input.setText("125")
        self.grupo_deltaP.input.setText("40")
        self.grupo_Kf.input.setText("0.08")
        self.grupo_proteina.input.setText("7")

        self.grupo_Qa.slider.valueChanged.connect(self.atualizar)
        self.grupo_deltaP.slider.valueChanged.connect(self.atualizar)
        self.grupo_Kf.slider.valueChanged.connect(self.atualizar)
        self.grupo_proteina.slider.valueChanged.connect(self.atualizar)

        self.grupo_Qa.input.editingFinished.connect(self._input_Qa)
        self.grupo_deltaP.input.editingFinished.connect(self._input_deltaP)
        self.grupo_Kf.input.editingFinished.connect(self._input_Kf)
        self.grupo_proteina.input.editingFinished.connect(self._input_proteina)

        grade_parametros = QGridLayout()
        grade_parametros.setSpacing(14)
        grade_parametros.addWidget(self.grupo_Qa, 0, 0)
        grade_parametros.addWidget(self.grupo_deltaP, 0, 1)
        grade_parametros.addWidget(self.grupo_Kf, 1, 0)
        grade_parametros.addWidget(self.grupo_proteina, 1, 1)
        layout.addLayout(grade_parametros)

        # --- Resultado ---
        painel_resultado = QFrame()
        painel_resultado.setObjectName("painelResultado")
        layout_resultado = QVBoxLayout(painel_resultado)
        layout_resultado.setContentsMargins(24, 18, 24, 18)
        layout_resultado.setSpacing(4)

        label_resultado_titulo = QLabel("Resultado")
        label_resultado_titulo.setStyleSheet("font-weight:700; color:#3730A3;")

        self.label_peuf = QLabel()
        self.label_peuf.setStyleSheet("font-size:15px;")
        self.label_fpn = QLabel()
        self.label_fpn.setStyleSheet("font-size:20px; font-weight:700; color:#3730A3;")

        layout_resultado.addWidget(label_resultado_titulo)
        layout_resultado.addWidget(self.label_peuf)
        layout_resultado.addWidget(self.label_fpn)

        layout.addWidget(painel_resultado)

        botao_reset = QPushButton("Restaurar valores de referência")
        botao_reset.setObjectName("botaoSecundario")
        botao_reset.setMinimumWidth(280)
        botao_reset.setMaximumWidth(320)
        botao_reset.clicked.connect(self.resetar)
        layout.addWidget(botao_reset)

        layout.addStretch()

        self.atualizar()

    # -------- entradas manuais --------
    def _input_Qa(self):
        try:
            valor = int(self.grupo_Qa.input.text())
            if 50 <= valor <= 500:
                self.grupo_Qa.slider.setValue(valor)
        except ValueError:
            pass
        self.atualizar()

    def _input_deltaP(self):
        try:
            valor = int(self.grupo_deltaP.input.text())
            if 10 <= valor <= 70:
                self.grupo_deltaP.slider.setValue(valor)
        except ValueError:
            pass
        self.atualizar()

    def _input_Kf(self):
        try:
            valor = float(self.grupo_Kf.input.text())
            if 0.01 <= valor <= 0.2:
                self.grupo_Kf.slider.setValue(int(valor * 100))
        except ValueError:
            pass
        self.atualizar()

    def _input_proteina(self):
        try:
            valor = int(self.grupo_proteina.input.text())
            if 1 <= valor <= 10:
                self.grupo_proteina.slider.setValue(valor)
        except ValueError:
            pass
        self.atualizar()

    # -------- ações --------
    def resetar(self):
        self.glom.resetar()
        self.grupo_Qa.slider.setValue(125)
        self.grupo_deltaP.slider.setValue(40)
        self.grupo_Kf.slider.setValue(8)
        self.grupo_proteina.slider.setValue(7)
        self.atualizar()

    def atualizar(self):
        self.glom.Qa = self.grupo_Qa.slider.value()
        self.glom.deltaP = self.grupo_deltaP.slider.value()
        self.glom.Kf = self.grupo_Kf.slider.value() / 100
        self.glom.proteina = self.grupo_proteina.slider.value()

        fpn = self.glom.calcular_fpn()
        peuf = self.glom.calcular_peuf()

        self.grupo_Qa._atualizar_label_valor(self.glom.Qa)
        self.grupo_Qa.input.setText(str(self.glom.Qa))

        self.grupo_deltaP._atualizar_label_valor(self.glom.deltaP)
        self.grupo_deltaP.input.setText(str(self.glom.deltaP))

        self.grupo_Kf._atualizar_label_valor(f"{self.glom.Kf:.2f}")
        self.grupo_Kf.input.setText(f"{self.glom.Kf:.2f}")

        self.grupo_proteina._atualizar_label_valor(self.glom.proteina)
        self.grupo_proteina.input.setText(str(self.glom.proteina))

        self.label_peuf.setText(f"PEUF = {peuf:.2f} mmHg")
        self.label_fpn.setText(f"FPN = {fpn:.2f}")

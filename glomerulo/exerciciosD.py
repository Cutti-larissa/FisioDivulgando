from grafico import Grafico
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class TelaExercicios(QWidget):

    def __init__(self):

        super().__init__()


        self.setWindowTitle("Exercício - Relação FPN x Qa")

        self.dados_Qa = []
        self.dados_FPN = []

        self.grafico = Grafico()

        self.input_Qa = QLineEdit()
        self.input_FPN = QLineEdit()

        botao = QPushButton("Adicionar ponto")
        botao.clicked.connect(self.adicionar_ponto)

        painel = QVBoxLayout()
        painel.addWidget(self.grafico)

        entradas = QHBoxLayout()
        entradas.addWidget(QLabel("Qa:"))
        entradas.addWidget(self.input_Qa)
        entradas.addWidget(QLabel("FPN:"))
        entradas.addWidget(self.input_FPN)
        entradas.addWidget(botao)

        painel.addLayout(entradas)

        self.setLayout(painel)

    def adicionar_ponto(self):

        qa = float(self.input_Qa.text())
        fpn = float(self.input_FPN.text())

        self.dados_Qa.append(qa)
        self.dados_FPN.append(fpn)
        self.grafico.plotar(self.dados_Qa,self.dados_FPN)
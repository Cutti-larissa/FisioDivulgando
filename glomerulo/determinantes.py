import sys
from grafico import Grafico
from modelo import Glomerulo
from PySide6.QtCore import Qt
from exerciciosD import TelaExercicios
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QSlider, QVBoxLayout, QPushButton, QLineEdit

class Janela(QWidget):

    def __init__(self):
        super().__init__()
        self.glom = Glomerulo()
        self.setWindowTitle(
            "Determinantes da Filtração Glomerular"
        )
        self.resize(700,600)

        self.label_Qa = QLabel()
        self.input_Qa = QLineEdit()
        self.input_Qa.setText("125")
        self.slider_Qa = QSlider(Qt.Horizontal)
        self.slider_Qa.setMinimum(50)
        self.slider_Qa.setMaximum(500)
        self.slider_Qa.setValue(125)
        self.input_Qa.editingFinished.connect(self.atualizar_Qa_input)
        self.slider_Qa.valueChanged.connect(self.atualizar)

        self.label_deltaP = QLabel()
        self.input_deltaP = QLineEdit()
        self.input_deltaP.setText("40")
        self.slider_deltaP = QSlider(Qt.Horizontal)
        self.slider_deltaP.setMinimum(10)
        self.slider_deltaP.setMaximum(70)
        self.slider_deltaP.setValue(40)
        self.input_deltaP.editingFinished.connect(self.atualizar_deltaP_input)
        self.slider_deltaP.valueChanged.connect(self.atualizar)

        self.label_Kf = QLabel()
        self.input_Kf = QLineEdit()
        self.input_Kf.setText("0.08")
        self.slider_Kf = QSlider(Qt.Horizontal)
        self.slider_Kf.setMinimum(1)
        self.slider_Kf.setMaximum(20)
        self.slider_Kf.setValue(8)
        self.input_Kf.editingFinished.connect(self.atualizar_Kf_input)
        self.slider_Kf.valueChanged.connect(self.atualizar)

        self.label_proteina = QLabel()
        self.slider_proteina = QSlider(Qt.Horizontal)
        self.slider_proteina.setMinimum(1)
        self.slider_proteina.setMaximum(10)
        self.slider_proteina.setValue(7)
        self.slider_proteina.valueChanged.connect(self.atualizar)   

        self.botao_exercicios = QPushButton("Exercícios")
        self.botao_exercicios.clicked.connect(self.abrir_exercicios)        

        self.botao_reset = QPushButton("Valores de referência")
        self.botao_reset.clicked.connect(self.resetar)


        self.resultado = QLabel()

        layout = QVBoxLayout()

        layout.addWidget(self.label_Qa)
        layout.addWidget(self.slider_Qa)
        layout.addWidget(self.input_Qa)
        layout.addWidget(self.label_deltaP)
        layout.addWidget(self.slider_deltaP)
        layout.addWidget(self.input_deltaP)
        layout.addWidget(self.label_Kf)
        layout.addWidget(self.slider_Kf)
        layout.addWidget(self.input_Kf)
        layout.addWidget(self.resultado)
        layout.addWidget(self.botao_exercicios)
        layout.addWidget(self.botao_reset)

        self.setLayout(layout)
        self.atualizar()

    def abrir_exercicios(self):

        self.exercicios = TelaExercicios()
        self.exercicios.show()

    def atualizar_Qa_input(self):

        valor = int(self.input_Qa.text())
        
        if 50 <= valor <= 500:
            self.slider_Qa.setValue(valor)

        self.atualizar()

    def atualizar_deltaP_input(self):

        valor = int(self.input_deltaP.text())
        
        if 10 <= valor <= 70:
            self.slider_deltaP.setValue(valor)

        self.atualizar()

    def atualizar_Kf_input(self):

        valor = float(self.input_Kf.text())
        
        if 0.01 <= valor <= 0.2:
            self.slider_Kf.setValue(int(valor*100))

        self.atualizar()

    def resetar(self):

        self.glom.resetar()

        self.slider_Qa.setValue(125)
        self.slider_deltaP.setValue(40)
        self.slider_Kf.setValue(8)
        self.slider_proteina.setValue(7)

        self.atualizar()

    def atualizar(self):

        self.glom.Qa = self.slider_Qa.value()
        self.glom.deltaP = self.slider_deltaP.value()
        self.glom.Kf = self.slider_Kf.value()/100
        self.glom.proteina = self.slider_proteina.value()

        fpn = self.glom.calcular_fpn()
        peuf = self.glom.calcular_peuf()

        self.label_Qa.setText(f"Qa = {self.glom.Qa} nL/min")
        self.label_deltaP.setText(f"ΔP = {self.glom.deltaP} mmHg")
        self.label_Kf.setText(f"Kf = {self.glom.Kf}") # unidade de medida?
        self.label_proteina.setText(f"Proteína = {self.glom.proteina}")
        self.resultado.setText(
            f"""
            Peuf = {peuf:.2f} mmHg

            FPN = {fpn:.2f}
            """
        )

if __name__ == "__main__":
    app = QApplication(sys.argv)

    janela = Janela()
    janela.showMaximized()

    sys.exit(app.exec())
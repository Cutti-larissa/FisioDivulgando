import sys

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QSlider,
    QVBoxLayout
)

from PySide6.QtCore import Qt

from modelo import Glomerulo

class Janela(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Determinantes da Filtração Glomerular")
        self.resize(700,600)

        self.glom = Glomerulo()


        # ---------
        # Qa
        # ---------

        self.label_Qa = QLabel()

        self.slider_Qa = QSlider(Qt.Horizontal)

        self.slider_Qa.setMinimum(50)
        self.slider_Qa.setMaximum(500)
        self.slider_Qa.setValue(125)


        self.slider_Qa.valueChanged.connect(
            self.atualizar
        )


        # ---------
        # Delta P
        # ---------

        self.label_deltaP = QLabel()

        self.slider_deltaP = QSlider(Qt.Horizontal)

        self.slider_deltaP.setMinimum(10)
        self.slider_deltaP.setMaximum(70)
        self.slider_deltaP.setValue(40)


        self.slider_deltaP.valueChanged.connect(
            self.atualizar
        )


        # ---------
        # Resultados
        # ---------

        self.resultado = QLabel()


        layout = QVBoxLayout()


        layout.addWidget(
            self.label_Qa
        )

        layout.addWidget(
            self.slider_Qa
        )


        layout.addWidget(
            self.label_deltaP
        )

        layout.addWidget(
            self.slider_deltaP
        )


        layout.addWidget(
            self.resultado
        )


        self.setLayout(layout)


        self.atualizar()



    def atualizar(self):

        self.glom.Qa = self.slider_Qa.value()

        self.glom.deltaP = self.slider_deltaP.value()


        fpn = self.glom.calcular_fpn()

        peuf = self.glom.calcular_peuf()


        self.label_Qa.setText(
            f"Qa = {self.glom.Qa} nL/min"
        )


        self.label_deltaP.setText(
            f"ΔP = {self.glom.deltaP} mmHg"
        )


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
# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QStackedWidget

from estilos import QSS_GLOBAL
from telas.tela_inicial import TelaInicial
from telas.tela_sobre import TelaSobre
from telas.tela_selecao_modulos import TelaSelecaoModulos
from modulos.glomerulo.modulo import ModuloGlomerulo


class JanelaPrincipal(QMainWindow):
    """Janela única que hospeda todas as telas do app em um
    QStackedWidget, controlando a navegação entre elas."""

    def __init__(self):
        super().__init__()
        self.setWindowTitle("FisioSimulando")
        self.resize(1100, 720)

        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)

        # ---- Tela inicial ----
        self.tela_inicial = TelaInicial()
        self.tela_inicial.ir_para_modulos.connect(self.abrir_selecao_modulos)
        self.tela_inicial.ir_para_sobre.connect(self.abrir_sobre)
        self.tela_inicial.sair.connect(self.close)
        self.stack.addWidget(self.tela_inicial)

        # ---- Tela sobre ----
        self.tela_sobre = TelaSobre()
        self.tela_sobre.voltar.connect(self.abrir_inicio)
        self.stack.addWidget(self.tela_sobre)

        # ---- Seleção de módulos ----
        self.tela_selecao = TelaSelecaoModulos()
        self.tela_selecao.voltar.connect(self.abrir_inicio)
        self.tela_selecao.modulo_escolhido.connect(self.abrir_modulo)
        self.stack.addWidget(self.tela_selecao)

        # Módulos são criados sob demanda e cacheados aqui
        self._modulos_criados = {}

        self.abrir_inicio()

    def abrir_inicio(self):
        self.stack.setCurrentWidget(self.tela_inicial)

    def abrir_sobre(self):
        self.stack.setCurrentWidget(self.tela_sobre)

    def abrir_selecao_modulos(self):
        self.stack.setCurrentWidget(self.tela_selecao)

    def abrir_modulo(self, chave):
        if chave not in self._modulos_criados:
            widget_modulo = self._criar_modulo(chave)
            widget_modulo.trocar_modulo.connect(self.abrir_selecao_modulos)
            widget_modulo.ir_para_inicio.connect(self.abrir_inicio)
            self.stack.addWidget(widget_modulo)
            self._modulos_criados[chave] = widget_modulo

        self.stack.setCurrentWidget(self._modulos_criados[chave])

    def _criar_modulo(self, chave):
        if chave == "glomerulo":
            return ModuloGlomerulo()
        raise ValueError(f"Módulo desconhecido: {chave}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet(QSS_GLOBAL)

    janela = JanelaPrincipal()
    janela.showMaximized()

    sys.exit(app.exec())

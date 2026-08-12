# telas/tela_modulo_base.py
from PySide6.QtCore import Signal
from PySide6.QtWidgets import (
    QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QStackedWidget, QFrame
)


class TelaModuloBase(QWidget):
    """Estrutura comum a todas as telas de módulo: uma sidebar fixa à
    esquerda (nome do módulo + navegação) e uma área de conteúdo à
    direita que troca de página conforme o botão clicado.

    Cada módulo concreto (ex.: Glomérulo) só precisa registrar suas
    páginas com `adicionar_pagina` e pronto.
    """

    trocar_modulo = Signal()
    ir_para_inicio = Signal()

    def __init__(self, nome_modulo):
        super().__init__()

        layout_principal = QHBoxLayout(self)
        layout_principal.setContentsMargins(0, 0, 0, 0)
        layout_principal.setSpacing(0)

        # ---------------- Sidebar ----------------
        sidebar = QWidget()
        sidebar.setObjectName("sidebar")
        sidebar.setFixedWidth(230)

        layout_sidebar = QVBoxLayout(sidebar)
        layout_sidebar.setContentsMargins(18, 26, 18, 20)
        layout_sidebar.setSpacing(6)

        label_nome = QLabel(nome_modulo)
        label_nome.setObjectName("tituloModulo")
        label_nome.setWordWrap(True)

        label_sub = QLabel("MÓDULO")
        label_sub.setObjectName("subtituloModulo")

        layout_sidebar.addWidget(label_sub)
        layout_sidebar.addWidget(label_nome)
        layout_sidebar.addSpacing(24)

        self._botoes_nav = []
        self.layout_sidebar = layout_sidebar

        layout_sidebar.addStretch()

        linha = QFrame()
        linha.setFrameShape(QFrame.HLine)
        linha.setStyleSheet("color: #374151;")
        layout_sidebar.addWidget(linha)
        layout_sidebar.addSpacing(6)

        botao_trocar = QPushButton("⇄  Trocar módulo")
        botao_trocar.setObjectName("botaoSidebar")
        botao_trocar.clicked.connect(self.trocar_modulo.emit)

        botao_inicio = QPushButton("⌂  Início")
        botao_inicio.setObjectName("botaoSidebarSair")
        botao_inicio.clicked.connect(self.ir_para_inicio.emit)

        layout_sidebar.addWidget(botao_trocar)
        layout_sidebar.addWidget(botao_inicio)

        # ---------------- Área de conteúdo ----------------
        self.stack_conteudo = QStackedWidget()

        layout_principal.addWidget(sidebar)
        layout_principal.addWidget(self.stack_conteudo, stretch=1)

    def adicionar_pagina(self, chave, rotulo, widget):
        """Registra uma página de conteúdo e cria o botão correspondente
        na sidebar, inserido logo antes do stretch."""
        indice = self.stack_conteudo.addWidget(widget)

        botao = QPushButton(rotulo)
        botao.setObjectName("botaoSidebar")
        botao.setCheckable(True)
        botao.clicked.connect(lambda: self._selecionar(indice, botao))
        self._botoes_nav.append(botao)

        # insere antes do stretch (que é o último item antes da linha)
        pos_insercao = self.layout_sidebar.count() - 3
        self.layout_sidebar.insertWidget(pos_insercao, botao)

        if len(self._botoes_nav) == 1:
            self._selecionar(indice, botao)

        return indice

    def _selecionar(self, indice, botao_clicado):
        self.stack_conteudo.setCurrentIndex(indice)
        for botao in self._botoes_nav:
            ativo = botao is botao_clicado
            botao.setChecked(ativo)
            botao.setObjectName("botaoSidebarAtivo" if ativo else "botaoSidebar")
            botao.style().unpolish(botao)
            botao.style().polish(botao)

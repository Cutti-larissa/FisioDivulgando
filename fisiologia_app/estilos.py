# estilos.py
# Paleta e QSS centralizados para manter o app com visual consistente.

COR_FUNDO = "#0F5257"
COR_FUNDO_SIDEBAR = "#0A2342"
COR_FUNDO_SIDEBAR_HOVER = "#003B46"
COR_PRIMARIA = "#2EC4B6"
COR_PRIMARIA_HOVER = "#07575B"
COR_SECUNDARIA = "#66A5AD"
COR_SECUNDARIA_HOVER = "#D0FAF6"
COR_TEXTO = "#0A0F14"
COR_TEXTO_CLARO = "#FFF9F1"
COR_TEXTO_MUTED = "#C4DFE6"
COR_CARD = "#E6FFFA"
COR_BORDA = "#E5E7EB"
COR_PERIGO = "#BB0B0B"
COR_PERIGO_HOVER ="#DC2626"

FONTE_BASE = "Segoe UI"

QSS_GLOBAL = f"""
QWidget {{
    background-color: {COR_FUNDO};
    color: {COR_TEXTO};
    font-family: '{FONTE_BASE}';
    font-size: 14px;
}}

QLabel {{
    background-color: transparent;
}}

QLabel#tituloApp {{
    font-size: 40px;
    font-weight: 700;
    color: {COR_PRIMARIA};
}}

QLabel#subtituloApp {{
    font-size: 15px;
    color: {COR_PRIMARIA};
}}

QLabel#tituloTela {{
    font-size: 24px;
    font-weight: 700;
    color: {COR_TEXTO_CLARO};
}}

QLabel#tituloModulo {{
    font-size: 17px;
    font-weight: 700;
    color: {COR_TEXTO_CLARO};
}}

QLabel#subtituloModulo {{
    font-size: 11px;
    color: #9CA3AF;
}}

QFrame#cardInicial {{
    background-color: {COR_CARD};
    border-radius: 18px;
    border: 1px solid {COR_BORDA};
}}

QFrame#cardModulo {{
    background-color: {COR_CARD};
    border-radius: 14px;
    border: 1px solid {COR_BORDA};
}}

QFrame#cardModulo:hover {{
    border: 1px solid {COR_PRIMARIA};
}}

QFrame#painelResultado {{
    background-color: #EEF2FF;
    border-radius: 12px;
    border: 1px solid #C7D2FE;
}}

QFrame#grupoParametro {{
    background-color: {COR_CARD};
    border-radius: 12px;
    border: 1px solid {COR_BORDA};
}}

QPushButton {{
    background-color: {COR_PRIMARIA};
    color: white;
    border: none;
    border-radius: 10px;
    padding: 10px 18px;
    font-weight: 600;
}}

QPushButton:hover {{
    background-color: {COR_PRIMARIA_HOVER};
}}

QPushButton:pressed {{
    background-color: {COR_PRIMARIA_HOVER};
}}

QPushButton#botaoSecundario {{
    background-color: transparent;
    color: {COR_PRIMARIA};
    border: 1.5px solid {COR_PRIMARIA};
}}

QPushButton#botaoSecundario:hover {{
    background-color: {COR_SECUNDARIA_HOVER};
}}

QPushButton#botaoVoltar {{
    background-color: transparent;
    color: {COR_CARD};
    border: 1.5px solid {COR_CARD};
}}

QPushButton#botaoVoltar:hover {{
    background-color: {COR_FUNDO_SIDEBAR_HOVER};
}}

QPushButton#botaoPerigo {{
    background-color: transparent;
    color: {COR_PERIGO};
    border: 1.5px solid {COR_PERIGO};
}}

QPushButton#botaoPerigo:hover {{
    background-color: #FEF2F2;
    color: {COR_PERIGO_HOVER};
    border: 1.5px solid {COR_PERIGO_HOVER};
}}

QWidget#sidebar {{
    background-color: {COR_FUNDO_SIDEBAR};
}}

QPushButton#botaoSidebar {{
    background-color: transparent;
    color: {COR_TEXTO_CLARO};
    text-align: left;
    padding: 12px 16px;
    border-radius: 10px;
    font-weight: 500;
}}

QPushButton#botaoSidebar:hover {{
    background-color: {COR_FUNDO_SIDEBAR_HOVER};
}}

QPushButton#botaoSidebarAtivo {{
    background-color: {COR_PRIMARIA_HOVER};
    color: white;
    text-align: left;
    padding: 12px 16px;
    border-radius: 10px;
    font-weight: 600;
}}

QPushButton#botaoSidebarSair {{
    background-color: transparent;
    color: #F87171;
    text-align: left;
    padding: 12px 16px;
    border-radius: 10px;
    font-weight: 500;
}}

QPushButton#botaoSidebarSair:hover {{
    background-color: #3B1D1D;
}}

QLineEdit {{
    background-color: white;
    border: 1px solid {COR_BORDA};
    border-radius: 8px;
    padding: 6px 10px;
}}

QLineEdit:focus {{
    border: 1.5px solid {COR_PRIMARIA};
}}

QSlider::groove:horizontal {{
    height: 6px;
    background: {COR_BORDA};
    border-radius: 3px;
}}

QSlider::handle:horizontal {{
    background: {COR_PRIMARIA};
    width: 18px;
    height: 18px;
    margin: -6px 0;
    border-radius: 9px;
}}

QSlider::sub-page:horizontal {{
    background: {COR_PRIMARIA};
    border-radius: 3px;
}}

QTextEdit {{
    background-color: {COR_CARD};
    border: 1px solid {COR_BORDA};
    border-radius: 10px;
    padding: 12px;
}}

QScrollArea {{
    border: none;
}}
"""

# estilos.py
# Paleta e QSS centralizados para manter o app com visual consistente.

COR_FUNDO = "#F5DFBD"
COR_FUNDO_SIDEBAR = "#44586B"
COR_FUNDO_SIDEBAR_HOVER = "#374151"
COR_PRIMARIA = "#3A8F8C"
COR_PRIMARIA_HOVER = "#3651D4"
COR_SECUNDARIA = "#2EC4B6"
COR_TEXTO = "#1F2937"
COR_TEXTO_CLARO = "#F9FAFB"
COR_TEXTO_MUTED = "#6B7280"
COR_CARD = "#D5E3E7"
COR_BORDA = "#E5E7EB"
COR_PERIGO = "#B45953"
COR_PERIGO_HOVER = "#DC2626"

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
    color: {COR_TEXTO_MUTED};
}}

QLabel#tituloTela {{
    font-size: 24px;
    font-weight: 700;
    color: {COR_TEXTO};
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
    background-color: #2D46B9;
}}

QPushButton#botaoSecundario {{
    background-color: transparent;
    color: {COR_PRIMARIA};
    border: 1.5px solid {COR_PRIMARIA};
}}

QPushButton#botaoSecundario:hover {{
    background-color: #EEF1FF;
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
    background-color: {COR_PRIMARIA};
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

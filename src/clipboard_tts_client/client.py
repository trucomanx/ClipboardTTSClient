#!/usr/bin/python3
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QTextEdit, QLabel
from PyQt5.QtGui import QClipboard, QPixmap
from PyQt5.QtCore import Qt
import os
from langdetect import detect
import requests

def detectar_linguagem(texto):
    try:
        linguagem = detect(texto)
        return linguagem
    except Exception as e:
        return "en";


def send_json_from_dict(server_url,data):
    # Enviar solicitação POST ao servidor
    response = requests.post(f'{server_url}/add_task', json=data)

    if response.status_code == 200:
        print(f"Task sent successfully! ID: {response.json()['id']}")
        return response.json()['id'];
    else:
        print("Error submitting task.")
        return None

class ClipboardApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Clipboard TTS Client')
        self.setGeometry(100, 100, 180, 256)

        # Layout
        layout = QVBoxLayout()

        # Obter o caminho do diretório onde o script está localizado
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Construir o caminho para o ícone
        icon_path = os.path.join(base_dir, 'icons', 'logo.png')

        # Logo
        self.logo = QLabel(self)
        pixmap = QPixmap(icon_path)
        self.logo.setPixmap(pixmap)
        self.logo.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.logo)

        # Botão
        self.button = QPushButton('Play clipboard text', self)
        self.button.clicked.connect(self.get_clipboard_text)
        layout.addWidget(self.button)

        # Caixa de texto para exibir o texto retornado
        self.text_edit = QTextEdit(self)
        self.text_edit.setReadOnly(True)  # Apenas para leitura
        layout.addWidget(self.text_edit)

        # Configura o layout
        self.setLayout(layout)

    def get_clipboard_text(self):
        # Obtém o texto da área de transferência
        clipboard = QApplication.clipboard()
        text = clipboard.text()

        # Aplica a função my_func ao texto obtido
        ret_str = self.my_func(text)

        # Exibe o texto retornado no QTextEdit
        self.text_edit.setText(ret_str)

    def my_func(self, text):
        # Placeholder para a função que você irá implementar
        # Retorna uma string com base no texto passado
        if text.strip()=="":
            return "";
        
        SERVER_URL = 'http://localhost:5000'
        DATA={
            "text": text, 
            "language": detectar_linguagem(text),
            "split_pattern": [".", "\n\n"], 
            "speed":1.25 
        }
        ret_str=send_json_from_dict(SERVER_URL,DATA)
        
        return ret_str

def main():
    app = QApplication(sys.argv)
    ex = ClipboardApp()
    ex.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main();

#!/usr/bin/python

import signal
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk, AppIndicator3
from PyQt5.QtWidgets import QApplication
import os

from lib_funcs import detectar_linguagem
from lib_funcs import send_json_from_dict
from lib_funcs import tts_play

last_play_id=None;

def quit(source):
    Gtk.main_quit();

def play(source):
    # Verifica se QApplication já existe
    app = QApplication.instance()
    if app is None:
        app = QApplication([])  # Inicializa QApplication se não existir
    
    clipboard = app.clipboard()  # Acessa o clipboard
    text = clipboard.text()  # Obtém o texto do clipboard
    
    # Suponho que tts_play seja outra função que você implementou
    last_play_id = tts_play(text)

def main():
    # Criação do indicador
    indicator = AppIndicator3.Indicator.new(
        "meu-indicador",                       # ID do indicador
        os.path.join(os.path.dirname(os.path.abspath(__file__)), 'icons', 'logo.png'), 
        AppIndicator3.IndicatorCategory.APPLICATION_STATUS
    )

    # Criação do menu
    menu = Gtk.Menu()

    # Adicionando exit
    item_play = Gtk.MenuItem(label="Play clipboard")
    item_play.connect("activate", play)
    menu.append(item_play)

    # Adicionando exit
    item_quit = Gtk.MenuItem(label="Exit")
    item_quit.connect("activate", quit)
    menu.append(item_quit)

    # Mostrar o menu
    menu.show_all()

    # Associar o menu ao indicador
    indicator.set_menu(menu)

    # Exibir o indicador
    indicator.set_status(AppIndicator3.IndicatorStatus.ACTIVE)

    # Manter o aplicativo rodando
    signal.signal(signal.SIGINT, signal.SIG_DFL)
    Gtk.main()

if __name__ == '__main__':
    main();

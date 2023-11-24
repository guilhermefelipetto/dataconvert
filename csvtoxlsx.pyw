"""
csv = str(input('Arquivo CSV: '))

if not csv.endswith('.csv'):
    csv += '.csv'

xlsx = f'XLSX_{csv[:-4]}.xlsx'

print(csv)

df = pd.read_csv(csv)

df.to_excel(xlsx, index=False)
"""

import sys
import os
import typing
from PyQt5 import QtCore

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QListWidget
import pandas as pd

class FileLister(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Obtem o caminho do diretorio onde o script esta sendo executado
        current_dir = os.path.dirname(os.path.realpath(__file__))

        # Lista os arquivos do diretorio
        files = os.listdir(current_dir)

        # Cria uma lista de widgets para exibir o nome dos arquivos
        file_list_widget = QListWidget(self)
        file_list_widget.addItems(files)

        # Configura o layout da janela
        layout = QVBoxLayout()
        layout.addWidget(file_list_widget)

        self.setLayout(layout)

        # Configuracoes da janela principal
        self.setGeometry(100, 100, 400, 300)
        self.setWindowTitle('Listagem de Arquivos')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileLister()
    sys.exit(app.exec_())

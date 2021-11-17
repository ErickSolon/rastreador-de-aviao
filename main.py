import sys

from Tela import tela
from PyQt5 import QtWidgets
from PyQt5.QtGui import QPixmap
from selenium import webdriver


class MainWindow(QtWidgets.QMainWindow, tela.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.imagem.setText("Aperte em atualizar parar rastrear aviões!")
        self.atualizar.clicked.connect(self.botao_action)

    def botao_action(self):
        try:
            option = webdriver.FirefoxOptions()
            option.add_argument('--headless')

            browser = webdriver.Firefox(executable_path="Driver/geckodriver", options=option)
            browser.get("https://pt.flightaware.com/live/map")
            browser.save_screenshot("Imagens/screenshot.png")
            browser.close()

            self.imagem.setPixmap(QPixmap("Imagens/screenshot.png"))
        except Exception as e:
            self.imagem.setText("Erro! " + str(e))


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

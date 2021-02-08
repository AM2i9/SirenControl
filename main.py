from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from siren import Siren
import time

if __name__ == "__main__":

    siren = Siren("10.0.0.65",90)

    Form, Window = uic.loadUiType("siren.ui")

    app = QApplication([])
    window = Window()
    form = Form()
    form.setupUi(window)

    form.steadyButton.pressed.connect(lambda : siren.steady())
    form.yelpButton.pressed.connect(lambda : siren.yelp())

    form.steadyButton.released.connect(lambda : siren.off())
    form.yelpButton.released.connect(lambda : siren.off())

    window.show()
    app.exec_()
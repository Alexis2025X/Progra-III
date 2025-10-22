from logging import exception

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QRadioButton, QPushButton, \
    QMessageBox, QCheckBox
import sys

class ventana(QMainWindow):
    def __init__(self):
        super().__init__()#Llamamos el constructor de lo que se heredo de QMainWindow
        self.setWindowTitle("Calculadora con opciones")
        self.setGeometry(500, 200, 250, 300)

        self.lblNum1 = QLabel(self)
        self.lblNum1.setText("Primer numero: ")
        self.lblNum1.move(5, 10)#(x, y)

        self.txtNumero1 = QLineEdit(self)
        self.txtNumero1.move(100, 10)
        #self.num1 = float(self.txtNumero1.text())

        self.lblNum1 = QLabel(self)
        self.lblNum1.setText("Segundo numero: ")
        self.lblNum1.move(5, 50)#(x, y)


        self.txtNumero2 = QLineEdit(self)
        self.txtNumero2.move(100, 50)
        #self.num2 = self.txtNumero2.text()

        self.lblResultado = QLabel(self)
        self.lblResultado.setText("Resultado: ")
        self.lblResultado.move(100, 80)  # (x, y)

        self.rdSuma = QRadioButton (self)
        self.rdSuma.setChecked(True)
        self.rdSuma.move(30, 100)

        self.lblSuma = QLabel(self)
        self.lblSuma.setText("Suma")
        self.lblSuma.move(60, 100)#(x, y)

        self.rdResta = QRadioButton (self)
        self.rdResta.move(30, 120)

        self.lblResta = QLabel(self)
        self.lblResta.setText("Resta")
        self.lblResta.move(60, 120)

        self.rdMulti = QRadioButton (self)
        self.rdMulti.move(30, 140)

        self.lblMulti = QLabel(self)
        self.lblMulti.setText("Multiplicación")
        self.lblMulti.move(60, 140)

        self.rdDivi = QRadioButton (self)
        self.rdDivi.move(30, 160)

        self.lblDivi = QLabel(self)
        self.lblDivi.setText("División")
        self.lblDivi.move(60, 160)

        self.btnEjecutar = QPushButton(self)
        self.btnEjecutar.setText("Ejecutar")
        self.btnEjecutar.setGeometry(0, 0, 60, 30)# x, y, ancho, alto
        self.btnEjecutar.move(70, 200)
        self.btnEjecutar.clicked.connect(self.ejecutar)

        self.btnCerrar = QPushButton(self)
        self.btnCerrar.setText("Cerrar")
        self.btnCerrar.setGeometry(0, 0, 60, 30)# x, y, ancho, alto
        self.btnCerrar.move(130, 200)
        self.btnCerrar.clicked.connect(self.Cancelar)


    def Cancelar(self):
        self.close()

    def ejecutar(self):
        self.validar()

    def validar(self):
        num1 = self.txtNumero1.text()
        num2 = self.txtNumero2.text()
        if len(num1) == 0 or len(num2) == 0:
            QMessageBox.critical(self, "Error", "Los campos no deben estar vacios")
        else:
            self.operacion()
            #self.numero_valido()
        """
    def numero_valido(self):
        num1 = float(self.txtNumero1.text())
        num2 = float(self.txtNumero2.text())
        if num1 < 0 or num2 < 0:
            QMessageBox.critical(self, "Error", "El número no puede ser menor a 0")
        else:
            self.operacion()
        """

    def operacion(self):
        num1 = float(self.txtNumero1.text())
        num2 = float(self.txtNumero2.text())
        if self.rdSuma.isChecked():
            resul = num1 + num2
        elif self.rdResta.isChecked():
            resul = num1 - num2
        elif self.rdMulti.isChecked():
            resul = num1 * num2
        else:
            resul = num1 / num2
        self.lblResultado.setText(f"Resultado: {resul}")



app = QApplication(sys.argv)#Crea la app
window = ventana()
window.show()#Muestra ventana
app.exec()
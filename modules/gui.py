# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gui.ui'
##
## Created by: Qt User Interface Compiler version 6.8.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(613, 754)
        font = QFont()
        font.setBold(False)
        font.setKerning(True)
        MainWindow.setFont(font)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 500, 81, 16))
        font1 = QFont()
        font1.setBold(True)
        font1.setKerning(True)
        self.label.setFont(font1)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 300, 71, 16))
        self.label_3.setFont(font1)
        self.resultado = QPlainTextEdit(self.centralwidget)
        self.resultado.setObjectName(u"resultado")
        self.resultado.setGeometry(QRect(30, 530, 551, 181))
        self.resultado.setReadOnly(True)
        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setGeometry(QRect(30, 480, 551, 16))
        font2 = QFont()
        font2.setPointSize(14)
        font2.setBold(False)
        font2.setKerning(True)
        self.line_2.setFont(font2)
        self.line_2.setStyleSheet(u"")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)
        self.preview = QTextEdit(self.centralwidget)
        self.preview.setObjectName(u"preview")
        self.preview.setEnabled(False)
        self.preview.setGeometry(QRect(30, 330, 301, 141))
        self.preview.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(350, 330, 231, 141))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.simular = QPushButton(self.frame)
        self.simular.setObjectName(u"simular")
        self.simular.setGeometry(QRect(50, 90, 131, 22))
        self.simular.setStyleSheet(u"color: rgb(3, 47, 29);\n"
"background-color: rgb(51, 209, 122);")
        self.agregar_proceso = QPushButton(self.frame)
        self.agregar_proceso.setObjectName(u"agregar_proceso")
        self.agregar_proceso.setGeometry(QRect(50, 30, 131, 22))
        self.eliminar_ultimo = QPushButton(self.frame)
        self.eliminar_ultimo.setObjectName(u"eliminar_ultimo")
        self.eliminar_ultimo.setGeometry(QRect(50, 60, 131, 22))
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(100, 300, 431, 16))
        self.label_9.setFont(font)
        self.label_9.setMargin(0)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 60, 541, 221))
        self.groupBox.setFont(font)
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.horizontalLayoutWidget = QWidget(self.groupBox)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(10, 10, 521, 201))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_4 = QLabel(self.horizontalLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_2.addWidget(self.label_4)

        self.id = QSpinBox(self.horizontalLayoutWidget)
        self.id.setObjectName(u"id")

        self.verticalLayout_2.addWidget(self.id)

        self.label_5 = QLabel(self.horizontalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_2.addWidget(self.label_5)

        self.llegada = QSpinBox(self.horizontalLayoutWidget)
        self.llegada.setObjectName(u"llegada")

        self.verticalLayout_2.addWidget(self.llegada)

        self.label_8 = QLabel(self.horizontalLayoutWidget)
        self.label_8.setObjectName(u"label_8")

        self.verticalLayout_2.addWidget(self.label_8)

        self.burst = QSpinBox(self.horizontalLayoutWidget)
        self.burst.setObjectName(u"burst")

        self.verticalLayout_2.addWidget(self.burst)

        self.label_7 = QLabel(self.horizontalLayoutWidget)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_2.addWidget(self.label_7)

        self.prioridad = QSpinBox(self.horizontalLayoutWidget)
        self.prioridad.setObjectName(u"prioridad")

        self.verticalLayout_2.addWidget(self.prioridad)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.horizontalSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_6 = QLabel(self.horizontalLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout.addWidget(self.label_6)

        self.memoria = QSpinBox(self.horizontalLayoutWidget)
        self.memoria.setObjectName(u"memoria")
        self.memoria.setMinimum(100)
        self.memoria.setMaximum(1000)

        self.verticalLayout.addWidget(self.memoria)

        self.label_10 = QLabel(self.horizontalLayoutWidget)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout.addWidget(self.label_10)

        self.memoria_disponible = QSpinBox(self.horizontalLayoutWidget)
        self.memoria_disponible.setObjectName(u"memoria_disponible")
        self.memoria_disponible.setMinimum(300)
        self.memoria_disponible.setMaximum(2000)

        self.verticalLayout.addWidget(self.memoria_disponible)

        self.verticalSpacer = QSpacerItem(20, 45, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label_11 = QLabel(self.horizontalLayoutWidget)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout.addWidget(self.label_11)

        self.quantum = QSpinBox(self.horizontalLayoutWidget)
        self.quantum.setObjectName(u"quantum")
        self.quantum.setMinimum(1)
        self.quantum.setMaximum(10)
        self.quantum.setValue(2)

        self.verticalLayout.addWidget(self.quantum)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 30, 251, 16))
        self.label_2.setFont(font1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Simulaci\u00f3n Procesos", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resultado", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Preview:", None))
        self.resultado.setPlainText("")
        self.simular.setText(QCoreApplication.translate("MainWindow", u"Simular", None))
        self.agregar_proceso.setText(QCoreApplication.translate("MainWindow", u"Agregar proceso", None))
        self.eliminar_ultimo.setText(QCoreApplication.translate("MainWindow", u"Eliminar ultimo", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"ID, LLEGADA, BURST, MEMORIA, PRIORIDAD", None))
        self.groupBox.setTitle("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"LLEGADA:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"BURST", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"PRIORIDAD", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"MEMORIA ASIGNADA", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"MEMORIA DISPONIBLE", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"QUANTUM (Round Robin)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Ingrese los valores de los procesos:", None))
    # retranslateUi


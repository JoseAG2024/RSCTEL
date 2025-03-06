# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mapperWJBfuv.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QSpinBox, QVBoxLayout,
    QWidget)

class Ui_principal(object):
    def setupUi(self, principal):
        if not principal.objectName():
            principal.setObjectName(u"principal")
        principal.resize(479, 690)
        principal.setMinimumSize(QSize(0, 0))
        principal.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(23, 83, 160, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        brush1 = QBrush(QColor(35, 125, 240, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        brush2 = QBrush(QColor(29, 104, 200, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(12, 42, 80, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(15, 55, 107, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush5)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette.setBrush(QPalette.Active, QPalette.Window, brush5)
        brush6 = QBrush(QColor(23, 83, 160, 150))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        brush7 = QBrush(QColor(139, 169, 207, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush7)
        brush8 = QBrush(QColor(255, 255, 220, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush8)
        brush9 = QBrush(QColor(214, 214, 214, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush9)
        brush10 = QBrush(QColor(0, 0, 0, 127))
        brush10.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush9)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush10)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush8)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush9)
        brush11 = QBrush(QColor(12, 42, 80, 127))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        brush12 = QBrush(QColor(30, 108, 208, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush12)
        principal.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        principal.setFont(font)
        self.centralwidget = QWidget(principal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.label.setFont(font1)

        self.verticalLayout.addWidget(self.label)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.sBOportunidad = QSpinBox(self.centralwidget)
        self.sBOportunidad.setObjectName(u"sBOportunidad")
        self.sBOportunidad.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        self.sBOportunidad.setPalette(palette1)
        self.sBOportunidad.setMaximum(9999)

        self.horizontalLayout_3.addWidget(self.sBOportunidad)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.cmbCatalogos = QComboBox(self.centralwidget)
        self.cmbCatalogos.setObjectName(u"cmbCatalogos")

        self.horizontalLayout_6.addWidget(self.cmbCatalogos)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)

        self.horizontalLayout_6.setStretch(1, 40)

        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.gbEnergia = QGroupBox(self.centralwidget)
        self.gbEnergia.setObjectName(u"gbEnergia")
        self.gbEnergia.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        brush13 = QBrush(QColor(138, 138, 138, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette2.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.gbEnergia.setPalette(palette2)
        self.gbEnergia.setCheckable(True)
        self.verticalLayout_7 = QVBoxLayout(self.gbEnergia)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.label_12 = QLabel(self.gbEnergia)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout_15.addWidget(self.label_12)

        self.cmbTarifaLuz = QComboBox(self.gbEnergia)
        self.cmbTarifaLuz.setObjectName(u"cmbTarifaLuz")
        palette3 = QPalette()
        brush14 = QBrush(QColor(140, 140, 140, 255))
        brush14.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        brush15 = QBrush(QColor(149, 149, 149, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        self.cmbTarifaLuz.setPalette(palette3)

        self.verticalLayout_15.addWidget(self.cmbTarifaLuz)


        self.verticalLayout_7.addLayout(self.verticalLayout_15)

        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_6 = QLabel(self.gbEnergia)
        self.label_6.setObjectName(u"label_6")

        self.verticalLayout_8.addWidget(self.label_6)

        self.lECUPSLuz = QLineEdit(self.gbEnergia)
        self.lECUPSLuz.setObjectName(u"lECUPSLuz")

        self.verticalLayout_8.addWidget(self.lECUPSLuz)


        self.verticalLayout_7.addLayout(self.verticalLayout_8)


        self.verticalLayout.addWidget(self.gbEnergia)

        self.gBGas = QGroupBox(self.centralwidget)
        self.gBGas.setObjectName(u"gBGas")
        self.gBGas.setEnabled(True)
        self.gBGas.setMinimumSize(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush13)
        palette4.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.gBGas.setPalette(palette4)
        self.gBGas.setCheckable(True)
        self.gBGas.setChecked(False)
        self.verticalLayout_5 = QVBoxLayout(self.gBGas)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_11 = QLabel(self.gBGas)
        self.label_11.setObjectName(u"label_11")

        self.verticalLayout_14.addWidget(self.label_11)

        self.cmbTarifaGas = QComboBox(self.gBGas)
        self.cmbTarifaGas.setObjectName(u"cmbTarifaGas")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush14)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush15)
        self.cmbTarifaGas.setPalette(palette5)

        self.verticalLayout_14.addWidget(self.cmbTarifaGas)


        self.verticalLayout_5.addLayout(self.verticalLayout_14)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.gBGas)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout_6.addWidget(self.label_5)

        self.lECUPSGas = QLineEdit(self.gBGas)
        self.lECUPSGas.setObjectName(u"lECUPSGas")

        self.verticalLayout_6.addWidget(self.lECUPSGas)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.verticalLayout.addWidget(self.gBGas)

        self.gBDireccion = QGroupBox(self.centralwidget)
        self.gBDireccion.setObjectName(u"gBDireccion")
        self.gBDireccion.setMinimumSize(QSize(0, 0))
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.Accent, brush)
        palette6.setBrush(QPalette.Inactive, QPalette.Accent, brush)
        palette6.setBrush(QPalette.Disabled, QPalette.Accent, brush)
        self.gBDireccion.setPalette(palette6)
        self.verticalLayout_9 = QVBoxLayout(self.gBDireccion)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_7 = QLabel(self.gBDireccion)
        self.label_7.setObjectName(u"label_7")

        self.verticalLayout_10.addWidget(self.label_7)

        self.cmbProvincia = QComboBox(self.gBDireccion)
        self.cmbProvincia.setObjectName(u"cmbProvincia")
        self.cmbProvincia.setEditable(False)
        self.cmbProvincia.setSizeAdjustPolicy(QComboBox.SizeAdjustPolicy.AdjustToMinimumContentsLengthWithIcon)
        self.cmbProvincia.setFrame(True)
        self.cmbProvincia.setModelColumn(0)

        self.verticalLayout_10.addWidget(self.cmbProvincia)


        self.horizontalLayout.addLayout(self.verticalLayout_10)

        self.horizontalLayout.setStretch(0, 50)

        self.verticalLayout_9.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_9 = QLabel(self.gBDireccion)
        self.label_9.setObjectName(u"label_9")

        self.verticalLayout_12.addWidget(self.label_9)

        self.lENombreCalle = QLineEdit(self.gBDireccion)
        self.lENombreCalle.setObjectName(u"lENombreCalle")

        self.verticalLayout_12.addWidget(self.lENombreCalle)


        self.horizontalLayout_2.addLayout(self.verticalLayout_12)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_10 = QLabel(self.gBDireccion)
        self.label_10.setObjectName(u"label_10")

        self.verticalLayout_13.addWidget(self.label_10)

        self.lENumeroCalle = QLineEdit(self.gBDireccion)
        self.lENumeroCalle.setObjectName(u"lENumeroCalle")

        self.verticalLayout_13.addWidget(self.lENumeroCalle)


        self.horizontalLayout_2.addLayout(self.verticalLayout_13)

        self.horizontalLayout_2.setStretch(0, 80)
        self.horizontalLayout_2.setStretch(1, 20)

        self.verticalLayout_9.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.gBDireccion)
        self.label_13.setObjectName(u"label_13")

        self.verticalLayout_16.addWidget(self.label_13)

        self.lEPisoLetra = QLineEdit(self.gBDireccion)
        self.lEPisoLetra.setObjectName(u"lEPisoLetra")

        self.verticalLayout_16.addWidget(self.lEPisoLetra)


        self.horizontalLayout_5.addLayout(self.verticalLayout_16)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_14 = QLabel(self.gBDireccion)
        self.label_14.setObjectName(u"label_14")

        self.verticalLayout_17.addWidget(self.label_14)

        self.lEBloqueEscalera = QLineEdit(self.gBDireccion)
        self.lEBloqueEscalera.setObjectName(u"lEBloqueEscalera")

        self.verticalLayout_17.addWidget(self.lEBloqueEscalera)


        self.horizontalLayout_5.addLayout(self.verticalLayout_17)

        self.horizontalLayout_5.setStretch(0, 80)
        self.horizontalLayout_5.setStretch(1, 20)

        self.verticalLayout_9.addLayout(self.horizontalLayout_5)


        self.verticalLayout.addWidget(self.gBDireccion)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.pBConfirmar = QPushButton(self.centralwidget)
        self.pBConfirmar.setObjectName(u"pBConfirmar")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Dark, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Active, QPalette.HighlightedText, brush5)
        palette7.setBrush(QPalette.Active, QPalette.Link, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Button, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Dark, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette7.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush5)
        palette7.setBrush(QPalette.Inactive, QPalette.Link, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush5)
        brush16 = QBrush(QColor(249, 249, 249, 77))
        brush16.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Disabled, QPalette.Button, brush16)
        palette7.setBrush(QPalette.Disabled, QPalette.Dark, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush5)
        brush17 = QBrush(QColor(0, 0, 0, 92))
        brush17.setStyle(Qt.SolidPattern)
        palette7.setBrush(QPalette.Disabled, QPalette.ButtonText, brush17)
        palette7.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush5)
        palette7.setBrush(QPalette.Disabled, QPalette.Link, brush5)
        self.pBConfirmar.setPalette(palette7)
        self.pBConfirmar.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.horizontalLayout_4.addWidget(self.pBConfirmar)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        principal.setCentralWidget(self.centralwidget)

        self.retranslateUi(principal)

        QMetaObject.connectSlotsByName(principal)
    # setupUi

    def retranslateUi(self, principal):
        principal.setWindowTitle(QCoreApplication.translate("principal", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("principal", u"POR FAVOR CONFIRMA LOS SIGUIENTES DATOS:", None))
        self.label_4.setText(QCoreApplication.translate("principal", u"NUMERO DE OPORTUNIDAD", None))
        self.label_3.setText(QCoreApplication.translate("principal", u"Elige el catalogo:", None))
        self.label_2.setText(QCoreApplication.translate("principal", u"\u00bfQue productos o servicios rellenamos en la oportunidad?", None))
        self.gbEnergia.setTitle(QCoreApplication.translate("principal", u"Energia", None))
        self.label_12.setText(QCoreApplication.translate("principal", u"Tarifa Luz vendida:", None))
        self.cmbTarifaLuz.setPlaceholderText(QCoreApplication.translate("principal", u"Elige la tarifa que haz vendido", None))
        self.label_6.setText(QCoreApplication.translate("principal", u"CUPS", None))
        self.gBGas.setTitle(QCoreApplication.translate("principal", u"Gas", None))
        self.label_11.setText(QCoreApplication.translate("principal", u"Tarifa Gas vendida:", None))
        self.cmbTarifaGas.setPlaceholderText(QCoreApplication.translate("principal", u"Elige la tarifa que haz vendido", None))
        self.label_5.setText(QCoreApplication.translate("principal", u"CUPS", None))
        self.gBDireccion.setTitle(QCoreApplication.translate("principal", u"Datos de Direccion", None))
        self.label_7.setText(QCoreApplication.translate("principal", u"Provincia", None))
        self.cmbProvincia.setPlaceholderText(QCoreApplication.translate("principal", u"Elije una provincia", None))
        self.label_9.setText(QCoreApplication.translate("principal", u"Nombre de Calle", None))
        self.label_10.setText(QCoreApplication.translate("principal", u"Numero de Calle", None))
        self.label_13.setText(QCoreApplication.translate("principal", u"Piso/Letra", None))
        self.label_14.setText(QCoreApplication.translate("principal", u"Bloque/Escalera", None))
        self.pBConfirmar.setText(QCoreApplication.translate("principal", u"Confirmar y Continuar", None))
    # retranslateUi


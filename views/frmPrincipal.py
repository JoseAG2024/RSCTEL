# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RSCTEL_UiPrincipaluopoRf.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QAbstractSpinBox, QApplication,
    QCheckBox, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QHeaderView, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QSpinBox, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_frmPrincipal(object):
    def setupUi(self, frmPrincipal):
        if not frmPrincipal.objectName():
            frmPrincipal.setObjectName(u"frmPrincipal")
        frmPrincipal.resize(850, 859)
        frmPrincipal.setMinimumSize(QSize(850, 850))
        palette = QPalette()
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 179))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        brush2 = QBrush(QColor(127, 127, 127, 179))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush2)
        brush3 = QBrush(QColor(170, 170, 170, 179))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        brush4 = QBrush(QColor(255, 255, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush4)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush)
        brush5 = QBrush(QColor(255, 255, 255, 217))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        brush6 = QBrush(QColor(255, 255, 220, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
        brush7 = QBrush(QColor(0, 0, 0, 127))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Active, QPalette.Accent, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.Accent, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
        brush8 = QBrush(QColor(127, 127, 127, 89))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        frmPrincipal.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        frmPrincipal.setFont(font)
        self.centralwidget = QWidget(frmPrincipal)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabFichas = QTabWidget(self.centralwidget)
        self.tabFichas.setObjectName(u"tabFichas")
        self.tabFichas.setEnabled(True)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Active, QPalette.Accent, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Accent, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Accent, brush1)
        self.tabFichas.setPalette(palette1)
        self.tabFichas.setTabPosition(QTabWidget.TabPosition.North)
        self.tabFichas.setTabShape(QTabWidget.TabShape.Rounded)
        self.tabFichas.setUsesScrollButtons(True)
        self.tabFichas.setDocumentMode(False)
        self.tabFichas.setTabsClosable(False)
        self.tabFichas.setMovable(False)
        self.tabFichaEnergia = QWidget()
        self.tabFichaEnergia.setObjectName(u"tabFichaEnergia")
        self.tabFichaEnergia.setEnabled(True)
        self.verticalLayout_2 = QVBoxLayout(self.tabFichaEnergia)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_7)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, -1, -1, 10)
        self.lblTitulo2_2 = QLabel(self.tabFichaEnergia)
        self.lblTitulo2_2.setObjectName(u"lblTitulo2_2")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(12)
        font1.setBold(True)
        self.lblTitulo2_2.setFont(font1)
        self.lblTitulo2_2.setMargin(0)

        self.verticalLayout_10.addWidget(self.lblTitulo2_2)

        self.line = QFrame(self.tabFichaEnergia)
        self.line.setObjectName(u"line")
        self.line.setLineWidth(2)
        self.line.setFrameShape(QFrame.Shape.HLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line)

        self.scrollArea_2 = QScrollArea(self.tabFichaEnergia)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_2.setMidLineWidth(0)
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, -344, 736, 987))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.gBDatosGeneralesCliente = QGroupBox(self.scrollAreaWidgetContents_2)
        self.gBDatosGeneralesCliente.setObjectName(u"gBDatosGeneralesCliente")
        self.gBDatosGeneralesCliente.setMinimumSize(QSize(0, 0))
        palette2 = QPalette()
        brush9 = QBrush(QColor(222, 222, 222, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.gBDatosGeneralesCliente.setPalette(palette2)
        self.gBDatosGeneralesCliente.setFont(font1)
        self.verticalLayout_3 = QVBoxLayout(self.gBDatosGeneralesCliente)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.qLNombreCliente = QLabel(self.gBDatosGeneralesCliente)
        self.qLNombreCliente.setObjectName(u"qLNombreCliente")
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setItalic(False)
        self.qLNombreCliente.setFont(font2)

        self.verticalLayout_13.addWidget(self.qLNombreCliente)

        self.lENombreCliente = QLineEdit(self.gBDatosGeneralesCliente)
        self.lENombreCliente.setObjectName(u"lENombreCliente")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(10)
        font3.setBold(False)
        self.lENombreCliente.setFont(font3)

        self.verticalLayout_13.addWidget(self.lENombreCliente)


        self.horizontalLayout_8.addLayout(self.verticalLayout_13)

        self.line_4 = QFrame(self.gBDatosGeneralesCliente)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShadow(QFrame.Shadow.Plain)
        self.line_4.setLineWidth(1)
        self.line_4.setMidLineWidth(8)
        self.line_4.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_4)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lblDNI_NIE_4 = QLabel(self.gBDatosGeneralesCliente)
        self.lblDNI_NIE_4.setObjectName(u"lblDNI_NIE_4")
        self.lblDNI_NIE_4.setFont(font2)

        self.verticalLayout_14.addWidget(self.lblDNI_NIE_4)

        self.lEDNI = QLineEdit(self.gBDatosGeneralesCliente)
        self.lEDNI.setObjectName(u"lEDNI")
        self.lEDNI.setFont(font3)
        self.lEDNI.setMaxLength(9)

        self.verticalLayout_14.addWidget(self.lEDNI)


        self.horizontalLayout_8.addLayout(self.verticalLayout_14)

        self.line_5 = QFrame(self.gBDatosGeneralesCliente)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShadow(QFrame.Shadow.Plain)
        self.line_5.setLineWidth(1)
        self.line_5.setMidLineWidth(8)
        self.line_5.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_8.addWidget(self.line_5)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lblDNI_NIE_5 = QLabel(self.gBDatosGeneralesCliente)
        self.lblDNI_NIE_5.setObjectName(u"lblDNI_NIE_5")
        self.lblDNI_NIE_5.setFont(font2)

        self.verticalLayout_16.addWidget(self.lblDNI_NIE_5)

        self.lECodigoPostal = QLineEdit(self.gBDatosGeneralesCliente)
        self.lECodigoPostal.setObjectName(u"lECodigoPostal")
        self.lECodigoPostal.setFont(font3)
        self.lECodigoPostal.setClearButtonEnabled(True)

        self.verticalLayout_16.addWidget(self.lECodigoPostal)


        self.horizontalLayout_8.addLayout(self.verticalLayout_16)

        self.horizontalLayout_8.setStretch(0, 60)
        self.horizontalLayout_8.setStretch(2, 20)
        self.horizontalLayout_8.setStretch(4, 20)

        self.verticalLayout_3.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_3 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_3.setObjectName(u"lblProvincia_3")
        self.lblProvincia_3.setFont(font2)

        self.verticalLayout_15.addWidget(self.lblProvincia_3)

        self.cmbProvincia = QComboBox(self.gBDatosGeneralesCliente)
        self.cmbProvincia.setObjectName(u"cmbProvincia")
        self.cmbProvincia.setMaximumSize(QSize(16777215, 16777215))
        self.cmbProvincia.setFont(font3)
        self.cmbProvincia.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_15.addWidget(self.cmbProvincia)


        self.horizontalLayout_9.addLayout(self.verticalLayout_15)

        self.line_6 = QFrame(self.gBDatosGeneralesCliente)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShadow(QFrame.Shadow.Plain)
        self.line_6.setLineWidth(1)
        self.line_6.setMidLineWidth(8)
        self.line_6.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_9.addWidget(self.line_6)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_4 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_4.setObjectName(u"lblProvincia_4")
        self.lblProvincia_4.setFont(font2)

        self.verticalLayout_17.addWidget(self.lblProvincia_4)

        self.lEMunicipio = QLineEdit(self.gBDatosGeneralesCliente)
        self.lEMunicipio.setObjectName(u"lEMunicipio")
        self.lEMunicipio.setFont(font3)

        self.verticalLayout_17.addWidget(self.lEMunicipio)


        self.horizontalLayout_9.addLayout(self.verticalLayout_17)

        self.horizontalLayout_9.setStretch(0, 50)
        self.horizontalLayout_9.setStretch(2, 50)

        self.verticalLayout_3.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_5 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_5.setObjectName(u"lblProvincia_5")
        self.lblProvincia_5.setFont(font2)

        self.verticalLayout_18.addWidget(self.lblProvincia_5)

        self.lENombreCalle = QLineEdit(self.gBDatosGeneralesCliente)
        self.lENombreCalle.setObjectName(u"lENombreCalle")
        self.lENombreCalle.setFont(font3)

        self.verticalLayout_18.addWidget(self.lENombreCalle)


        self.horizontalLayout_10.addLayout(self.verticalLayout_18)

        self.line_8 = QFrame(self.gBDatosGeneralesCliente)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShadow(QFrame.Shadow.Plain)
        self.line_8.setLineWidth(1)
        self.line_8.setMidLineWidth(8)
        self.line_8.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_10.addWidget(self.line_8)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_6 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_6.setObjectName(u"lblProvincia_6")
        self.lblProvincia_6.setFont(font2)

        self.verticalLayout_19.addWidget(self.lblProvincia_6)

        self.sBNumeroDeLaCalle = QSpinBox(self.gBDatosGeneralesCliente)
        self.sBNumeroDeLaCalle.setObjectName(u"sBNumeroDeLaCalle")
        self.sBNumeroDeLaCalle.setFont(font3)
        self.sBNumeroDeLaCalle.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.sBNumeroDeLaCalle.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.sBNumeroDeLaCalle.setFrame(True)
        self.sBNumeroDeLaCalle.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sBNumeroDeLaCalle.setKeyboardTracking(True)
        self.sBNumeroDeLaCalle.setMaximum(999)
        self.sBNumeroDeLaCalle.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.verticalLayout_19.addWidget(self.sBNumeroDeLaCalle)


        self.horizontalLayout_10.addLayout(self.verticalLayout_19)

        self.line_7 = QFrame(self.gBDatosGeneralesCliente)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShadow(QFrame.Shadow.Plain)
        self.line_7.setLineWidth(1)
        self.line_7.setMidLineWidth(8)
        self.line_7.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_10.addWidget(self.line_7)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_7 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_7.setObjectName(u"lblProvincia_7")
        self.lblProvincia_7.setFont(font2)

        self.verticalLayout_20.addWidget(self.lblProvincia_7)

        self.lEPisoYLetra = QLineEdit(self.gBDatosGeneralesCliente)
        self.lEPisoYLetra.setObjectName(u"lEPisoYLetra")
        self.lEPisoYLetra.setFont(font3)

        self.verticalLayout_20.addWidget(self.lEPisoYLetra)


        self.horizontalLayout_10.addLayout(self.verticalLayout_20)

        self.line_11 = QFrame(self.gBDatosGeneralesCliente)
        self.line_11.setObjectName(u"line_11")
        self.line_11.setFrameShadow(QFrame.Shadow.Plain)
        self.line_11.setLineWidth(1)
        self.line_11.setMidLineWidth(8)
        self.line_11.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_10.addWidget(self.line_11)

        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_8 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_8.setObjectName(u"lblProvincia_8")
        self.lblProvincia_8.setFont(font2)

        self.verticalLayout_21.addWidget(self.lblProvincia_8)

        self.lEBloqueOEscalera = QLineEdit(self.gBDatosGeneralesCliente)
        self.lEBloqueOEscalera.setObjectName(u"lEBloqueOEscalera")
        self.lEBloqueOEscalera.setFont(font3)

        self.verticalLayout_21.addWidget(self.lEBloqueOEscalera)


        self.horizontalLayout_10.addLayout(self.verticalLayout_21)

        self.horizontalLayout_10.setStretch(0, 40)

        self.verticalLayout_3.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_16 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_16.setObjectName(u"lblProvincia_16")
        self.lblProvincia_16.setFont(font2)

        self.verticalLayout_22.addWidget(self.lblProvincia_16)

        self.lECUPS_Luz = QLineEdit(self.gBDatosGeneralesCliente)
        self.lECUPS_Luz.setObjectName(u"lECUPS_Luz")
        self.lECUPS_Luz.setFont(font3)

        self.verticalLayout_22.addWidget(self.lECUPS_Luz)


        self.horizontalLayout_15.addLayout(self.verticalLayout_22)

        self.line_9 = QFrame(self.gBDatosGeneralesCliente)
        self.line_9.setObjectName(u"line_9")
        self.line_9.setFrameShadow(QFrame.Shadow.Plain)
        self.line_9.setLineWidth(1)
        self.line_9.setMidLineWidth(8)
        self.line_9.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_15.addWidget(self.line_9)

        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_17 = QLabel(self.gBDatosGeneralesCliente)
        self.lblProvincia_17.setObjectName(u"lblProvincia_17")
        self.lblProvincia_17.setFont(font2)

        self.verticalLayout_23.addWidget(self.lblProvincia_17)

        self.lECUPS_Gas = QLineEdit(self.gBDatosGeneralesCliente)
        self.lECUPS_Gas.setObjectName(u"lECUPS_Gas")
        self.lECUPS_Gas.setFont(font3)

        self.verticalLayout_23.addWidget(self.lECUPS_Gas)


        self.horizontalLayout_15.addLayout(self.verticalLayout_23)

        self.horizontalLayout_15.setStretch(0, 50)
        self.horizontalLayout_15.setStretch(2, 50)

        self.verticalLayout_3.addLayout(self.horizontalLayout_15)


        self.verticalLayout_9.addWidget(self.gBDatosGeneralesCliente)

        self.groupBox_2 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 0))
        self.groupBox_2.setFont(font1)
        self.verticalLayout_32 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.lblDNI_NIE_9 = QLabel(self.groupBox_2)
        self.lblDNI_NIE_9.setObjectName(u"lblDNI_NIE_9")
        self.lblDNI_NIE_9.setFont(font2)

        self.verticalLayout_33.addWidget(self.lblDNI_NIE_9)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lENumeroIBAN = QLineEdit(self.groupBox_2)
        self.lENumeroIBAN.setObjectName(u"lENumeroIBAN")
        self.lENumeroIBAN.setFont(font2)
        self.lENumeroIBAN.setMouseTracking(False)
        self.lENumeroIBAN.setMaxLength(28)
        self.lENumeroIBAN.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lENumeroIBAN.setCursorPosition(0)
        self.lENumeroIBAN.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lENumeroIBAN.setClearButtonEnabled(True)

        self.horizontalLayout_17.addWidget(self.lENumeroIBAN)


        self.verticalLayout_33.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_14.addLayout(self.verticalLayout_33)

        self.line_12 = QFrame(self.groupBox_2)
        self.line_12.setObjectName(u"line_12")
        self.line_12.setFrameShadow(QFrame.Shadow.Plain)
        self.line_12.setLineWidth(1)
        self.line_12.setMidLineWidth(8)
        self.line_12.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_14.addWidget(self.line_12)

        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.lblDNI_NIE_10 = QLabel(self.groupBox_2)
        self.lblDNI_NIE_10.setObjectName(u"lblDNI_NIE_10")
        self.lblDNI_NIE_10.setFont(font2)

        self.verticalLayout_34.addWidget(self.lblDNI_NIE_10)

        self.lEEntidad = QLineEdit(self.groupBox_2)
        self.lEEntidad.setObjectName(u"lEEntidad")
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(12)
        font4.setBold(False)
        self.lEEntidad.setFont(font4)

        self.verticalLayout_34.addWidget(self.lEEntidad)


        self.horizontalLayout_14.addLayout(self.verticalLayout_34)

        self.horizontalLayout_14.setStretch(0, 50)
        self.horizontalLayout_14.setStretch(2, 50)

        self.verticalLayout_32.addLayout(self.horizontalLayout_14)


        self.verticalLayout_9.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.scrollAreaWidgetContents_2)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setMinimumSize(QSize(0, 0))
        self.groupBox_3.setFont(font1)
        self.verticalLayout_38 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.tWContratos = QTableWidget(self.groupBox_3)
        if (self.tWContratos.columnCount() < 13):
            self.tWContratos.setColumnCount(13)
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(10)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font5);
        self.tWContratos.setHorizontalHeaderItem(12, __qtablewidgetitem12)
        self.tWContratos.setObjectName(u"tWContratos")
        self.tWContratos.setMinimumSize(QSize(0, 200))
        self.tWContratos.setFont(font3)
        self.tWContratos.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tWContratos.setAlternatingRowColors(True)
        self.tWContratos.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tWContratos.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tWContratos.setShowGrid(True)
        self.tWContratos.setSortingEnabled(False)
        self.tWContratos.setCornerButtonEnabled(True)
        self.tWContratos.setRowCount(0)
        self.tWContratos.horizontalHeader().setVisible(True)
        self.tWContratos.horizontalHeader().setCascadingSectionResizes(True)
        self.tWContratos.horizontalHeader().setMinimumSectionSize(50)
        self.tWContratos.horizontalHeader().setHighlightSections(True)
        self.tWContratos.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tWContratos.horizontalHeader().setStretchLastSection(True)
        self.tWContratos.verticalHeader().setVisible(True)
        self.tWContratos.verticalHeader().setHighlightSections(False)
        self.tWContratos.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_38.addWidget(self.tWContratos)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, -1, -1, 10)
        self.pBEliminarContrato = QPushButton(self.groupBox_3)
        self.pBEliminarContrato.setObjectName(u"pBEliminarContrato")
        self.pBEliminarContrato.setEnabled(False)
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(10)
        font6.setBold(True)
        self.pBEliminarContrato.setFont(font6)

        self.horizontalLayout_6.addWidget(self.pBEliminarContrato)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)

        self.pBEditarContrato = QPushButton(self.groupBox_3)
        self.pBEditarContrato.setObjectName(u"pBEditarContrato")
        self.pBEditarContrato.setEnabled(False)
        self.pBEditarContrato.setFont(font6)

        self.horizontalLayout_6.addWidget(self.pBEditarContrato)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_2)

        self.pBAgregarContrato = QPushButton(self.groupBox_3)
        self.pBAgregarContrato.setObjectName(u"pBAgregarContrato")
        self.pBAgregarContrato.setEnabled(True)
        self.pBAgregarContrato.setFont(font6)

        self.horizontalLayout_6.addWidget(self.pBAgregarContrato)


        self.verticalLayout_38.addLayout(self.horizontalLayout_6)

        self.gBAgregarOEditarContrato = QGroupBox(self.groupBox_3)
        self.gBAgregarOEditarContrato.setObjectName(u"gBAgregarOEditarContrato")
        self.gBAgregarOEditarContrato.setEnabled(False)
        self.verticalLayout_4 = QVBoxLayout(self.gBAgregarOEditarContrato)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.lblDNI_NIE_16 = QLabel(self.gBAgregarOEditarContrato)
        self.lblDNI_NIE_16.setObjectName(u"lblDNI_NIE_16")
        self.lblDNI_NIE_16.setFont(font2)

        self.verticalLayout_42.addWidget(self.lblDNI_NIE_16)

        self.cmbCatalogos = QComboBox(self.gBAgregarOEditarContrato)
        self.cmbCatalogos.setObjectName(u"cmbCatalogos")
        self.cmbCatalogos.setMaximumSize(QSize(16777215, 16777215))
        self.cmbCatalogos.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_42.addWidget(self.cmbCatalogos)


        self.horizontalLayout_18.addLayout(self.verticalLayout_42)

        self.line_13 = QFrame(self.gBAgregarOEditarContrato)
        self.line_13.setObjectName(u"line_13")
        self.line_13.setFrameShadow(QFrame.Shadow.Plain)
        self.line_13.setLineWidth(1)
        self.line_13.setMidLineWidth(8)
        self.line_13.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_18.addWidget(self.line_13)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.lblDNI_NIE_17 = QLabel(self.gBAgregarOEditarContrato)
        self.lblDNI_NIE_17.setObjectName(u"lblDNI_NIE_17")
        self.lblDNI_NIE_17.setFont(font2)

        self.verticalLayout_43.addWidget(self.lblDNI_NIE_17)

        self.cmbTiposContratos = QComboBox(self.gBAgregarOEditarContrato)
        self.cmbTiposContratos.setObjectName(u"cmbTiposContratos")
        self.cmbTiposContratos.setMaximumSize(QSize(16777215, 16777215))
        self.cmbTiposContratos.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_43.addWidget(self.cmbTiposContratos)


        self.horizontalLayout_18.addLayout(self.verticalLayout_43)

        self.horizontalLayout_18.setStretch(0, 60)
        self.horizontalLayout_18.setStretch(2, 40)

        self.verticalLayout_4.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_47 = QVBoxLayout()
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.lblDNI_NIE_21 = QLabel(self.gBAgregarOEditarContrato)
        self.lblDNI_NIE_21.setObjectName(u"lblDNI_NIE_21")
        self.lblDNI_NIE_21.setFont(font2)

        self.verticalLayout_47.addWidget(self.lblDNI_NIE_21)

        self.cmbContratos = QComboBox(self.gBAgregarOEditarContrato)
        self.cmbContratos.setObjectName(u"cmbContratos")
        self.cmbContratos.setMaximumSize(QSize(16777215, 16777215))
        self.cmbContratos.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_47.addWidget(self.cmbContratos)


        self.horizontalLayout_13.addLayout(self.verticalLayout_47)

        self.line_14 = QFrame(self.gBAgregarOEditarContrato)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShadow(QFrame.Shadow.Plain)
        self.line_14.setLineWidth(1)
        self.line_14.setMidLineWidth(8)
        self.line_14.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_13.addWidget(self.line_14)

        self.verticalLayout_31 = QVBoxLayout()
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_31.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_15 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_15.setObjectName(u"lblProvincia_15")
        self.lblProvincia_15.setFont(font2)

        self.verticalLayout_31.addWidget(self.lblProvincia_15)

        self.lECUPS = QLineEdit(self.gBAgregarOEditarContrato)
        self.lECUPS.setObjectName(u"lECUPS")
        self.lECUPS.setFont(font4)

        self.verticalLayout_31.addWidget(self.lECUPS)


        self.horizontalLayout_13.addLayout(self.verticalLayout_31)

        self.horizontalLayout_13.setStretch(0, 40)
        self.horizontalLayout_13.setStretch(2, 60)

        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_13 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_13.setObjectName(u"lblProvincia_13")
        self.lblProvincia_13.setFont(font2)

        self.verticalLayout_28.addWidget(self.lblProvincia_13)

        self.cmbProvinciaSuministro = QComboBox(self.gBAgregarOEditarContrato)
        self.cmbProvinciaSuministro.setObjectName(u"cmbProvinciaSuministro")
        self.cmbProvinciaSuministro.setMaximumSize(QSize(16777215, 16777215))
        self.cmbProvinciaSuministro.setFont(font4)
        self.cmbProvinciaSuministro.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_28.addWidget(self.cmbProvinciaSuministro)


        self.horizontalLayout_12.addLayout(self.verticalLayout_28)

        self.line_15 = QFrame(self.gBAgregarOEditarContrato)
        self.line_15.setObjectName(u"line_15")
        self.line_15.setFrameShadow(QFrame.Shadow.Plain)
        self.line_15.setLineWidth(1)
        self.line_15.setMidLineWidth(8)
        self.line_15.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_12.addWidget(self.line_15)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_29.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_14 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_14.setObjectName(u"lblProvincia_14")
        self.lblProvincia_14.setFont(font2)

        self.verticalLayout_29.addWidget(self.lblProvincia_14)

        self.lEMunicipioSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lEMunicipioSuministro.setObjectName(u"lEMunicipioSuministro")
        self.lEMunicipioSuministro.setFont(font4)

        self.verticalLayout_29.addWidget(self.lEMunicipioSuministro)


        self.horizontalLayout_12.addLayout(self.verticalLayout_29)

        self.horizontalLayout_12.setStretch(0, 50)
        self.horizontalLayout_12.setStretch(2, 50)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_9 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_9.setObjectName(u"lblProvincia_9")
        self.lblProvincia_9.setFont(font2)

        self.verticalLayout_24.addWidget(self.lblProvincia_9)

        self.lENombreCalleSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lENombreCalleSuministro.setObjectName(u"lENombreCalleSuministro")
        self.lENombreCalleSuministro.setFont(font4)

        self.verticalLayout_24.addWidget(self.lENombreCalleSuministro)


        self.horizontalLayout_11.addLayout(self.verticalLayout_24)

        self.line_17 = QFrame(self.gBAgregarOEditarContrato)
        self.line_17.setObjectName(u"line_17")
        self.line_17.setFrameShadow(QFrame.Shadow.Plain)
        self.line_17.setLineWidth(1)
        self.line_17.setMidLineWidth(8)
        self.line_17.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_11.addWidget(self.line_17)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_10 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_10.setObjectName(u"lblProvincia_10")
        self.lblProvincia_10.setFont(font2)

        self.verticalLayout_25.addWidget(self.lblProvincia_10)

        self.sBNumeroCalleSuministro = QSpinBox(self.gBAgregarOEditarContrato)
        self.sBNumeroCalleSuministro.setObjectName(u"sBNumeroCalleSuministro")
        self.sBNumeroCalleSuministro.setFont(font4)
        self.sBNumeroCalleSuministro.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.sBNumeroCalleSuministro.setMaximum(999)
        self.sBNumeroCalleSuministro.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.verticalLayout_25.addWidget(self.sBNumeroCalleSuministro)


        self.horizontalLayout_11.addLayout(self.verticalLayout_25)

        self.line_16 = QFrame(self.gBAgregarOEditarContrato)
        self.line_16.setObjectName(u"line_16")
        self.line_16.setFrameShadow(QFrame.Shadow.Plain)
        self.line_16.setLineWidth(1)
        self.line_16.setMidLineWidth(8)
        self.line_16.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_11.addWidget(self.line_16)

        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_11 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_11.setObjectName(u"lblProvincia_11")
        self.lblProvincia_11.setFont(font2)

        self.verticalLayout_26.addWidget(self.lblProvincia_11)

        self.lEPisoYLetraSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lEPisoYLetraSuministro.setObjectName(u"lEPisoYLetraSuministro")
        self.lEPisoYLetraSuministro.setFont(font4)

        self.verticalLayout_26.addWidget(self.lEPisoYLetraSuministro)


        self.horizontalLayout_11.addLayout(self.verticalLayout_26)

        self.line_18 = QFrame(self.gBAgregarOEditarContrato)
        self.line_18.setObjectName(u"line_18")
        self.line_18.setFrameShadow(QFrame.Shadow.Plain)
        self.line_18.setLineWidth(1)
        self.line_18.setMidLineWidth(8)
        self.line_18.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_11.addWidget(self.line_18)

        self.verticalLayout_27 = QVBoxLayout()
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_12 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_12.setObjectName(u"lblProvincia_12")
        self.lblProvincia_12.setFont(font2)

        self.verticalLayout_27.addWidget(self.lblProvincia_12)

        self.lEBloqueEscaleraSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lEBloqueEscaleraSuministro.setObjectName(u"lEBloqueEscaleraSuministro")
        self.lEBloqueEscaleraSuministro.setFont(font4)

        self.verticalLayout_27.addWidget(self.lEBloqueEscaleraSuministro)


        self.horizontalLayout_11.addLayout(self.verticalLayout_27)

        self.line_19 = QFrame(self.gBAgregarOEditarContrato)
        self.line_19.setObjectName(u"line_19")
        self.line_19.setFrameShadow(QFrame.Shadow.Plain)
        self.line_19.setLineWidth(1)
        self.line_19.setMidLineWidth(8)
        self.line_19.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_11.addWidget(self.line_19)

        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_18 = QLabel(self.gBAgregarOEditarContrato)
        self.lblProvincia_18.setObjectName(u"lblProvincia_18")
        self.lblProvincia_18.setFont(font2)

        self.verticalLayout_30.addWidget(self.lblProvincia_18)

        self.lECodigoPostalSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lECodigoPostalSuministro.setObjectName(u"lECodigoPostalSuministro")
        self.lECodigoPostalSuministro.setFont(font3)
        self.lECodigoPostalSuministro.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lECodigoPostalSuministro.setClearButtonEnabled(True)

        self.verticalLayout_30.addWidget(self.lECodigoPostalSuministro)


        self.horizontalLayout_11.addLayout(self.verticalLayout_30)

        self.horizontalLayout_11.setStretch(0, 40)

        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.lblDNI_NIE_11 = QLabel(self.gBAgregarOEditarContrato)
        self.lblDNI_NIE_11.setObjectName(u"lblDNI_NIE_11")
        self.lblDNI_NIE_11.setFont(font2)

        self.verticalLayout_35.addWidget(self.lblDNI_NIE_11)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lENumeroIBANSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lENumeroIBANSuministro.setObjectName(u"lENumeroIBANSuministro")
        self.lENumeroIBANSuministro.setFont(font2)
        self.lENumeroIBANSuministro.setMouseTracking(False)
        self.lENumeroIBANSuministro.setMaxLength(28)
        self.lENumeroIBANSuministro.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lENumeroIBANSuministro.setCursorPosition(0)
        self.lENumeroIBANSuministro.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lENumeroIBANSuministro.setClearButtonEnabled(True)

        self.horizontalLayout_19.addWidget(self.lENumeroIBANSuministro)


        self.verticalLayout_35.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_16.addLayout(self.verticalLayout_35)

        self.line_20 = QFrame(self.gBAgregarOEditarContrato)
        self.line_20.setObjectName(u"line_20")
        self.line_20.setFrameShadow(QFrame.Shadow.Plain)
        self.line_20.setLineWidth(1)
        self.line_20.setMidLineWidth(8)
        self.line_20.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_16.addWidget(self.line_20)

        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.lblDNI_NIE_12 = QLabel(self.gBAgregarOEditarContrato)
        self.lblDNI_NIE_12.setObjectName(u"lblDNI_NIE_12")
        self.lblDNI_NIE_12.setFont(font2)

        self.verticalLayout_36.addWidget(self.lblDNI_NIE_12)

        self.lEEntidadSuministro = QLineEdit(self.gBAgregarOEditarContrato)
        self.lEEntidadSuministro.setObjectName(u"lEEntidadSuministro")
        self.lEEntidadSuministro.setFont(font4)

        self.verticalLayout_36.addWidget(self.lEEntidadSuministro)


        self.horizontalLayout_16.addLayout(self.verticalLayout_36)

        self.horizontalLayout_16.setStretch(0, 50)
        self.horizontalLayout_16.setStretch(2, 50)

        self.verticalLayout_4.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)

        self.pBCancelarCambiosEnContrato = QPushButton(self.gBAgregarOEditarContrato)
        self.pBCancelarCambiosEnContrato.setObjectName(u"pBCancelarCambiosEnContrato")
        self.pBCancelarCambiosEnContrato.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pBCancelarCambiosEnContrato)

        self.pBGuardarCambiosEnContrato = QPushButton(self.gBAgregarOEditarContrato)
        self.pBGuardarCambiosEnContrato.setObjectName(u"pBGuardarCambiosEnContrato")
        self.pBGuardarCambiosEnContrato.setEnabled(False)
        self.pBGuardarCambiosEnContrato.setFont(font3)

        self.horizontalLayout_2.addWidget(self.pBGuardarCambiosEnContrato)


        self.verticalLayout_4.addLayout(self.horizontalLayout_2)


        self.verticalLayout_38.addWidget(self.gBAgregarOEditarContrato)


        self.verticalLayout_9.addWidget(self.groupBox_3)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_10.addWidget(self.scrollArea_2)

        self.line_3 = QFrame(self.tabFichaEnergia)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setLineWidth(2)
        self.line_3.setFrameShape(QFrame.Shape.HLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_10.addWidget(self.line_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.lEUserCRM = QLineEdit(self.tabFichaEnergia)
        self.lEUserCRM.setObjectName(u"lEUserCRM")
        self.lEUserCRM.setFont(font4)

        self.horizontalLayout.addWidget(self.lEUserCRM)

        self.lEPassCRM = QLineEdit(self.tabFichaEnergia)
        self.lEPassCRM.setObjectName(u"lEPassCRM")
        self.lEPassCRM.setFont(font4)
        self.lEPassCRM.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout.addWidget(self.lEPassCRM)

        self.pBEnviarVentaACRM = QPushButton(self.tabFichaEnergia)
        self.pBEnviarVentaACRM.setObjectName(u"pBEnviarVentaACRM")
        self.pBEnviarVentaACRM.setEnabled(True)

        self.horizontalLayout.addWidget(self.pBEnviarVentaACRM)


        self.verticalLayout_10.addLayout(self.horizontalLayout)

        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(-1, 0, -1, -1)
        self.horizontalSpacer_13 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_34.addItem(self.horizontalSpacer_13)

        self.lblEstadoCopiaVenta = QLabel(self.tabFichaEnergia)
        self.lblEstadoCopiaVenta.setObjectName(u"lblEstadoCopiaVenta")
        palette3 = QPalette()
        brush10 = QBrush(QColor(255, 0, 0, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush10)
        self.lblEstadoCopiaVenta.setPalette(palette3)
        self.lblEstadoCopiaVenta.setFont(font6)

        self.horizontalLayout_34.addWidget(self.lblEstadoCopiaVenta)


        self.verticalLayout_10.addLayout(self.horizontalLayout_34)


        self.horizontalLayout_7.addLayout(self.verticalLayout_10)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_7.setStretch(0, 10)
        self.horizontalLayout_7.setStretch(1, 80)
        self.horizontalLayout_7.setStretch(2, 10)

        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.tabFichas.addTab(self.tabFichaEnergia, "")
        self.tabFichaTelefonia = QWidget()
        self.tabFichaTelefonia.setObjectName(u"tabFichaTelefonia")
        self.tabFichaTelefonia.setEnabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.tabFichaTelefonia)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_9)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, -1, -1, 0)
        self.lblTitulo2_3 = QLabel(self.tabFichaTelefonia)
        self.lblTitulo2_3.setObjectName(u"lblTitulo2_3")
        self.lblTitulo2_3.setFont(font1)
        self.lblTitulo2_3.setMargin(0)

        self.verticalLayout_11.addWidget(self.lblTitulo2_3)

        self.line_2 = QFrame(self.tabFichaTelefonia)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QFrame.Shape.HLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_2)

        self.scrollArea_3 = QScrollArea(self.tabFichaTelefonia)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setFrameShape(QFrame.Shape.NoFrame)
        self.scrollArea_3.setMidLineWidth(0)
        self.scrollArea_3.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.scrollArea_3.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 736, 987))
        self.verticalLayout_12 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.gBDatosGeneralesCliente_2 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.gBDatosGeneralesCliente_2.setObjectName(u"gBDatosGeneralesCliente_2")
        self.gBDatosGeneralesCliente_2.setMinimumSize(QSize(0, 0))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush9)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush9)
        self.gBDatosGeneralesCliente_2.setPalette(palette4)
        self.gBDatosGeneralesCliente_2.setFont(font1)
        self.verticalLayout_5 = QVBoxLayout(self.gBDatosGeneralesCliente_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.qLNombreCliente_2 = QLabel(self.gBDatosGeneralesCliente_2)
        self.qLNombreCliente_2.setObjectName(u"qLNombreCliente_2")
        self.qLNombreCliente_2.setFont(font2)

        self.verticalLayout_37.addWidget(self.qLNombreCliente_2)

        self.lENombreCliente_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lENombreCliente_2.setObjectName(u"lENombreCliente_2")
        self.lENombreCliente_2.setFont(font3)

        self.verticalLayout_37.addWidget(self.lENombreCliente_2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_37)

        self.line_10 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_10.setObjectName(u"line_10")
        self.line_10.setFrameShadow(QFrame.Shadow.Plain)
        self.line_10.setLineWidth(1)
        self.line_10.setMidLineWidth(8)
        self.line_10.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_21.addWidget(self.line_10)

        self.verticalLayout_39 = QVBoxLayout()
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.lblDNI_NIE_6 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblDNI_NIE_6.setObjectName(u"lblDNI_NIE_6")
        self.lblDNI_NIE_6.setFont(font2)

        self.verticalLayout_39.addWidget(self.lblDNI_NIE_6)

        self.lEDNI_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lEDNI_2.setObjectName(u"lEDNI_2")
        self.lEDNI_2.setFont(font3)
        self.lEDNI_2.setMaxLength(9)

        self.verticalLayout_39.addWidget(self.lEDNI_2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_39)

        self.line_21 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_21.setObjectName(u"line_21")
        self.line_21.setFrameShadow(QFrame.Shadow.Plain)
        self.line_21.setLineWidth(1)
        self.line_21.setMidLineWidth(8)
        self.line_21.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_21.addWidget(self.line_21)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.lblDNI_NIE_7 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblDNI_NIE_7.setObjectName(u"lblDNI_NIE_7")
        self.lblDNI_NIE_7.setFont(font2)

        self.verticalLayout_40.addWidget(self.lblDNI_NIE_7)

        self.lECodigoPostal_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lECodigoPostal_2.setObjectName(u"lECodigoPostal_2")
        self.lECodigoPostal_2.setFont(font3)
        self.lECodigoPostal_2.setClearButtonEnabled(True)

        self.verticalLayout_40.addWidget(self.lECodigoPostal_2)


        self.horizontalLayout_21.addLayout(self.verticalLayout_40)

        self.horizontalLayout_21.setStretch(0, 60)
        self.horizontalLayout_21.setStretch(2, 20)
        self.horizontalLayout_21.setStretch(4, 20)

        self.verticalLayout_5.addLayout(self.horizontalLayout_21)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.horizontalLayout_22.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_41 = QVBoxLayout()
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_19 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_19.setObjectName(u"lblProvincia_19")
        self.lblProvincia_19.setFont(font2)

        self.verticalLayout_41.addWidget(self.lblProvincia_19)

        self.cmbProvincia_2 = QComboBox(self.gBDatosGeneralesCliente_2)
        self.cmbProvincia_2.setObjectName(u"cmbProvincia_2")
        self.cmbProvincia_2.setMaximumSize(QSize(16777215, 16777215))
        self.cmbProvincia_2.setFont(font3)
        self.cmbProvincia_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_41.addWidget(self.cmbProvincia_2)


        self.horizontalLayout_22.addLayout(self.verticalLayout_41)

        self.line_22 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_22.setObjectName(u"line_22")
        self.line_22.setFrameShadow(QFrame.Shadow.Plain)
        self.line_22.setLineWidth(1)
        self.line_22.setMidLineWidth(8)
        self.line_22.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_22.addWidget(self.line_22)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_20 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_20.setObjectName(u"lblProvincia_20")
        self.lblProvincia_20.setFont(font2)

        self.verticalLayout_44.addWidget(self.lblProvincia_20)

        self.lEMunicipio_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lEMunicipio_2.setObjectName(u"lEMunicipio_2")
        self.lEMunicipio_2.setFont(font3)

        self.verticalLayout_44.addWidget(self.lEMunicipio_2)


        self.horizontalLayout_22.addLayout(self.verticalLayout_44)

        self.horizontalLayout_22.setStretch(0, 50)
        self.horizontalLayout_22.setStretch(2, 50)

        self.verticalLayout_5.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_21 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_21.setObjectName(u"lblProvincia_21")
        self.lblProvincia_21.setFont(font2)

        self.verticalLayout_45.addWidget(self.lblProvincia_21)

        self.lENombreCalle_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lENombreCalle_2.setObjectName(u"lENombreCalle_2")
        self.lENombreCalle_2.setFont(font3)

        self.verticalLayout_45.addWidget(self.lENombreCalle_2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_45)

        self.line_23 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_23.setObjectName(u"line_23")
        self.line_23.setFrameShadow(QFrame.Shadow.Plain)
        self.line_23.setLineWidth(1)
        self.line_23.setMidLineWidth(8)
        self.line_23.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_23.addWidget(self.line_23)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_22 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_22.setObjectName(u"lblProvincia_22")
        self.lblProvincia_22.setFont(font2)

        self.verticalLayout_46.addWidget(self.lblProvincia_22)

        self.sBNumeroDeLaCalle_2 = QSpinBox(self.gBDatosGeneralesCliente_2)
        self.sBNumeroDeLaCalle_2.setObjectName(u"sBNumeroDeLaCalle_2")
        self.sBNumeroDeLaCalle_2.setFont(font3)
        self.sBNumeroDeLaCalle_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.sBNumeroDeLaCalle_2.setInputMethodHints(Qt.InputMethodHint.ImhDigitsOnly)
        self.sBNumeroDeLaCalle_2.setFrame(True)
        self.sBNumeroDeLaCalle_2.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.UpDownArrows)
        self.sBNumeroDeLaCalle_2.setKeyboardTracking(True)
        self.sBNumeroDeLaCalle_2.setMaximum(999)
        self.sBNumeroDeLaCalle_2.setStepType(QAbstractSpinBox.StepType.DefaultStepType)

        self.verticalLayout_46.addWidget(self.sBNumeroDeLaCalle_2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_46)

        self.line_24 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_24.setObjectName(u"line_24")
        self.line_24.setFrameShadow(QFrame.Shadow.Plain)
        self.line_24.setLineWidth(1)
        self.line_24.setMidLineWidth(8)
        self.line_24.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_23.addWidget(self.line_24)

        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_23 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_23.setObjectName(u"lblProvincia_23")
        self.lblProvincia_23.setFont(font2)

        self.verticalLayout_48.addWidget(self.lblProvincia_23)

        self.lEPisoYLetra_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lEPisoYLetra_2.setObjectName(u"lEPisoYLetra_2")
        self.lEPisoYLetra_2.setFont(font3)

        self.verticalLayout_48.addWidget(self.lEPisoYLetra_2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_48)

        self.line_25 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_25.setObjectName(u"line_25")
        self.line_25.setFrameShadow(QFrame.Shadow.Plain)
        self.line_25.setLineWidth(1)
        self.line_25.setMidLineWidth(8)
        self.line_25.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_23.addWidget(self.line_25)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.verticalLayout_49.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_24 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_24.setObjectName(u"lblProvincia_24")
        self.lblProvincia_24.setFont(font2)

        self.verticalLayout_49.addWidget(self.lblProvincia_24)

        self.lEBloqueOEscalera_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lEBloqueOEscalera_2.setObjectName(u"lEBloqueOEscalera_2")
        self.lEBloqueOEscalera_2.setFont(font3)

        self.verticalLayout_49.addWidget(self.lEBloqueOEscalera_2)


        self.horizontalLayout_23.addLayout(self.verticalLayout_49)

        self.horizontalLayout_23.setStretch(0, 40)

        self.verticalLayout_5.addLayout(self.horizontalLayout_23)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_50.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_25 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_25.setObjectName(u"lblProvincia_25")
        self.lblProvincia_25.setFont(font2)

        self.verticalLayout_50.addWidget(self.lblProvincia_25)

        self.lECUPS_Luz_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lECUPS_Luz_2.setObjectName(u"lECUPS_Luz_2")
        self.lECUPS_Luz_2.setFont(font3)

        self.verticalLayout_50.addWidget(self.lECUPS_Luz_2)


        self.horizontalLayout_24.addLayout(self.verticalLayout_50)

        self.line_26 = QFrame(self.gBDatosGeneralesCliente_2)
        self.line_26.setObjectName(u"line_26")
        self.line_26.setFrameShadow(QFrame.Shadow.Plain)
        self.line_26.setLineWidth(1)
        self.line_26.setMidLineWidth(8)
        self.line_26.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_24.addWidget(self.line_26)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.verticalLayout_51.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_26 = QLabel(self.gBDatosGeneralesCliente_2)
        self.lblProvincia_26.setObjectName(u"lblProvincia_26")
        self.lblProvincia_26.setFont(font2)

        self.verticalLayout_51.addWidget(self.lblProvincia_26)

        self.lECUPS_Gas_2 = QLineEdit(self.gBDatosGeneralesCliente_2)
        self.lECUPS_Gas_2.setObjectName(u"lECUPS_Gas_2")
        self.lECUPS_Gas_2.setFont(font3)

        self.verticalLayout_51.addWidget(self.lECUPS_Gas_2)


        self.horizontalLayout_24.addLayout(self.verticalLayout_51)

        self.horizontalLayout_24.setStretch(0, 50)
        self.horizontalLayout_24.setStretch(2, 50)

        self.verticalLayout_5.addLayout(self.horizontalLayout_24)


        self.verticalLayout_12.addWidget(self.gBDatosGeneralesCliente_2)

        self.groupBox_4 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setMinimumSize(QSize(0, 0))
        self.groupBox_4.setFont(font1)
        self.verticalLayout_52 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.lblDNI_NIE_13 = QLabel(self.groupBox_4)
        self.lblDNI_NIE_13.setObjectName(u"lblDNI_NIE_13")
        self.lblDNI_NIE_13.setFont(font2)

        self.verticalLayout_53.addWidget(self.lblDNI_NIE_13)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.lENumeroIBAN_2 = QLineEdit(self.groupBox_4)
        self.lENumeroIBAN_2.setObjectName(u"lENumeroIBAN_2")
        self.lENumeroIBAN_2.setFont(font2)
        self.lENumeroIBAN_2.setMouseTracking(False)
        self.lENumeroIBAN_2.setMaxLength(28)
        self.lENumeroIBAN_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lENumeroIBAN_2.setCursorPosition(0)
        self.lENumeroIBAN_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lENumeroIBAN_2.setClearButtonEnabled(True)

        self.horizontalLayout_26.addWidget(self.lENumeroIBAN_2)


        self.verticalLayout_53.addLayout(self.horizontalLayout_26)


        self.horizontalLayout_25.addLayout(self.verticalLayout_53)

        self.line_27 = QFrame(self.groupBox_4)
        self.line_27.setObjectName(u"line_27")
        self.line_27.setFrameShadow(QFrame.Shadow.Plain)
        self.line_27.setLineWidth(1)
        self.line_27.setMidLineWidth(8)
        self.line_27.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_25.addWidget(self.line_27)

        self.verticalLayout_54 = QVBoxLayout()
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.lblDNI_NIE_14 = QLabel(self.groupBox_4)
        self.lblDNI_NIE_14.setObjectName(u"lblDNI_NIE_14")
        self.lblDNI_NIE_14.setFont(font2)

        self.verticalLayout_54.addWidget(self.lblDNI_NIE_14)

        self.lEEntidad_2 = QLineEdit(self.groupBox_4)
        self.lEEntidad_2.setObjectName(u"lEEntidad_2")
        self.lEEntidad_2.setFont(font4)

        self.verticalLayout_54.addWidget(self.lEEntidad_2)


        self.horizontalLayout_25.addLayout(self.verticalLayout_54)

        self.horizontalLayout_25.setStretch(0, 50)
        self.horizontalLayout_25.setStretch(2, 50)

        self.verticalLayout_52.addLayout(self.horizontalLayout_25)


        self.verticalLayout_12.addWidget(self.groupBox_4)

        self.groupBox_5 = QGroupBox(self.scrollAreaWidgetContents_3)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setMinimumSize(QSize(0, 0))
        self.groupBox_5.setFont(font1)
        self.verticalLayout_55 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.tWContratos_2 = QTableWidget(self.groupBox_5)
        if (self.tWContratos_2.columnCount() < 13):
            self.tWContratos_2.setColumnCount(13)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(0, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(1, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(2, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(3, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(4, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(5, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(6, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(7, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(8, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(9, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(10, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(11, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font5);
        self.tWContratos_2.setHorizontalHeaderItem(12, __qtablewidgetitem25)
        self.tWContratos_2.setObjectName(u"tWContratos_2")
        self.tWContratos_2.setMinimumSize(QSize(0, 200))
        self.tWContratos_2.setFont(font3)
        self.tWContratos_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tWContratos_2.setAlternatingRowColors(True)
        self.tWContratos_2.setSelectionMode(QAbstractItemView.SelectionMode.SingleSelection)
        self.tWContratos_2.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tWContratos_2.setShowGrid(True)
        self.tWContratos_2.setSortingEnabled(False)
        self.tWContratos_2.setCornerButtonEnabled(True)
        self.tWContratos_2.setRowCount(0)
        self.tWContratos_2.horizontalHeader().setVisible(True)
        self.tWContratos_2.horizontalHeader().setCascadingSectionResizes(True)
        self.tWContratos_2.horizontalHeader().setMinimumSectionSize(50)
        self.tWContratos_2.horizontalHeader().setHighlightSections(True)
        self.tWContratos_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tWContratos_2.horizontalHeader().setStretchLastSection(True)
        self.tWContratos_2.verticalHeader().setVisible(True)
        self.tWContratos_2.verticalHeader().setHighlightSections(False)
        self.tWContratos_2.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_55.addWidget(self.tWContratos_2)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.horizontalLayout_27.setContentsMargins(-1, -1, -1, 10)
        self.pBEliminarContrato_2 = QPushButton(self.groupBox_5)
        self.pBEliminarContrato_2.setObjectName(u"pBEliminarContrato_2")
        self.pBEliminarContrato_2.setEnabled(False)
        self.pBEliminarContrato_2.setFont(font6)

        self.horizontalLayout_27.addWidget(self.pBEliminarContrato_2)

        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_10)

        self.pBEditarContrato_2 = QPushButton(self.groupBox_5)
        self.pBEditarContrato_2.setObjectName(u"pBEditarContrato_2")
        self.pBEditarContrato_2.setEnabled(False)
        self.pBEditarContrato_2.setFont(font6)

        self.horizontalLayout_27.addWidget(self.pBEditarContrato_2)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_27.addItem(self.horizontalSpacer_4)

        self.pBAgregarContrato_2 = QPushButton(self.groupBox_5)
        self.pBAgregarContrato_2.setObjectName(u"pBAgregarContrato_2")
        self.pBAgregarContrato_2.setEnabled(True)
        self.pBAgregarContrato_2.setFont(font6)

        self.horizontalLayout_27.addWidget(self.pBAgregarContrato_2)


        self.verticalLayout_55.addLayout(self.horizontalLayout_27)

        self.gBAgregarOEditarContrato_2 = QGroupBox(self.groupBox_5)
        self.gBAgregarOEditarContrato_2.setObjectName(u"gBAgregarOEditarContrato_2")
        self.gBAgregarOEditarContrato_2.setEnabled(False)
        self.verticalLayout_6 = QVBoxLayout(self.gBAgregarOEditarContrato_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.horizontalLayout_28 = QHBoxLayout()
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.lblDNI_NIE_18 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblDNI_NIE_18.setObjectName(u"lblDNI_NIE_18")
        self.lblDNI_NIE_18.setFont(font2)

        self.verticalLayout_56.addWidget(self.lblDNI_NIE_18)

        self.cmbCatalogos_2 = QComboBox(self.gBAgregarOEditarContrato_2)
        self.cmbCatalogos_2.setObjectName(u"cmbCatalogos_2")
        self.cmbCatalogos_2.setMaximumSize(QSize(16777215, 16777215))
        self.cmbCatalogos_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_56.addWidget(self.cmbCatalogos_2)


        self.horizontalLayout_28.addLayout(self.verticalLayout_56)

        self.line_28 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_28.setObjectName(u"line_28")
        self.line_28.setFrameShadow(QFrame.Shadow.Plain)
        self.line_28.setLineWidth(1)
        self.line_28.setMidLineWidth(8)
        self.line_28.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_28.addWidget(self.line_28)

        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.lblDNI_NIE_19 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblDNI_NIE_19.setObjectName(u"lblDNI_NIE_19")
        self.lblDNI_NIE_19.setFont(font2)

        self.verticalLayout_57.addWidget(self.lblDNI_NIE_19)

        self.cmbTiposContratos_2 = QComboBox(self.gBAgregarOEditarContrato_2)
        self.cmbTiposContratos_2.setObjectName(u"cmbTiposContratos_2")
        self.cmbTiposContratos_2.setMaximumSize(QSize(16777215, 16777215))
        self.cmbTiposContratos_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_57.addWidget(self.cmbTiposContratos_2)


        self.horizontalLayout_28.addLayout(self.verticalLayout_57)

        self.horizontalLayout_28.setStretch(0, 60)
        self.horizontalLayout_28.setStretch(2, 40)

        self.verticalLayout_6.addLayout(self.horizontalLayout_28)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.lblDNI_NIE_22 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblDNI_NIE_22.setObjectName(u"lblDNI_NIE_22")
        self.lblDNI_NIE_22.setFont(font2)

        self.verticalLayout_58.addWidget(self.lblDNI_NIE_22)

        self.cmbContratos_2 = QComboBox(self.gBAgregarOEditarContrato_2)
        self.cmbContratos_2.setObjectName(u"cmbContratos_2")
        self.cmbContratos_2.setMaximumSize(QSize(16777215, 16777215))
        self.cmbContratos_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_58.addWidget(self.cmbContratos_2)


        self.horizontalLayout_29.addLayout(self.verticalLayout_58)

        self.line_29 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_29.setObjectName(u"line_29")
        self.line_29.setFrameShadow(QFrame.Shadow.Plain)
        self.line_29.setLineWidth(1)
        self.line_29.setMidLineWidth(8)
        self.line_29.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_29.addWidget(self.line_29)

        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_27 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_27.setObjectName(u"lblProvincia_27")
        self.lblProvincia_27.setFont(font2)

        self.verticalLayout_59.addWidget(self.lblProvincia_27)

        self.lECUPS_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lECUPS_2.setObjectName(u"lECUPS_2")
        self.lECUPS_2.setFont(font4)

        self.verticalLayout_59.addWidget(self.lECUPS_2)


        self.horizontalLayout_29.addLayout(self.verticalLayout_59)

        self.horizontalLayout_29.setStretch(0, 40)
        self.horizontalLayout_29.setStretch(2, 60)

        self.verticalLayout_6.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.verticalLayout_60.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_28 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_28.setObjectName(u"lblProvincia_28")
        self.lblProvincia_28.setFont(font2)

        self.verticalLayout_60.addWidget(self.lblProvincia_28)

        self.cmbProvinciaSuministro_2 = QComboBox(self.gBAgregarOEditarContrato_2)
        self.cmbProvinciaSuministro_2.setObjectName(u"cmbProvinciaSuministro_2")
        self.cmbProvinciaSuministro_2.setMaximumSize(QSize(16777215, 16777215))
        self.cmbProvinciaSuministro_2.setFont(font4)
        self.cmbProvinciaSuministro_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)

        self.verticalLayout_60.addWidget(self.cmbProvinciaSuministro_2)


        self.horizontalLayout_30.addLayout(self.verticalLayout_60)

        self.line_30 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_30.setObjectName(u"line_30")
        self.line_30.setFrameShadow(QFrame.Shadow.Plain)
        self.line_30.setLineWidth(1)
        self.line_30.setMidLineWidth(8)
        self.line_30.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_30.addWidget(self.line_30)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_61.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_29 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_29.setObjectName(u"lblProvincia_29")
        self.lblProvincia_29.setFont(font2)

        self.verticalLayout_61.addWidget(self.lblProvincia_29)

        self.lEMunicipioSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lEMunicipioSuministro_2.setObjectName(u"lEMunicipioSuministro_2")
        self.lEMunicipioSuministro_2.setFont(font4)

        self.verticalLayout_61.addWidget(self.lEMunicipioSuministro_2)


        self.horizontalLayout_30.addLayout(self.verticalLayout_61)

        self.horizontalLayout_30.setStretch(0, 50)
        self.horizontalLayout_30.setStretch(2, 50)

        self.verticalLayout_6.addLayout(self.horizontalLayout_30)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(-1, -1, -1, 10)
        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.verticalLayout_62.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_30 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_30.setObjectName(u"lblProvincia_30")
        self.lblProvincia_30.setFont(font2)

        self.verticalLayout_62.addWidget(self.lblProvincia_30)

        self.lENombreCalleSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lENombreCalleSuministro_2.setObjectName(u"lENombreCalleSuministro_2")
        self.lENombreCalleSuministro_2.setFont(font4)

        self.verticalLayout_62.addWidget(self.lENombreCalleSuministro_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_62)

        self.line_31 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_31.setObjectName(u"line_31")
        self.line_31.setFrameShadow(QFrame.Shadow.Plain)
        self.line_31.setLineWidth(1)
        self.line_31.setMidLineWidth(8)
        self.line_31.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_31.addWidget(self.line_31)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_63.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_31 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_31.setObjectName(u"lblProvincia_31")
        self.lblProvincia_31.setFont(font2)

        self.verticalLayout_63.addWidget(self.lblProvincia_31)

        self.sBNumeroCalleSuministro_2 = QSpinBox(self.gBAgregarOEditarContrato_2)
        self.sBNumeroCalleSuministro_2.setObjectName(u"sBNumeroCalleSuministro_2")
        self.sBNumeroCalleSuministro_2.setFont(font4)
        self.sBNumeroCalleSuministro_2.setFocusPolicy(Qt.FocusPolicy.TabFocus)
        self.sBNumeroCalleSuministro_2.setMaximum(999)
        self.sBNumeroCalleSuministro_2.setStepType(QAbstractSpinBox.StepType.AdaptiveDecimalStepType)

        self.verticalLayout_63.addWidget(self.sBNumeroCalleSuministro_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_63)

        self.line_32 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_32.setObjectName(u"line_32")
        self.line_32.setFrameShadow(QFrame.Shadow.Plain)
        self.line_32.setLineWidth(1)
        self.line_32.setMidLineWidth(8)
        self.line_32.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_31.addWidget(self.line_32)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.verticalLayout_64.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_32 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_32.setObjectName(u"lblProvincia_32")
        self.lblProvincia_32.setFont(font2)

        self.verticalLayout_64.addWidget(self.lblProvincia_32)

        self.lEPisoYLetraSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lEPisoYLetraSuministro_2.setObjectName(u"lEPisoYLetraSuministro_2")
        self.lEPisoYLetraSuministro_2.setFont(font4)

        self.verticalLayout_64.addWidget(self.lEPisoYLetraSuministro_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_64)

        self.line_33 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_33.setObjectName(u"line_33")
        self.line_33.setFrameShadow(QFrame.Shadow.Plain)
        self.line_33.setLineWidth(1)
        self.line_33.setMidLineWidth(8)
        self.line_33.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_31.addWidget(self.line_33)

        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_65.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_33 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_33.setObjectName(u"lblProvincia_33")
        self.lblProvincia_33.setFont(font2)

        self.verticalLayout_65.addWidget(self.lblProvincia_33)

        self.lEBloqueEscaleraSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lEBloqueEscaleraSuministro_2.setObjectName(u"lEBloqueEscaleraSuministro_2")
        self.lEBloqueEscaleraSuministro_2.setFont(font4)

        self.verticalLayout_65.addWidget(self.lEBloqueEscaleraSuministro_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_65)

        self.line_34 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_34.setObjectName(u"line_34")
        self.line_34.setFrameShadow(QFrame.Shadow.Plain)
        self.line_34.setLineWidth(1)
        self.line_34.setMidLineWidth(8)
        self.line_34.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_31.addWidget(self.line_34)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.verticalLayout_66.setContentsMargins(-1, -1, -1, 0)
        self.lblProvincia_34 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblProvincia_34.setObjectName(u"lblProvincia_34")
        self.lblProvincia_34.setFont(font2)

        self.verticalLayout_66.addWidget(self.lblProvincia_34)

        self.lECodigoPostalSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lECodigoPostalSuministro_2.setObjectName(u"lECodigoPostalSuministro_2")
        self.lECodigoPostalSuministro_2.setFont(font3)
        self.lECodigoPostalSuministro_2.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.lECodigoPostalSuministro_2.setClearButtonEnabled(True)

        self.verticalLayout_66.addWidget(self.lECodigoPostalSuministro_2)


        self.horizontalLayout_31.addLayout(self.verticalLayout_66)

        self.horizontalLayout_31.setStretch(0, 40)

        self.verticalLayout_6.addLayout(self.horizontalLayout_31)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.lblDNI_NIE_15 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblDNI_NIE_15.setObjectName(u"lblDNI_NIE_15")
        self.lblDNI_NIE_15.setFont(font2)

        self.verticalLayout_67.addWidget(self.lblDNI_NIE_15)

        self.horizontalLayout_33 = QHBoxLayout()
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lENumeroIBANSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lENumeroIBANSuministro_2.setObjectName(u"lENumeroIBANSuministro_2")
        self.lENumeroIBANSuministro_2.setFont(font2)
        self.lENumeroIBANSuministro_2.setMouseTracking(False)
        self.lENumeroIBANSuministro_2.setMaxLength(28)
        self.lENumeroIBANSuministro_2.setEchoMode(QLineEdit.EchoMode.Normal)
        self.lENumeroIBANSuministro_2.setCursorPosition(0)
        self.lENumeroIBANSuministro_2.setCursorMoveStyle(Qt.CursorMoveStyle.LogicalMoveStyle)
        self.lENumeroIBANSuministro_2.setClearButtonEnabled(True)

        self.horizontalLayout_33.addWidget(self.lENumeroIBANSuministro_2)


        self.verticalLayout_67.addLayout(self.horizontalLayout_33)


        self.horizontalLayout_32.addLayout(self.verticalLayout_67)

        self.line_35 = QFrame(self.gBAgregarOEditarContrato_2)
        self.line_35.setObjectName(u"line_35")
        self.line_35.setFrameShadow(QFrame.Shadow.Plain)
        self.line_35.setLineWidth(1)
        self.line_35.setMidLineWidth(8)
        self.line_35.setFrameShape(QFrame.Shape.VLine)

        self.horizontalLayout_32.addWidget(self.line_35)

        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.lblDNI_NIE_20 = QLabel(self.gBAgregarOEditarContrato_2)
        self.lblDNI_NIE_20.setObjectName(u"lblDNI_NIE_20")
        self.lblDNI_NIE_20.setFont(font2)

        self.verticalLayout_68.addWidget(self.lblDNI_NIE_20)

        self.lEEntidadSuministro_2 = QLineEdit(self.gBAgregarOEditarContrato_2)
        self.lEEntidadSuministro_2.setObjectName(u"lEEntidadSuministro_2")
        self.lEEntidadSuministro_2.setFont(font4)

        self.verticalLayout_68.addWidget(self.lEEntidadSuministro_2)


        self.horizontalLayout_32.addLayout(self.verticalLayout_68)

        self.horizontalLayout_32.setStretch(0, 50)
        self.horizontalLayout_32.setStretch(2, 50)

        self.verticalLayout_6.addLayout(self.horizontalLayout_32)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_5)

        self.pBCancelarCambiosEnContrato_2 = QPushButton(self.gBAgregarOEditarContrato_2)
        self.pBCancelarCambiosEnContrato_2.setObjectName(u"pBCancelarCambiosEnContrato_2")
        self.pBCancelarCambiosEnContrato_2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pBCancelarCambiosEnContrato_2)

        self.pBGuardarCambiosEnContrato_2 = QPushButton(self.gBAgregarOEditarContrato_2)
        self.pBGuardarCambiosEnContrato_2.setObjectName(u"pBGuardarCambiosEnContrato_2")
        self.pBGuardarCambiosEnContrato_2.setEnabled(False)
        self.pBGuardarCambiosEnContrato_2.setFont(font3)

        self.horizontalLayout_3.addWidget(self.pBGuardarCambiosEnContrato_2)


        self.verticalLayout_6.addLayout(self.horizontalLayout_3)


        self.verticalLayout_55.addWidget(self.gBAgregarOEditarContrato_2)


        self.verticalLayout_12.addWidget(self.groupBox_5)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_11.addWidget(self.scrollArea_3)

        self.line_36 = QFrame(self.tabFichaTelefonia)
        self.line_36.setObjectName(u"line_36")
        self.line_36.setLineWidth(2)
        self.line_36.setFrameShape(QFrame.Shape.HLine)
        self.line_36.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout_11.addWidget(self.line_36)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, -1, -1, 10)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_11)

        self.lEUserCRM_2 = QLineEdit(self.tabFichaTelefonia)
        self.lEUserCRM_2.setObjectName(u"lEUserCRM_2")
        self.lEUserCRM_2.setFont(font4)

        self.horizontalLayout_4.addWidget(self.lEUserCRM_2)

        self.lEPassCRM_2 = QLineEdit(self.tabFichaTelefonia)
        self.lEPassCRM_2.setObjectName(u"lEPassCRM_2")
        self.lEPassCRM_2.setFont(font4)
        self.lEPassCRM_2.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_4.addWidget(self.lEPassCRM_2)

        self.cBOportunidadesSeparadas_2 = QCheckBox(self.tabFichaTelefonia)
        self.cBOportunidadesSeparadas_2.setObjectName(u"cBOportunidadesSeparadas_2")
        self.cBOportunidadesSeparadas_2.setEnabled(True)
        palette5 = QPalette()
        brush11 = QBrush(QColor(23, 83, 160, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Active, QPalette.Accent, brush11)
        palette5.setBrush(QPalette.Inactive, QPalette.Accent, brush11)
        brush12 = QBrush(QColor(249, 249, 249, 77))
        brush12.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush12)
        brush13 = QBrush(QColor(0, 0, 0, 92))
        brush13.setStyle(Qt.SolidPattern)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush13)
        palette5.setBrush(QPalette.Disabled, QPalette.Accent, brush11)
        self.cBOportunidadesSeparadas_2.setPalette(palette5)
        self.cBOportunidadesSeparadas_2.setAutoExclusive(False)
        self.cBOportunidadesSeparadas_2.setTristate(False)

        self.horizontalLayout_4.addWidget(self.cBOportunidadesSeparadas_2)

        self.pBEnviarVentaACRM_2 = QPushButton(self.tabFichaTelefonia)
        self.pBEnviarVentaACRM_2.setObjectName(u"pBEnviarVentaACRM_2")
        self.pBEnviarVentaACRM_2.setEnabled(True)

        self.horizontalLayout_4.addWidget(self.pBEnviarVentaACRM_2)


        self.verticalLayout_11.addLayout(self.horizontalLayout_4)


        self.horizontalLayout_20.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_12 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_20.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_20.setStretch(0, 10)
        self.horizontalLayout_20.setStretch(1, 80)
        self.horizontalLayout_20.setStretch(2, 10)

        self.horizontalLayout_5.addLayout(self.horizontalLayout_20)

        self.tabFichas.addTab(self.tabFichaTelefonia, "")

        self.verticalLayout.addWidget(self.tabFichas)

        frmPrincipal.setCentralWidget(self.centralwidget)
#if QT_CONFIG(shortcut)
        self.lblProvincia_3.setBuddy(self.cmbProvincia)
        self.lblProvincia_4.setBuddy(self.cmbProvincia)
        self.lblProvincia_5.setBuddy(self.cmbProvincia)
        self.lblProvincia_6.setBuddy(self.cmbProvincia)
        self.lblProvincia_7.setBuddy(self.cmbProvincia)
        self.lblProvincia_8.setBuddy(self.cmbProvincia)
        self.lblProvincia_16.setBuddy(self.cmbProvincia)
        self.lblProvincia_17.setBuddy(self.cmbProvincia)
        self.lblProvincia_15.setBuddy(self.cmbProvincia)
        self.lblProvincia_13.setBuddy(self.cmbProvincia)
        self.lblProvincia_14.setBuddy(self.cmbProvincia)
        self.lblProvincia_9.setBuddy(self.cmbProvincia)
        self.lblProvincia_10.setBuddy(self.cmbProvincia)
        self.lblProvincia_11.setBuddy(self.cmbProvincia)
        self.lblProvincia_12.setBuddy(self.cmbProvincia)
        self.lblProvincia_18.setBuddy(self.cmbProvincia)
        self.lblProvincia_19.setBuddy(self.cmbProvincia)
        self.lblProvincia_20.setBuddy(self.cmbProvincia)
        self.lblProvincia_21.setBuddy(self.cmbProvincia)
        self.lblProvincia_22.setBuddy(self.cmbProvincia)
        self.lblProvincia_23.setBuddy(self.cmbProvincia)
        self.lblProvincia_24.setBuddy(self.cmbProvincia)
        self.lblProvincia_25.setBuddy(self.cmbProvincia)
        self.lblProvincia_26.setBuddy(self.cmbProvincia)
        self.lblProvincia_27.setBuddy(self.cmbProvincia)
        self.lblProvincia_28.setBuddy(self.cmbProvincia)
        self.lblProvincia_29.setBuddy(self.cmbProvincia)
        self.lblProvincia_30.setBuddy(self.cmbProvincia)
        self.lblProvincia_31.setBuddy(self.cmbProvincia)
        self.lblProvincia_32.setBuddy(self.cmbProvincia)
        self.lblProvincia_33.setBuddy(self.cmbProvincia)
        self.lblProvincia_34.setBuddy(self.cmbProvincia)
#endif // QT_CONFIG(shortcut)
        QWidget.setTabOrder(self.lENombreCliente, self.lEDNI)
        QWidget.setTabOrder(self.lEDNI, self.lECodigoPostal)
        QWidget.setTabOrder(self.lECodigoPostal, self.cmbProvincia)
        QWidget.setTabOrder(self.cmbProvincia, self.lEMunicipio)
        QWidget.setTabOrder(self.lEMunicipio, self.lENombreCalle)
        QWidget.setTabOrder(self.lENombreCalle, self.sBNumeroDeLaCalle)
        QWidget.setTabOrder(self.sBNumeroDeLaCalle, self.lEPisoYLetra)
        QWidget.setTabOrder(self.lEPisoYLetra, self.lEBloqueOEscalera)
        QWidget.setTabOrder(self.lEBloqueOEscalera, self.lECUPS_Luz)
        QWidget.setTabOrder(self.lECUPS_Luz, self.lECUPS_Gas)
        QWidget.setTabOrder(self.lECUPS_Gas, self.lENumeroIBAN)
        QWidget.setTabOrder(self.lENumeroIBAN, self.lEEntidad)
        QWidget.setTabOrder(self.lEEntidad, self.tWContratos)
        QWidget.setTabOrder(self.tWContratos, self.pBEliminarContrato)
        QWidget.setTabOrder(self.pBEliminarContrato, self.pBEditarContrato)
        QWidget.setTabOrder(self.pBEditarContrato, self.pBAgregarContrato)
        QWidget.setTabOrder(self.pBAgregarContrato, self.cmbCatalogos)
        QWidget.setTabOrder(self.cmbCatalogos, self.cmbTiposContratos)
        QWidget.setTabOrder(self.cmbTiposContratos, self.cmbContratos)
        QWidget.setTabOrder(self.cmbContratos, self.lECUPS)
        QWidget.setTabOrder(self.lECUPS, self.cmbProvinciaSuministro)
        QWidget.setTabOrder(self.cmbProvinciaSuministro, self.lEMunicipioSuministro)
        QWidget.setTabOrder(self.lEMunicipioSuministro, self.lENombreCalleSuministro)
        QWidget.setTabOrder(self.lENombreCalleSuministro, self.sBNumeroCalleSuministro)
        QWidget.setTabOrder(self.sBNumeroCalleSuministro, self.lEPisoYLetraSuministro)
        QWidget.setTabOrder(self.lEPisoYLetraSuministro, self.lEBloqueEscaleraSuministro)
        QWidget.setTabOrder(self.lEBloqueEscaleraSuministro, self.lECodigoPostalSuministro)
        QWidget.setTabOrder(self.lECodigoPostalSuministro, self.lENumeroIBANSuministro)
        QWidget.setTabOrder(self.lENumeroIBANSuministro, self.lEEntidadSuministro)
        QWidget.setTabOrder(self.lEEntidadSuministro, self.tabFichas)
        QWidget.setTabOrder(self.tabFichas, self.pBCancelarCambiosEnContrato)
        QWidget.setTabOrder(self.pBCancelarCambiosEnContrato, self.pBGuardarCambiosEnContrato)
        QWidget.setTabOrder(self.pBGuardarCambiosEnContrato, self.lEUserCRM)
        QWidget.setTabOrder(self.lEUserCRM, self.lEPassCRM)
        QWidget.setTabOrder(self.lEPassCRM, self.pBEnviarVentaACRM)
        QWidget.setTabOrder(self.pBEnviarVentaACRM, self.scrollArea_2)

        self.retranslateUi(frmPrincipal)

        self.tabFichas.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(frmPrincipal)
    # setupUi

    def retranslateUi(self, frmPrincipal):
        frmPrincipal.setWindowTitle(QCoreApplication.translate("frmPrincipal", u"RSCTEL Agent", None))
        self.lblTitulo2_2.setText(QCoreApplication.translate("frmPrincipal", u"Toma de Datos:", None))
        self.gBDatosGeneralesCliente.setTitle(QCoreApplication.translate("frmPrincipal", u"DATOS GENERALES DEL CLIENTE", None))
        self.qLNombreCliente.setText(QCoreApplication.translate("frmPrincipal", u"1.NOMBRE DEL CLIENTE", None))
        self.lblDNI_NIE_4.setText(QCoreApplication.translate("frmPrincipal", u"2.DNI O NIE", None))
        self.lblDNI_NIE_5.setText(QCoreApplication.translate("frmPrincipal", u"3.CODIGO POSTAL", None))
        self.lECodigoPostal.setInputMask(QCoreApplication.translate("frmPrincipal", u"99999", None))
        self.lblProvincia_3.setText(QCoreApplication.translate("frmPrincipal", u"4.PROVINCIA", None))
        self.lblProvincia_4.setText(QCoreApplication.translate("frmPrincipal", u"5.MUNICIPIO", None))
        self.lblProvincia_5.setText(QCoreApplication.translate("frmPrincipal", u"6.NOMBRE DE LA CALLE", None))
        self.lblProvincia_6.setText(QCoreApplication.translate("frmPrincipal", u"7.NO. DE CALLE", None))
        self.sBNumeroDeLaCalle.setSpecialValueText(QCoreApplication.translate("frmPrincipal", u"S/N", None))
        self.lblProvincia_7.setText(QCoreApplication.translate("frmPrincipal", u"8.PISO/LETRA", None))
        self.lblProvincia_8.setText(QCoreApplication.translate("frmPrincipal", u"9.BLOQ./ESC.", None))
        self.lblProvincia_16.setText(QCoreApplication.translate("frmPrincipal", u"10.CUPS LUZ", None))
        self.lblProvincia_17.setText(QCoreApplication.translate("frmPrincipal", u"11.CUPS GAS", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("frmPrincipal", u"DATOS BANCARIOS", None))
        self.lblDNI_NIE_9.setText(QCoreApplication.translate("frmPrincipal", u"12.NUMERO DE IBAN", None))
        self.lENumeroIBAN.setInputMask(QCoreApplication.translate("frmPrincipal", u"ES99 9999 9999 99 9999999999", None))
        self.lENumeroIBAN.setText(QCoreApplication.translate("frmPrincipal", u"ES    ", None))
        self.lblDNI_NIE_10.setText(QCoreApplication.translate("frmPrincipal", u"13.ENTIDAD", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("frmPrincipal", u"PRODUCTOS VENDIDOS", None))
        ___qtablewidgetitem = self.tWContratos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("frmPrincipal", u"Catalogo", None));
        ___qtablewidgetitem1 = self.tWContratos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("frmPrincipal", u"Tipo de Contrato", None));
        ___qtablewidgetitem2 = self.tWContratos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("frmPrincipal", u"Contrato", None));
        ___qtablewidgetitem3 = self.tWContratos.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("frmPrincipal", u"CUPS", None));
        ___qtablewidgetitem4 = self.tWContratos.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("frmPrincipal", u"Provincia", None));
        ___qtablewidgetitem5 = self.tWContratos.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("frmPrincipal", u"Municipio", None));
        ___qtablewidgetitem6 = self.tWContratos.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("frmPrincipal", u"Nombre de la Calle", None));
        ___qtablewidgetitem7 = self.tWContratos.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("frmPrincipal", u"No Calle", None));
        ___qtablewidgetitem8 = self.tWContratos.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("frmPrincipal", u"Piso/Letra", None));
        ___qtablewidgetitem9 = self.tWContratos.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("frmPrincipal", u"Bloq./Esc.", None));
        ___qtablewidgetitem10 = self.tWContratos.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("frmPrincipal", u"Cod. Postal", None));
        ___qtablewidgetitem11 = self.tWContratos.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("frmPrincipal", u"Entidad Bancaria", None));
        ___qtablewidgetitem12 = self.tWContratos.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("frmPrincipal", u"IBAN", None));
        self.pBEliminarContrato.setText(QCoreApplication.translate("frmPrincipal", u"Eliminar Contrato", None))
        self.pBEditarContrato.setText(QCoreApplication.translate("frmPrincipal", u"Editar Contrato", None))
        self.pBAgregarContrato.setText(QCoreApplication.translate("frmPrincipal", u"Agregar Nuevo Contrato", None))
        self.gBAgregarOEditarContrato.setTitle(QCoreApplication.translate("frmPrincipal", u"Agregar o Editar Contrato", None))
        self.lblDNI_NIE_16.setText(QCoreApplication.translate("frmPrincipal", u"1.CATALOGO DE VENTA", None))
#if QT_CONFIG(tooltip)
        self.cmbCatalogos.setToolTip(QCoreApplication.translate("frmPrincipal", u"\u00bfQue compa\u00f1ia haz vendido?", None))
#endif // QT_CONFIG(tooltip)
        self.lblDNI_NIE_17.setText(QCoreApplication.translate("frmPrincipal", u"2.TIPO DE CONTRATO", None))
        self.lblDNI_NIE_21.setText(QCoreApplication.translate("frmPrincipal", u"3.CONTRATO", None))
        self.lblProvincia_15.setText(QCoreApplication.translate("frmPrincipal", u"4.CUPS", None))
        self.lblProvincia_13.setText(QCoreApplication.translate("frmPrincipal", u"5.PROVINCIA", None))
        self.lblProvincia_14.setText(QCoreApplication.translate("frmPrincipal", u"6.MUNICIPIO", None))
        self.lblProvincia_9.setText(QCoreApplication.translate("frmPrincipal", u"7.NOMBRE DE LA CALLE", None))
        self.lblProvincia_10.setText(QCoreApplication.translate("frmPrincipal", u"8.NUMERO DE LA CALLE", None))
        self.sBNumeroCalleSuministro.setSpecialValueText(QCoreApplication.translate("frmPrincipal", u"S/N", None))
        self.lblProvincia_11.setText(QCoreApplication.translate("frmPrincipal", u"9.PISO Y LETRA", None))
        self.lblProvincia_12.setText(QCoreApplication.translate("frmPrincipal", u"10.BLOQ./ESC.", None))
        self.lblProvincia_18.setText(QCoreApplication.translate("frmPrincipal", u"11.CODIGO POSTAL", None))
        self.lECodigoPostalSuministro.setInputMask(QCoreApplication.translate("frmPrincipal", u"99999", None))
        self.lblDNI_NIE_11.setText(QCoreApplication.translate("frmPrincipal", u"12.NUMERO DE IBAN", None))
        self.lENumeroIBANSuministro.setInputMask(QCoreApplication.translate("frmPrincipal", u"ES99 9999 9999 99 9999999999", None))
        self.lENumeroIBANSuministro.setText(QCoreApplication.translate("frmPrincipal", u"ES    ", None))
        self.lblDNI_NIE_12.setText(QCoreApplication.translate("frmPrincipal", u"13.ENTIDAD BANCARIA", None))
        self.pBCancelarCambiosEnContrato.setText(QCoreApplication.translate("frmPrincipal", u"Cancelar Cambios", None))
        self.pBGuardarCambiosEnContrato.setText(QCoreApplication.translate("frmPrincipal", u"Guardar Cambios", None))
        self.lEUserCRM.setPlaceholderText(QCoreApplication.translate("frmPrincipal", u"Usuario para CRM", None))
        self.lEPassCRM.setPlaceholderText(QCoreApplication.translate("frmPrincipal", u"Contrase\u00f1a para CRM", None))
        self.pBEnviarVentaACRM.setText(QCoreApplication.translate("frmPrincipal", u"ENVIAR A CRM", None))
        self.lblEstadoCopiaVenta.setText(QCoreApplication.translate("frmPrincipal", u"Estado venta", None))
        self.tabFichas.setTabText(self.tabFichas.indexOf(self.tabFichaEnergia), QCoreApplication.translate("frmPrincipal", u"Energia", None))
        self.lblTitulo2_3.setText(QCoreApplication.translate("frmPrincipal", u"Toma de Datos:", None))
        self.gBDatosGeneralesCliente_2.setTitle(QCoreApplication.translate("frmPrincipal", u"DATOS GENERALES DEL CLIENTE", None))
        self.qLNombreCliente_2.setText(QCoreApplication.translate("frmPrincipal", u"1.NOMBRE DEL CLIENTE", None))
        self.lblDNI_NIE_6.setText(QCoreApplication.translate("frmPrincipal", u"2.DNI O NIE", None))
        self.lblDNI_NIE_7.setText(QCoreApplication.translate("frmPrincipal", u"3.CODIGO POSTAL", None))
        self.lECodigoPostal_2.setInputMask(QCoreApplication.translate("frmPrincipal", u"99999", None))
        self.lblProvincia_19.setText(QCoreApplication.translate("frmPrincipal", u"4.PROVINCIA", None))
        self.lblProvincia_20.setText(QCoreApplication.translate("frmPrincipal", u"5.MUNICIPIO", None))
        self.lblProvincia_21.setText(QCoreApplication.translate("frmPrincipal", u"6.NOMBRE DE LA CALLE", None))
        self.lblProvincia_22.setText(QCoreApplication.translate("frmPrincipal", u"7.NO. DE CALLE", None))
        self.sBNumeroDeLaCalle_2.setSpecialValueText(QCoreApplication.translate("frmPrincipal", u"S/N", None))
        self.lblProvincia_23.setText(QCoreApplication.translate("frmPrincipal", u"8.PISO/LETRA", None))
        self.lblProvincia_24.setText(QCoreApplication.translate("frmPrincipal", u"9.BLOQ./ESC.", None))
        self.lblProvincia_25.setText(QCoreApplication.translate("frmPrincipal", u"10.CUPS LUZ", None))
        self.lblProvincia_26.setText(QCoreApplication.translate("frmPrincipal", u"11.CUPS GAS", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("frmPrincipal", u"DATOS BANCARIOS", None))
        self.lblDNI_NIE_13.setText(QCoreApplication.translate("frmPrincipal", u"12.NUMERO DE IBAN", None))
        self.lENumeroIBAN_2.setInputMask(QCoreApplication.translate("frmPrincipal", u"ES99 9999 9999 99 9999999999", None))
        self.lENumeroIBAN_2.setText(QCoreApplication.translate("frmPrincipal", u"ES    ", None))
        self.lblDNI_NIE_14.setText(QCoreApplication.translate("frmPrincipal", u"13.ENTIDAD", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("frmPrincipal", u"PRODUCTOS VENDIDOS", None))
        ___qtablewidgetitem13 = self.tWContratos_2.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("frmPrincipal", u"Catalogo", None));
        ___qtablewidgetitem14 = self.tWContratos_2.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("frmPrincipal", u"Tipo de Contrato", None));
        ___qtablewidgetitem15 = self.tWContratos_2.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("frmPrincipal", u"Contrato", None));
        ___qtablewidgetitem16 = self.tWContratos_2.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("frmPrincipal", u"CUPS", None));
        ___qtablewidgetitem17 = self.tWContratos_2.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("frmPrincipal", u"Provincia", None));
        ___qtablewidgetitem18 = self.tWContratos_2.horizontalHeaderItem(5)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("frmPrincipal", u"Municipio", None));
        ___qtablewidgetitem19 = self.tWContratos_2.horizontalHeaderItem(6)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("frmPrincipal", u"Nombre de la Calle", None));
        ___qtablewidgetitem20 = self.tWContratos_2.horizontalHeaderItem(7)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("frmPrincipal", u"No Calle", None));
        ___qtablewidgetitem21 = self.tWContratos_2.horizontalHeaderItem(8)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("frmPrincipal", u"Piso/Letra", None));
        ___qtablewidgetitem22 = self.tWContratos_2.horizontalHeaderItem(9)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("frmPrincipal", u"Bloq./Esc.", None));
        ___qtablewidgetitem23 = self.tWContratos_2.horizontalHeaderItem(10)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("frmPrincipal", u"Cod. Postal", None));
        ___qtablewidgetitem24 = self.tWContratos_2.horizontalHeaderItem(11)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("frmPrincipal", u"Entidad Bancaria", None));
        ___qtablewidgetitem25 = self.tWContratos_2.horizontalHeaderItem(12)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("frmPrincipal", u"IBAN", None));
        self.pBEliminarContrato_2.setText(QCoreApplication.translate("frmPrincipal", u"Eliminar Contrato", None))
        self.pBEditarContrato_2.setText(QCoreApplication.translate("frmPrincipal", u"Editar Contrato", None))
        self.pBAgregarContrato_2.setText(QCoreApplication.translate("frmPrincipal", u"Agregar Nuevo Contrato", None))
        self.gBAgregarOEditarContrato_2.setTitle(QCoreApplication.translate("frmPrincipal", u"Agregar o Editar Contrato", None))
        self.lblDNI_NIE_18.setText(QCoreApplication.translate("frmPrincipal", u"1.CATALOGO DE VENTA", None))
#if QT_CONFIG(tooltip)
        self.cmbCatalogos_2.setToolTip(QCoreApplication.translate("frmPrincipal", u"\u00bfQue compa\u00f1ia haz vendido?", None))
#endif // QT_CONFIG(tooltip)
        self.lblDNI_NIE_19.setText(QCoreApplication.translate("frmPrincipal", u"2.TIPO DE CONTRATO", None))
        self.lblDNI_NIE_22.setText(QCoreApplication.translate("frmPrincipal", u"3.CONTRATO", None))
        self.lblProvincia_27.setText(QCoreApplication.translate("frmPrincipal", u"4.CUPS", None))
        self.lblProvincia_28.setText(QCoreApplication.translate("frmPrincipal", u"5.PROVINCIA", None))
        self.lblProvincia_29.setText(QCoreApplication.translate("frmPrincipal", u"6.MUNICIPIO", None))
        self.lblProvincia_30.setText(QCoreApplication.translate("frmPrincipal", u"7.NOMBRE DE LA CALLE", None))
        self.lblProvincia_31.setText(QCoreApplication.translate("frmPrincipal", u"8.NUMERO DE LA CALLE", None))
        self.sBNumeroCalleSuministro_2.setSpecialValueText(QCoreApplication.translate("frmPrincipal", u"S/N", None))
        self.lblProvincia_32.setText(QCoreApplication.translate("frmPrincipal", u"9.PISO Y LETRA", None))
        self.lblProvincia_33.setText(QCoreApplication.translate("frmPrincipal", u"10.BLOQ./ESC.", None))
        self.lblProvincia_34.setText(QCoreApplication.translate("frmPrincipal", u"11.CODIGO POSTAL", None))
        self.lECodigoPostalSuministro_2.setInputMask(QCoreApplication.translate("frmPrincipal", u"99999", None))
        self.lblDNI_NIE_15.setText(QCoreApplication.translate("frmPrincipal", u"12.NUMERO DE IBAN", None))
        self.lENumeroIBANSuministro_2.setInputMask(QCoreApplication.translate("frmPrincipal", u"ES99 9999 9999 99 9999999999", None))
        self.lENumeroIBANSuministro_2.setText(QCoreApplication.translate("frmPrincipal", u"ES    ", None))
        self.lblDNI_NIE_20.setText(QCoreApplication.translate("frmPrincipal", u"13.ENTIDAD BANCARIA", None))
        self.pBCancelarCambiosEnContrato_2.setText(QCoreApplication.translate("frmPrincipal", u"Cancelar Cambios", None))
        self.pBGuardarCambiosEnContrato_2.setText(QCoreApplication.translate("frmPrincipal", u"Guardar Cambios", None))
        self.lEUserCRM_2.setPlaceholderText(QCoreApplication.translate("frmPrincipal", u"Usuario para CRM", None))
        self.lEPassCRM_2.setPlaceholderText(QCoreApplication.translate("frmPrincipal", u"Contrase\u00f1a para CRM", None))
        self.cBOportunidadesSeparadas_2.setText(QCoreApplication.translate("frmPrincipal", u"Crear Oportunidad por cada Contrato", None))
        self.pBEnviarVentaACRM_2.setText(QCoreApplication.translate("frmPrincipal", u"ENVIAR A CRM", None))
        self.tabFichas.setTabText(self.tabFichas.indexOf(self.tabFichaTelefonia), QCoreApplication.translate("frmPrincipal", u"Telefonia", None))
    # retranslateUi


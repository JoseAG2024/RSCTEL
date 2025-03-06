# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'frmLoginIcTDnW.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
import os
# Cambiar el directorio de trabajo al directorio donde está el script
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLayout,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_frmLogin(object):
    def setupUi(self, frmLogin):
        if not frmLogin.objectName():
            frmLogin.setObjectName(u"frmLogin")
        frmLogin.setWindowModality(Qt.WindowModality.ApplicationModal)
        frmLogin.resize(415, 138)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(frmLogin.sizePolicy().hasHeightForWidth())
        frmLogin.setSizePolicy(sizePolicy)
        frmLogin.setMinimumSize(QSize(415, 138))
        frmLogin.setMaximumSize(QSize(415, 138))
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        frmLogin.setPalette(palette)
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        frmLogin.setFont(font)
        frmLogin.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        icon = QIcon()
        icon.addFile(u"../res/img/logo.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        frmLogin.setWindowIcon(icon)
        frmLogin.setWindowOpacity(1.000000000000000)
        frmLogin.setAutoFillBackground(True)
        self.centralwidget = QWidget(frmLogin)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.QLImagen = QLabel(self.centralwidget)
        self.QLImagen.setObjectName(u"QLImagen")
        self.QLImagen.setMaximumSize(QSize(160, 16777215))
        self.QLImagen.setTextFormat(Qt.TextFormat.AutoText)
        self.QLImagen.setPixmap(QPixmap(u"../res/img/logo.png"))
        self.QLImagen.setScaledContents(True)

        self.verticalLayout_2.addWidget(self.QLImagen)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.lblTitulo = QLabel(self.centralwidget)
        self.lblTitulo.setObjectName(u"lblTitulo")
        palette1 = QPalette()
        brush1 = QBrush(QColor(23, 83, 160, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        self.lblTitulo.setPalette(palette1)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(14)
        font1.setBold(True)
        self.lblTitulo.setFont(font1)
        self.lblTitulo.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.verticalLayout.addWidget(self.lblTitulo)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(25, 25))
        self.label.setMaximumSize(QSize(25, 25))
        self.label.setPixmap(QPixmap(u"../res/img/username_25px.png"))

        self.horizontalLayout_2.addWidget(self.label)

        self.QLEUsuario = QLineEdit(self.centralwidget)
        self.QLEUsuario.setObjectName(u"QLEUsuario")
        palette2 = QPalette()
        brush2 = QBrush(QColor(0, 0, 0, 228))
        brush2.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush3 = QBrush(QColor(85, 255, 255, 228))
        brush3.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush)
        brush4 = QBrush(QColor(85, 170, 255, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.QLEUsuario.setPalette(palette2)
        self.QLEUsuario.setFocusPolicy(Qt.FocusPolicy.StrongFocus)

        self.horizontalLayout_2.addWidget(self.QLEUsuario)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(25, 25))
        self.label_2.setMaximumSize(QSize(25, 25))
        self.label_2.setPixmap(QPixmap(u"../res/img/sign_in_form_password_25px.png"))

        self.horizontalLayout_3.addWidget(self.label_2)

        self.QLEClave = QLineEdit(self.centralwidget)
        self.QLEClave.setObjectName(u"QLEClave")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush3)
        brush5 = QBrush(QColor(255, 255, 255, 100))
        brush5.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush1)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush1)
#endif
        self.QLEClave.setPalette(palette3)
        self.QLEClave.setFrame(True)
        self.QLEClave.setEchoMode(QLineEdit.EchoMode.Password)

        self.horizontalLayout_3.addWidget(self.QLEClave)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)

        self.PBIngresar = QPushButton(self.centralwidget)
        self.PBIngresar.setObjectName(u"PBIngresar")
        self.PBIngresar.setMinimumSize(QSize(120, 35))
        self.PBIngresar.setMaximumSize(QSize(120, 35))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.Button, brush)
        brush6 = QBrush(QColor(23, 83, 160, 225))
        brush6.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(249, 249, 249, 77))
        brush7.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush7)
        brush8 = QBrush(QColor(0, 0, 0, 92))
        brush8.setStyle(Qt.SolidPattern)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush8)
        self.PBIngresar.setPalette(palette4)
        self.PBIngresar.setFocusPolicy(Qt.FocusPolicy.StrongFocus)
        self.PBIngresar.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        icon1 = QIcon()
        icon1.addFile(u"../res/img/enter_25px.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PBIngresar.setIcon(icon1)
        self.PBIngresar.setAutoDefault(False)
        self.PBIngresar.setFlat(False)

        self.horizontalLayout_4.addWidget(self.PBIngresar)


        self.verticalLayout.addLayout(self.horizontalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout)

        frmLogin.setCentralWidget(self.centralwidget)

        self.retranslateUi(frmLogin)

        self.PBIngresar.setDefault(True)


        QMetaObject.connectSlotsByName(frmLogin)
    # setupUi

    def retranslateUi(self, frmLogin):
        frmLogin.setWindowTitle(QCoreApplication.translate("frmLogin", u"RSCTEL Agent", None))
        self.QLImagen.setText("")
        self.lblTitulo.setText(QCoreApplication.translate("frmLogin", u"RSCTEL AGENT", None))
        self.label.setText("")
#if QT_CONFIG(tooltip)
        self.QLEUsuario.setToolTip(QCoreApplication.translate("frmLogin", u"Nombre de usuario asignado por Administracion", None))
#endif // QT_CONFIG(tooltip)
        self.QLEUsuario.setPlaceholderText(QCoreApplication.translate("frmLogin", u"Usuario", None))
        self.label_2.setText("")
#if QT_CONFIG(tooltip)
        self.QLEClave.setToolTip(QCoreApplication.translate("frmLogin", u"Contrase\u00f1a del agente.", None))
#endif // QT_CONFIG(tooltip)
        self.QLEClave.setPlaceholderText(QCoreApplication.translate("frmLogin", u"Clave", None))
        self.PBIngresar.setText(QCoreApplication.translate("frmLogin", u"Ingresar", None))
    # retranslateUi


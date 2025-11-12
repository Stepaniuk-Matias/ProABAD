# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_view.ui'
##
## Created by: Qt User Interface Compiler version 6.10.0
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_LoginForm(object):
    def setupUi(self, LoginForm):
        if not LoginForm.objectName():
            LoginForm.setObjectName(u"LoginForm")
        LoginForm.resize(360, 340)
        LoginForm.setMaximumSize(QSize(360, 340))
        self.verticalLayout = QVBoxLayout(LoginForm)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.central_widget_frame = QFrame(LoginForm)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
        self.central_widget_frame.setStyleSheet(u"border-color: rgb(0, 0, 0);")
        self.central_widget_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.central_widget_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.central_widget_frame)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.background_frame = QFrame(self.central_widget_frame)
        self.background_frame.setObjectName(u"background_frame")
        self.background_frame.setStyleSheet(u"background-color: rgb(245,240,225);")
        self.background_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.background_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.background_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.content_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_frame = QFrame(self.content_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setMaximumSize(QSize(16777215, 120))
        self.title_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.title_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(self.title_frame)
        self.label_2.setObjectName(u"label_2")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QSize(120, 100))
        self.label_2.setPixmap(QPixmap(u"../assets/icons/logo_abad.png"))
        self.label_2.setScaledContents(True)

        self.horizontalLayout.addWidget(self.label_2)

        self.label = QLabel(self.title_frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setStyleSheet(u"color: grey;")
        self.label.setFrameShadow(QFrame.Shadow.Plain)
        self.label.setMidLineWidth(1)
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.horizontalLayout.addWidget(self.label)


        self.verticalLayout_4.addWidget(self.title_frame)

        self.login_frame = QFrame(self.content_frame)
        self.login_frame.setObjectName(u"login_frame")
        self.login_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.login_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.login_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.input_frame = QFrame(self.login_frame)
        self.input_frame.setObjectName(u"input_frame")
        self.input_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.input_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.input_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.user_lineEdit = QLineEdit(self.input_frame)
        self.user_lineEdit.setObjectName(u"user_lineEdit")
        self.user_lineEdit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")

        self.verticalLayout_5.addWidget(self.user_lineEdit)

        self.password_lineEdit = QLineEdit(self.input_frame)
        self.password_lineEdit.setObjectName(u"password_lineEdit")
        self.password_lineEdit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.password_lineEdit.setEchoMode(QLineEdit.EchoMode.Password)

        self.verticalLayout_5.addWidget(self.password_lineEdit)


        self.verticalLayout_7.addWidget(self.input_frame)

        self.buttons_frame = QFrame(self.login_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.buttons_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_2 = QPushButton(self.buttons_frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")

        self.verticalLayout_6.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.buttons_frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")

        self.verticalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_7.addWidget(self.buttons_frame)


        self.verticalLayout_4.addWidget(self.login_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(LoginForm)

        QMetaObject.connectSlotsByName(LoginForm)
    # setupUi

    def retranslateUi(self, LoginForm):
        LoginForm.setWindowTitle(QCoreApplication.translate("LoginForm", u"Form", None))
        self.label_2.setText("")
        self.label.setText(QCoreApplication.translate("LoginForm", u"LOGIN", None))
        self.user_lineEdit.setInputMask("")
        self.user_lineEdit.setText("")
        self.user_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginForm", u"usuario", None))
        self.password_lineEdit.setInputMask("")
        self.password_lineEdit.setText("")
        self.password_lineEdit.setPlaceholderText(QCoreApplication.translate("LoginForm", u"contrase\u00f1a", None))
        self.pushButton_2.setText(QCoreApplication.translate("LoginForm", u"Ingresar", None))
        self.pushButton.setText(QCoreApplication.translate("LoginForm", u"Nuevo usuario", None))
    # retranslateUi


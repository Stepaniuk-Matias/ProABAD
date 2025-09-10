# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_view.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
    QLayout, QPushButton, QSizePolicy, QSpacerItem,
    QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 722)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.central_widget_frame = QFrame(Form)
        self.central_widget_frame.setObjectName(u"central_widget_frame")
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
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.content_frame = QFrame(self.background_frame)
        self.content_frame.setObjectName(u"content_frame")
        self.content_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.content_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout = QHBoxLayout(self.content_frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.option_bar_frame = QFrame(self.content_frame)
        self.option_bar_frame.setObjectName(u"option_bar_frame")
        self.option_bar_frame.setMaximumSize(QSize(120, 16777215))
        self.option_bar_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.option_bar_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.option_bar_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_2 = QFrame(self.option_bar_frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer = QSpacerItem(69, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.toolButton = QToolButton(self.frame_2)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QToolButton::hover {background-color : #ffc13b};")
        icon = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MediaSeekBackward))
        self.toolButton.setIcon(icon)

        self.horizontalLayout_2.addWidget(self.toolButton)


        self.verticalLayout_5.addWidget(self.frame_2)

        self.frame = QFrame(self.option_bar_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.familys_button = QPushButton(self.frame)
        self.familys_button.setObjectName(u"familys_button")
        self.familys_button.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")

        self.verticalLayout_4.addWidget(self.familys_button)

        self.products_button = QPushButton(self.frame)
        self.products_button.setObjectName(u"products_button")
        self.products_button.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")

        self.verticalLayout_4.addWidget(self.products_button)

        self.procceses_button = QPushButton(self.frame)
        self.procceses_button.setObjectName(u"procceses_button")
        self.procceses_button.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")

        self.verticalLayout_4.addWidget(self.procceses_button)


        self.verticalLayout_5.addWidget(self.frame)

        self.verticalSpacer = QSpacerItem(20, 514, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.option_bar_frame)

        self.line = QFrame(self.content_frame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.dashboard_frame = QFrame(self.content_frame)
        self.dashboard_frame.setObjectName(u"dashboard_frame")
        self.dashboard_frame.setMaximumSize(QSize(16777215, 16777215))
        self.dashboard_frame.setSizeIncrement(QSize(762, 678))
        self.dashboard_frame.setBaseSize(QSize(762, 678))
        self.dashboard_frame.setLayoutDirection(Qt.LayoutDirection.RightToLeft)
        self.dashboard_frame.setAutoFillBackground(False)
        self.dashboard_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.dashboard_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.dashboard_frame)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setSizeConstraint(QLayout.SizeConstraint.SetNoConstraint)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.dashboard_frame)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QSize(10000, 10000))
        self.label.setSizeIncrement(QSize(2, 1))
        self.label.setBaseSize(QSize(381, 339))
        self.label.setAutoFillBackground(False)
        self.label.setPixmap(QPixmap(u"./src/assets/icons/logo_abad.png"))
        self.label.setScaledContents(True)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setWordWrap(False)

        self.verticalLayout_6.addWidget(self.label)


        self.horizontalLayout.addWidget(self.dashboard_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)

        QWidget.setTabOrder(self.toolButton, self.products_button)
        QWidget.setTabOrder(self.products_button, self.procceses_button)
        QWidget.setTabOrder(self.procceses_button, self.familys_button)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.familys_button.setText(QCoreApplication.translate("Form", u"Familias", None))
        self.products_button.setText(QCoreApplication.translate("Form", u"Productos", None))
        self.procceses_button.setText(QCoreApplication.translate("Form", u"Procesos", None))
        self.label.setText("")
    # retranslateUi


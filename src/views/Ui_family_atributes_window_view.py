# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'family_atributes_window_view.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QTreeView, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1024, 580)
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
        self.left_frame = QFrame(self.content_frame)
        self.left_frame.setObjectName(u"left_frame")
        self.left_frame.setMinimumSize(QSize(300, 0))
        self.left_frame.setMaximumSize(QSize(500, 16777215))
        self.left_frame.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.left_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.left_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.left_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(9, 0, -1, 0)
        self.search_bars_frame = QFrame(self.left_frame)
        self.search_bars_frame.setObjectName(u"search_bars_frame")
        self.search_bars_frame.setMinimumSize(QSize(0, 40))
        self.search_bars_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.search_bars_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.search_bars_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, -1)
        self.label = QLabel(self.search_bars_frame)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(30, 30))
        self.label.setMaximumSize(QSize(30, 16777215))
        self.label.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.label.setPixmap(QPixmap(u"./src/assets/icons/search.png"))

        self.horizontalLayout_2.addWidget(self.label)

        self.search_family_lineEdit = QLineEdit(self.search_bars_frame)
        self.search_family_lineEdit.setObjectName(u"search_family_lineEdit")
        self.search_family_lineEdit.setMinimumSize(QSize(0, 30))
        self.search_family_lineEdit.setMaximumSize(QSize(500, 16777215))
        self.search_family_lineEdit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")

        self.horizontalLayout_2.addWidget(self.search_family_lineEdit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_2 = QLabel(self.search_bars_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(30, 30))
        self.label_2.setMaximumSize(QSize(30, 16777215))
        self.label_2.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")
        self.label_2.setPixmap(QPixmap(u"./src/assets/icons/search.png"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.search_atribute_lineEdit = QLineEdit(self.search_bars_frame)
        self.search_atribute_lineEdit.setObjectName(u"search_atribute_lineEdit")
        self.search_atribute_lineEdit.setMinimumSize(QSize(0, 30))
        self.search_atribute_lineEdit.setMaximumSize(QSize(500, 16777215))
        self.search_atribute_lineEdit.setStyleSheet(u"background-color: white;\n"
"border-radius: 0px;")

        self.horizontalLayout_2.addWidget(self.search_atribute_lineEdit)


        self.verticalLayout_4.addWidget(self.search_bars_frame)

        self.treeView = QTreeView(self.left_frame)
        self.treeView.setObjectName(u"treeView")

        self.verticalLayout_4.addWidget(self.treeView)


        self.horizontalLayout.addWidget(self.left_frame)

        self.line = QFrame(self.content_frame)
        self.line.setObjectName(u"line")
        self.line.setCursor(QCursor(Qt.CursorShape.ArrowCursor))
        self.line.setStyleSheet(u"color: rgb(255, 85, 0);")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout.addWidget(self.line)

        self.right_frame = QFrame(self.content_frame)
        self.right_frame.setObjectName(u"right_frame")
        self.right_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.right_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.right_frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.buttons_frame = QFrame(self.right_frame)
        self.buttons_frame.setObjectName(u"buttons_frame")
        self.buttons_frame.setMaximumSize(QSize(16777215, 50))
        self.buttons_frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.buttons_frame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.buttons_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.edit_family_button = QPushButton(self.buttons_frame)
        self.edit_family_button.setObjectName(u"edit_family_button")
        self.edit_family_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.edit_family_button.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon = QIcon()
        icon.addFile(u"./src/assets/icons/edit.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.edit_family_button.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.edit_family_button)

        self.create_family_button = QPushButton(self.buttons_frame)
        self.create_family_button.setObjectName(u"create_family_button")
        self.create_family_button.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.create_family_button.setStyleSheet(u"QPushButton {\n"
"	background-color : #ff6e40;\n"
"	color: white;\n"
"}\n"
"QPushButton::hover {background-color : #ffc13b};")
        icon1 = QIcon()
        icon1.addFile(u"./src/assets/icons/plus.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.create_family_button.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.create_family_button)


        self.verticalLayout_5.addWidget(self.buttons_frame)


        self.horizontalLayout.addWidget(self.right_frame)


        self.verticalLayout_3.addWidget(self.content_frame)


        self.verticalLayout_2.addWidget(self.background_frame)


        self.verticalLayout.addWidget(self.central_widget_frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.search_family_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar familia...", None))
        self.label_2.setText("")
        self.search_atribute_lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Buscar atributo...", None))
        self.edit_family_button.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.create_family_button.setText(QCoreApplication.translate("Form", u"Nueva Familia", None))
    # retranslateUi


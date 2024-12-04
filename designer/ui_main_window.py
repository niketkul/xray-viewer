# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(9, 9, 783, 531))
        self.horizontalLayout_3 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 10, 10, 10)
        self.image_label = QLabel(self.horizontalLayoutWidget)
        self.image_label.setObjectName(u"image_label")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image_label.sizePolicy().hasHeightForWidth())
        self.image_label.setSizePolicy(sizePolicy)
        self.image_label.setMinimumSize(QSize(502, 511))
        self.image_label.setMargin(10)

        self.horizontalLayout_3.addWidget(self.image_label)

        self.control_container = QWidget(self.horizontalLayoutWidget)
        self.control_container.setObjectName(u"control_container")
        self.control_container.setMinimumSize(QSize(251, 511))
        self.verticalLayout_5 = QVBoxLayout(self.control_container)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.slider_area_container = QWidget(self.control_container)
        self.slider_area_container.setObjectName(u"slider_area_container")
        self.slider_area_container.setMinimumSize(QSize(227, 239))
        self.horizontalLayout_9 = QHBoxLayout(self.slider_area_container)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.brightness_container = QWidget(self.slider_area_container)
        self.brightness_container.setObjectName(u"brightness_container")
        self.verticalLayout_6 = QVBoxLayout(self.brightness_container)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.brightness_label = QLabel(self.brightness_container)
        self.brightness_label.setObjectName(u"brightness_label")

        self.verticalLayout_6.addWidget(self.brightness_label)

        self.brightness_slider = QSlider(self.brightness_container)
        self.brightness_slider.setObjectName(u"brightness_slider")
        self.brightness_slider.setMinimumSize(QSize(22, 160))
        self.brightness_slider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_6.addWidget(self.brightness_slider)


        self.horizontalLayout_9.addWidget(self.brightness_container)

        self.contrast_container = QWidget(self.slider_area_container)
        self.contrast_container.setObjectName(u"contrast_container")
        self.verticalLayout_7 = QVBoxLayout(self.contrast_container)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.contrast_label = QLabel(self.contrast_container)
        self.contrast_label.setObjectName(u"contrast_label")

        self.verticalLayout_7.addWidget(self.contrast_label)

        self.contrast_slider = QSlider(self.contrast_container)
        self.contrast_slider.setObjectName(u"contrast_slider")
        self.contrast_slider.setMinimumSize(QSize(22, 160))
        self.contrast_slider.setOrientation(Qt.Orientation.Vertical)

        self.verticalLayout_7.addWidget(self.contrast_slider)


        self.horizontalLayout_9.addWidget(self.contrast_container)


        self.verticalLayout_5.addWidget(self.slider_area_container)

        self.button_area_container = QWidget(self.control_container)
        self.button_area_container.setObjectName(u"button_area_container")
        self.button_area_container.setMinimumSize(QSize(227, 238))
        self.verticalLayout_8 = QVBoxLayout(self.button_area_container)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.save_button = QPushButton(self.button_area_container)
        self.save_button.setObjectName(u"save_button")
        self.save_button.setMinimumSize(QSize(203, 45))

        self.verticalLayout_8.addWidget(self.save_button)


        self.verticalLayout_5.addWidget(self.button_area_container)


        self.horizontalLayout_3.addWidget(self.control_container)

        self.horizontalLayout_3.setStretch(0, 2)
        self.horizontalLayout_3.setStretch(1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.image_label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.brightness_label.setText(QCoreApplication.translate("MainWindow", u"Brightness", None))
        self.contrast_label.setText(QCoreApplication.translate("MainWindow", u"Contrast", None))
        self.save_button.setText(QCoreApplication.translate("MainWindow", u"Save Image", None))
    # retranslateUi


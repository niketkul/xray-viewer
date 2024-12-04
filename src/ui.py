import sys
import cv2
import numpy as np

from PySide6.QtCore import (
    QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt, Slot, Signal
)
from PySide6.QtGui import (
    QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform, 
    QImageReader
)
from PySide6.QtWidgets import (
    QApplication, QHBoxLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QSlider,
    QStatusBar, QVBoxLayout, QWidget, QFileDialog
)

class UIMainWindow(QMainWindow):
    imageUpdated = Signal(int, str)

    def setupUi(self, mainWindow: QMainWindow) -> None:
        if not mainWindow.objectName():
            mainWindow.setObjectName("mainWindow")
        mainWindow.resize(800, 600)
        mainWindow.setMinimumSize(QSize(800, 600))
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.setupAppContainer(mainWindow)
        self.setupImageArea()
        self.setupControlArea()
        self.setupSliders()
        self.setupButtons()

        self.retranslateUi(mainWindow)

        QMetaObject.connectSlotsByName(mainWindow)
    
    # Setup the main container for the application
    def setupAppContainer(self, mainWindow: QMainWindow) -> None:
        self.centralwidget = QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.mainContainer = QWidget(self.centralwidget)
        self.mainContainer.setObjectName("mainContainer")
        self.mainContainer.setGeometry(QRect(9, 9, 783, 531))

        self.mainHorizontalLayout = QHBoxLayout(self.mainContainer)
        self.mainHorizontalLayout.setObjectName("mainHorizontalLayout")
        self.mainHorizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.mainHorizontalLayout.setStretch(0, 2)
        self.mainHorizontalLayout.setStretch(1, 1)

        mainWindow.setCentralWidget(self.centralwidget)

    # Setup the area where the image will be displayed
    def setupImageArea(self) -> None:
        self.imageLabel = QLabel(self.mainContainer)
        self.imageLabel.setObjectName("imageLabel")
        self.imageLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy)
        self.imageLabel.setMinimumSize(QSize(502, 511))
        self.imageLabel.setMargin(10)
        self.imageLabel.setScaledContents(True)
        self.imageUpdated.connect(self.processImage)
        self.mainHorizontalLayout.addWidget(self.imageLabel)
    
    @Slot(int, str)
    def processImage(self, value: int, adjustment_type: str) -> None:
        # Do nothing if image has not been loaded
        if not hasattr(self, "original_image") or self.original_image is None:
            print("No image loaded")
            return
        
        print("processImage")
        new_pixmap = self.getNewPixmap(value, adjustment_type)
        self.imageLabel.setPixmap(new_pixmap)

    def getNewPixmap(self, value: int, adjustment_type: str) -> QPixmap:
        print("getNewPixmap")
        if adjustment_type == "Brightness":
            alpha = 1.0 
            beta = value
        elif adjustment_type == "Contrast":
            alpha = 1.0 + (value / 100.0)
            beta = 0

        self.processed_image = cv2.convertScaleAbs(self.original_image, alpha=alpha, beta=beta)

        height, width, channel = self.processed_image.shape
        bytes_per_line = 3 * width
        qimage = QImage(self.processed_image.data, width, height, bytes_per_line, QImage.Format_RGB888)
        return QPixmap.fromImage(qimage)

    # Setup the area where the sliders and button controls will be displayed
    def setupControlArea(self) -> None:
        self.controlAreaContainer = QWidget(self.mainContainer)
        self.controlAreaContainer.setObjectName("controlAreaContainer")
        self.controlAreaContainer.setMinimumSize(QSize(251, 511))

        self.controlAreaVerticalLayout = QVBoxLayout(self.controlAreaContainer)
        self.controlAreaVerticalLayout.setObjectName("controlAreaVerticalLayout")

        self.mainHorizontalLayout.addWidget(self.controlAreaContainer)

    # Setup the sliders for brightness and contrast
    def setupSliders(self) -> None:
        self.sliderAreaContainer = QWidget(self.controlAreaContainer)
        self.sliderAreaContainer.setObjectName("sliderAreaContainer")
        self.sliderAreaContainer.setMinimumSize(QSize(227, 239))

        self.sliderAreaHorizontalLayout = QHBoxLayout(self.sliderAreaContainer)
        self.sliderAreaHorizontalLayout.setObjectName("sliderAreaHorizontalLayout")

        class LabeledSlider(QWidget):
            sliderChanged = Signal(int, str)

            def __init__(self, label_text: str, parent: QWidget = None) -> None:
                super().__init__(parent)
                self.setObjectName(f"{label_text.lower()}Container")
                self.setMinimumSize(QSize(22, 160))

                self.verticalLayout = QVBoxLayout(self)
                self.verticalLayout.setObjectName(f"{label_text.lower()}VerticalLayout")

                self.label = QLabel(self)
                self.label.setObjectName(f"{label_text.lower()}Label")
                self.label.setText(label_text)
                self.verticalLayout.addWidget(self.label)

                self.slider = QSlider(self)
                self.slider.setObjectName(f"{label_text.lower()}Slider")
                self.slider.setOrientation(Qt.Orientation.Vertical)

                self.slider.setRange(-100, 100)
                self.slider.setValue(0)
                self.slider.setTickPosition(QSlider.TickPosition.TicksBothSides)
                self.slider.setTickInterval(100)
                self.slider.setSingleStep(1)
                
                self.slider.valueChanged.connect(self.adjustImage)
                self.verticalLayout.addWidget(self.slider)
            
            @Slot(int)
            def adjustImage(self, value: int) -> None:  
                print("adjustImage")    
                if self.label.text() == "Brightness":
                    self.sliderChanged.emit(value, "Brightness")
                elif self.label.text() == "Contrast":
                    self.sliderChanged.emit(value, "Contrast")

        self.brightnessSliderWidget = LabeledSlider("Brightness", self.sliderAreaContainer)
        self.contrastSliderWidget = LabeledSlider("Contrast", self.sliderAreaContainer)

        self.brightnessSliderWidget.sliderChanged.connect(self.imageUpdated.emit)
        self.contrastSliderWidget.sliderChanged.connect(self.imageUpdated.emit)

        self.sliderAreaHorizontalLayout.addWidget(self.brightnessSliderWidget)
        self.sliderAreaHorizontalLayout.addWidget(self.contrastSliderWidget)

        self.controlAreaVerticalLayout.addWidget(self.sliderAreaContainer)

    # Setup the buttons for loading and saving images
    def setupButtons(self) -> None:
        self.buttonAreaContainer = QWidget(self.controlAreaContainer)
        self.buttonAreaContainer.setObjectName("buttonAreaContainer")
        self.buttonAreaContainer.setMinimumSize(QSize(227, 238))

        self.buttonAreaVerticalLayout = QVBoxLayout(self.buttonAreaContainer)
        self.buttonAreaVerticalLayout.setObjectName("buttonAreaVerticalLayout")

        self.loadButton = QPushButton(self.buttonAreaContainer)
        self.loadButton.setObjectName("loadButton")
        self.loadButton.setMinimumSize(QSize(203, 45))
        self.loadButton.clicked.connect(self.openFileDialog)

        self.saveButton = QPushButton(self.buttonAreaContainer)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setMinimumSize(QSize(203, 45))

        self.buttonAreaVerticalLayout.addWidget(self.loadButton)
        self.buttonAreaVerticalLayout.addWidget(self.saveButton)
        
        self.controlAreaVerticalLayout.addWidget(self.buttonAreaContainer)

    def retranslateUi(self, mainWindow: QMainWindow) -> None:
        mainWindow.setWindowTitle(QCoreApplication.translate("mainWindow", "X-Ray Image Processor", None))
        self.imageLabel.setText(QCoreApplication.translate("mainWindow", "No Image Selected", None))
        self.brightnessSliderWidget.label.setText(QCoreApplication.translate("mainWindow", "Brightness", None))
        self.contrastSliderWidget.label.setText(QCoreApplication.translate("mainWindow", "Contrast", None))
        self.loadButton.setText(QCoreApplication.translate("mainWindow", "Load Image", None))
        self.saveButton.setText(QCoreApplication.translate("mainWindow", "Save Image", None))

    @Slot()
    def openFileDialog(self) -> None:
        dialog = QFileDialog(self.centralwidget)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile)
        dialog.setViewMode(QFileDialog.Detail)
        dialog.setNameFilter("Image Files (*.png *.jpg *.jpeg *.bmp);;All Files (*)")
        file_path, _ = dialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")

        if file_path: 
            pixmap = QPixmap(file_path)
            if pixmap.isNull():
                self.imageLabel.setText("Failed to load image")
            else:
                self.original_image = cv2.imread(file_path)
                self.original_image = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)
                scaled_pixmap = pixmap.scaled(
                    self.imageLabel.size(),
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                )
                self.imageLabel.setPixmap(scaled_pixmap)

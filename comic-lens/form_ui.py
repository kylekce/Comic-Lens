# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.6.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGroupBox,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QSlider, QSpacerItem, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(766, 723)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"")
        self.actionOpen_PDF = QAction(MainWindow)
        self.actionOpen_PDF.setObjectName(u"actionOpen_PDF")
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        self.actionFit = QAction(MainWindow)
        self.actionFit.setObjectName(u"actionFit")
        self.actionNext_Page = QAction(MainWindow)
        self.actionNext_Page.setObjectName(u"actionNext_Page")
        self.actionPrevious_Page = QAction(MainWindow)
        self.actionPrevious_Page.setObjectName(u"actionPrevious_Page")
        self.actionStart_Page = QAction(MainWindow)
        self.actionStart_Page.setObjectName(u"actionStart_Page")
        self.actionLast_Page = QAction(MainWindow)
        self.actionLast_Page.setObjectName(u"actionLast_Page")
        self.actionBox_Screenshot = QAction(MainWindow)
        self.actionBox_Screenshot.setObjectName(u"actionBox_Screenshot")
        self.actionBox_Screenshot.setCheckable(True)
        self.actionAsd = QAction(MainWindow)
        self.actionAsd.setObjectName(u"actionAsd")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.main = QHBoxLayout()
        self.main.setObjectName(u"main")
        self.main.setContentsMargins(0, -1, 0, -1)
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.page_layout = QHBoxLayout()
        self.page_layout.setObjectName(u"page_layout")
        self.page_layout.setSizeConstraint(QLayout.SetDefaultConstraint)

        self.main_layout.addLayout(self.page_layout)

        self.page_navigation = QHBoxLayout()
        self.page_navigation.setObjectName(u"page_navigation")
        self.page_navigation.setContentsMargins(0, -1, -1, 0)
        self.page_navigation_frame = QFrame(self.centralwidget)
        self.page_navigation_frame.setObjectName(u"page_navigation_frame")
        self.page_navigation_frame.setFrameShape(QFrame.StyledPanel)
        self.page_navigation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.page_navigation_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(108, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.start_page = QPushButton(self.page_navigation_frame)
        self.start_page.setObjectName(u"start_page")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/resources/skip-start-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_page.setIcon(icon)

        self.horizontalLayout_5.addWidget(self.start_page)

        self.previous_page = QPushButton(self.page_navigation_frame)
        self.previous_page.setObjectName(u"previous_page")
        sizePolicy2.setHeightForWidth(self.previous_page.sizePolicy().hasHeightForWidth())
        self.previous_page.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/resources/caret-left-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_page.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.previous_page)

        self.page_line_edit = QLineEdit(self.page_navigation_frame)
        self.page_line_edit.setObjectName(u"page_line_edit")
        sizePolicy2.setHeightForWidth(self.page_line_edit.sizePolicy().hasHeightForWidth())
        self.page_line_edit.setSizePolicy(sizePolicy2)
        self.page_line_edit.setMaximumSize(QSize(25, 16777215))
        self.page_line_edit.setAutoFillBackground(False)
        self.page_line_edit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.page_line_edit)

        self.page_label = QLabel(self.page_navigation_frame)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout_5.addWidget(self.page_label)

        self.next_page = QPushButton(self.page_navigation_frame)
        self.next_page.setObjectName(u"next_page")
        sizePolicy2.setHeightForWidth(self.next_page.sizePolicy().hasHeightForWidth())
        self.next_page.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/resources/caret-right-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.next_page)

        self.last_page = QPushButton(self.page_navigation_frame)
        self.last_page.setObjectName(u"last_page")
        sizePolicy2.setHeightForWidth(self.last_page.sizePolicy().hasHeightForWidth())
        self.last_page.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/resources/skip-end-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.last_page.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.last_page)

        self.horizontalSpacer_2 = QSpacerItem(107, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.page_navigation.addWidget(self.page_navigation_frame)


        self.main_layout.addLayout(self.page_navigation)

        self.main_layout.setStretch(0, 1)

        self.main.addLayout(self.main_layout)

        self.main_layout_2 = QVBoxLayout()
        self.main_layout_2.setObjectName(u"main_layout_2")
        self.main_layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.main_layout_2_frame = QFrame(self.centralwidget)
        self.main_layout_2_frame.setObjectName(u"main_layout_2_frame")
        self.main_layout_2_frame.setFrameShape(QFrame.StyledPanel)
        self.main_layout_2_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_layout_2_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox_2 = QGroupBox(self.main_layout_2_frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.box_screenshot = QPushButton(self.groupBox_2)
        self.box_screenshot.setObjectName(u"box_screenshot")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.box_screenshot.sizePolicy().hasHeightForWidth())
        self.box_screenshot.setSizePolicy(sizePolicy3)
        icon4 = QIcon()
        icon4.addFile(u":/resources/bounding-box-circles.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.box_screenshot.setIcon(icon4)
        self.box_screenshot.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.box_screenshot)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.main_layout_2_frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label = QLabel(self.groupBox_3)
        self.label.setObjectName(u"label")

        self.verticalLayout_4.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resize_factor_slider = QSlider(self.groupBox_3)
        self.resize_factor_slider.setObjectName(u"resize_factor_slider")
        self.resize_factor_slider.setMinimum(1)
        self.resize_factor_slider.setMaximum(100)
        self.resize_factor_slider.setValue(5)
        self.resize_factor_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.resize_factor_slider)

        self.resize_factor_box = QSpinBox(self.groupBox_3)
        self.resize_factor_box.setObjectName(u"resize_factor_box")
        self.resize_factor_box.setMinimum(1)
        self.resize_factor_box.setMaximum(100)
        self.resize_factor_box.setSingleStep(1)
        self.resize_factor_box.setValue(5)

        self.horizontalLayout.addWidget(self.resize_factor_box)


        self.verticalLayout_4.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.groupBox_3)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_4.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.median_blur_slider = QSlider(self.groupBox_3)
        self.median_blur_slider.setObjectName(u"median_blur_slider")
        self.median_blur_slider.setMinimum(1)
        self.median_blur_slider.setMaximum(100)
        self.median_blur_slider.setValue(5)
        self.median_blur_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.median_blur_slider)

        self.median_blur_box = QSpinBox(self.groupBox_3)
        self.median_blur_box.setObjectName(u"median_blur_box")
        self.median_blur_box.setMinimum(1)
        self.median_blur_box.setMaximum(100)
        self.median_blur_box.setValue(5)

        self.horizontalLayout_3.addWidget(self.median_blur_box)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.main_layout_2_frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy4)
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.input_combo_box = QComboBox(self.groupBox)
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.addItem("")
        self.input_combo_box.setObjectName(u"input_combo_box")

        self.verticalLayout.addWidget(self.input_combo_box)

        self.input_text_edit = QTextEdit(self.groupBox)
        self.input_text_edit.setObjectName(u"input_text_edit")

        self.verticalLayout.addWidget(self.input_text_edit)

        self.translate_button = QPushButton(self.groupBox)
        self.translate_button.setObjectName(u"translate_button")
        icon5 = QIcon()
        icon5.addFile(u":/resources/caret-down-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.translate_button.setIcon(icon5)

        self.verticalLayout.addWidget(self.translate_button)

        self.output_combo_box = QComboBox(self.groupBox)
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
        self.output_combo_box.setObjectName(u"output_combo_box")

        self.verticalLayout.addWidget(self.output_combo_box)

        self.output_text_edit = QTextEdit(self.groupBox)
        self.output_text_edit.setObjectName(u"output_text_edit")
        self.output_text_edit.setReadOnly(True)

        self.verticalLayout.addWidget(self.output_text_edit)


        self.verticalLayout_2.addWidget(self.groupBox)


        self.main_layout_2.addWidget(self.main_layout_2_frame)


        self.main.addLayout(self.main_layout_2)

        self.main.setStretch(0, 2)
        self.main.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.main)

        self.toolbar = QHBoxLayout()
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.toolbar_frame = QFrame(self.centralwidget)
        self.toolbar_frame.setObjectName(u"toolbar_frame")
        self.toolbar_frame.setFrameShape(QFrame.StyledPanel)
        self.toolbar_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.toolbar_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_layout.setContentsMargins(-1, -1, 0, -1)
        self.fit = QPushButton(self.toolbar_frame)
        self.fit.setObjectName(u"fit")
        sizePolicy2.setHeightForWidth(self.fit.sizePolicy().hasHeightForWidth())
        self.fit.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/resources/horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fit.setIcon(icon6)

        self.toolbar_layout.addWidget(self.fit)

        self.zoom_out = QPushButton(self.toolbar_frame)
        self.zoom_out.setObjectName(u"zoom_out")
        sizePolicy2.setHeightForWidth(self.zoom_out.sizePolicy().hasHeightForWidth())
        self.zoom_out.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/resources/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_out.setIcon(icon7)

        self.toolbar_layout.addWidget(self.zoom_out)

        self.zoom_in = QPushButton(self.toolbar_frame)
        self.zoom_in.setObjectName(u"zoom_in")
        sizePolicy2.setHeightForWidth(self.zoom_in.sizePolicy().hasHeightForWidth())
        self.zoom_in.setSizePolicy(sizePolicy2)
        icon8 = QIcon()
        icon8.addFile(u":/resources/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_in.setIcon(icon8)

        self.toolbar_layout.addWidget(self.zoom_in)


        self.horizontalLayout_4.addLayout(self.toolbar_layout)

        self.horizontalSpacer = QSpacerItem(443, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer)

        self.current_file_label = QLabel(self.toolbar_frame)
        self.current_file_label.setObjectName(u"current_file_label")

        self.horizontalLayout_4.addWidget(self.current_file_label)


        self.toolbar.addWidget(self.toolbar_frame)


        self.verticalLayout_3.addLayout(self.toolbar)

        self.verticalLayout_3.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 766, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuAbout.setSeparatorsCollapsible(False)
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuPage = QMenu(self.menubar)
        self.menuPage.setObjectName(u"menuPage")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen_PDF)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionFit)
        self.menuPage.addAction(self.actionNext_Page)
        self.menuPage.addAction(self.actionPrevious_Page)
        self.menuPage.addAction(self.actionStart_Page)
        self.menuPage.addAction(self.actionLast_Page)

        self.retranslateUi(MainWindow)

        self.input_combo_box.setCurrentIndex(4)
        self.output_combo_box.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comic Lens", None))
        self.actionOpen_PDF.setText(QCoreApplication.translate("MainWindow", u"Open PDF", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.actionFit.setText(QCoreApplication.translate("MainWindow", u"Fit to Page", None))
        self.actionNext_Page.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.actionPrevious_Page.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.actionStart_Page.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.actionLast_Page.setText(QCoreApplication.translate("MainWindow", u"Last Page", None))
        self.actionBox_Screenshot.setText(QCoreApplication.translate("MainWindow", u"Box Screenshot", None))
        self.actionAsd.setText(QCoreApplication.translate("MainWindow", u"Asd", None))
#if QT_CONFIG(tooltip)
        self.start_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the Start Page", None))
#endif // QT_CONFIG(tooltip)
        self.start_page.setText("")
#if QT_CONFIG(tooltip)
        self.previous_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the Previous Page", None))
#endif // QT_CONFIG(tooltip)
        self.previous_page.setText("")
#if QT_CONFIG(tooltip)
        self.page_line_edit.setToolTip(QCoreApplication.translate("MainWindow", u"Current Page Number", None))
#endif // QT_CONFIG(tooltip)
        self.page_line_edit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"0", None))
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"of 0", None))
#if QT_CONFIG(tooltip)
        self.next_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the Next Page", None))
#endif // QT_CONFIG(tooltip)
        self.next_page.setText("")
#if QT_CONFIG(tooltip)
        self.last_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the Last Page", None))
#endif // QT_CONFIG(tooltip)
        self.last_page.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
#if QT_CONFIG(tooltip)
        self.box_screenshot.setToolTip(QCoreApplication.translate("MainWindow", u"Draw a Box for Screenshot", None))
#endif // QT_CONFIG(tooltip)
        self.box_screenshot.setText(QCoreApplication.translate("MainWindow", u" Box Screenshot", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Character Recognition", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust the factor by which the image is resized. Larger values may improve OCR on high-resolution images. (default: 5).", None))
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resize Factor", None))
#if QT_CONFIG(tooltip)
        self.resize_factor_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust the factor by which the image is resized. Larger values may improve OCR on high-resolution images. (default: 5).", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust the kernel size for median blur. This controls the degree of smoothing applied to the image. (default: 5).", None))
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Median Blur", None))
#if QT_CONFIG(tooltip)
        self.median_blur_slider.setToolTip(QCoreApplication.translate("MainWindow", u"Adjust the kernel size for median blur. This controls the degree of smoothing applied to the image. (default: 5).", None))
#endif // QT_CONFIG(tooltip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.input_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese - Simplified", None))
        self.input_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese - Simplified (Vertical)", None))
        self.input_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Chinese - Traditional", None))
        self.input_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Chinese - Traditional (Vertical)", None))
        self.input_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"English", None))
        self.input_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.input_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Japanese (Vertical)", None))
        self.input_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Korean", None))

        self.input_combo_box.setCurrentText(QCoreApplication.translate("MainWindow", u"English", None))
#if QT_CONFIG(tooltip)
        self.translate_button.setToolTip(QCoreApplication.translate("MainWindow", u"Re-run the Translation", None))
#endif // QT_CONFIG(tooltip)
        self.translate_button.setText(QCoreApplication.translate("MainWindow", u"Translate to", None))
        self.output_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese - Simplified", None))
        self.output_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese - Traditional", None))
        self.output_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.output_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.output_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Korean", None))

#if QT_CONFIG(tooltip)
        self.fit.setToolTip(QCoreApplication.translate("MainWindow", u"Fit to Page", None))
#endif // QT_CONFIG(tooltip)
        self.fit.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_out.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_out.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_in.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom In", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_in.setText("")
        self.current_file_label.setText(QCoreApplication.translate("MainWindow", u"Open a PDF to start.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPage.setTitle(QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi


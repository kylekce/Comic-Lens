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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QComboBox, QFrame,
    QGroupBox, QHBoxLayout, QLabel, QLayout,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QScrollArea, QSizePolicy, QSlider, QSpacerItem,
    QSpinBox, QTabWidget, QTextEdit, QVBoxLayout,
    QWidget)
import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1237, 776)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamilies([u"Verdana"])
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/resources/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
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
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionDocumentation = QAction(MainWindow)
        self.actionDocumentation.setObjectName(u"actionDocumentation")
        self.actionDocumentation.setMenuRole(QAction.TextHeuristicRole)
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
        self.main_layout_frame = QFrame(self.centralwidget)
        self.main_layout_frame.setObjectName(u"main_layout_frame")
        self.main_layout_frame.setFrameShape(QFrame.StyledPanel)
        self.main_layout_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.main_layout_frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.page_layout = QHBoxLayout()
        self.page_layout.setObjectName(u"page_layout")
        self.page_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.start_layout = QVBoxLayout()
        self.start_layout.setObjectName(u"start_layout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.start_layout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_6)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, -1, 20)
        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_8)

        self.label_6 = QLabel(self.main_layout_frame)
        self.label_6.setObjectName(u"label_6")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy2)
        self.label_6.setMinimumSize(QSize(0, 0))
        self.label_6.setMaximumSize(QSize(350, 205))
        font1 = QFont()
        font1.setFamilies([u"Verdana"])
        font1.setPointSize(9)
        self.label_6.setFont(font1)
        self.label_6.setTextFormat(Qt.AutoText)
        self.label_6.setPixmap(QPixmap(u":/resources/logo-mini.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setAlignment(Qt.AlignCenter)
        self.label_6.setMargin(0)

        self.horizontalLayout_8.addWidget(self.label_6)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_7)


        self.verticalLayout_11.addLayout(self.horizontalLayout_8)

        self.start_label_1 = QLabel(self.main_layout_frame)
        self.start_label_1.setObjectName(u"start_label_1")
        self.start_label_1.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_label_1.setMargin(10)

        self.verticalLayout_11.addWidget(self.start_label_1)

        self.start_label_2 = QLabel(self.main_layout_frame)
        self.start_label_2.setObjectName(u"start_label_2")
        self.start_label_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_label_2.setMargin(10)

        self.verticalLayout_11.addWidget(self.start_label_2)

        self.start_label_3 = QLabel(self.main_layout_frame)
        self.start_label_3.setObjectName(u"start_label_3")
        self.start_label_3.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.start_label_3.setMargin(10)

        self.verticalLayout_11.addWidget(self.start_label_3)


        self.horizontalLayout_7.addLayout(self.verticalLayout_11)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_5)


        self.start_layout.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 20, -1, -1)
        self.open_button = QPushButton(self.main_layout_frame)
        self.open_button.setObjectName(u"open_button")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy3)
        font2 = QFont()
        font2.setFamilies([u"Verdana"])
        font2.setBold(True)
        self.open_button.setFont(font2)

        self.horizontalLayout_6.addWidget(self.open_button)


        self.start_layout.addLayout(self.horizontalLayout_6)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.start_layout.addItem(self.verticalSpacer_3)


        self.page_layout.addLayout(self.start_layout)


        self.verticalLayout_5.addLayout(self.page_layout)

        self.page_navigation = QHBoxLayout()
        self.page_navigation.setObjectName(u"page_navigation")
        self.page_navigation.setContentsMargins(0, -1, -1, 0)
        self.page_navigation_frame = QFrame(self.main_layout_frame)
        self.page_navigation_frame.setObjectName(u"page_navigation_frame")
        self.page_navigation_frame.setFrameShape(QFrame.StyledPanel)
        self.page_navigation_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.page_navigation_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalSpacer_3 = QSpacerItem(106, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_3)

        self.start_page = QPushButton(self.page_navigation_frame)
        self.start_page.setObjectName(u"start_page")
        sizePolicy3.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy3)
        icon1 = QIcon()
        icon1.addFile(u":/resources/skip-start-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_page.setIcon(icon1)

        self.horizontalLayout_5.addWidget(self.start_page)

        self.previous_page = QPushButton(self.page_navigation_frame)
        self.previous_page.setObjectName(u"previous_page")
        sizePolicy3.setHeightForWidth(self.previous_page.sizePolicy().hasHeightForWidth())
        self.previous_page.setSizePolicy(sizePolicy3)
        icon2 = QIcon()
        icon2.addFile(u":/resources/caret-left-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_page.setIcon(icon2)

        self.horizontalLayout_5.addWidget(self.previous_page)

        self.page_spin_box = QSpinBox(self.page_navigation_frame)
        self.page_spin_box.setObjectName(u"page_spin_box")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.page_spin_box.sizePolicy().hasHeightForWidth())
        self.page_spin_box.setSizePolicy(sizePolicy4)
        self.page_spin_box.setAlignment(Qt.AlignCenter)
        self.page_spin_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.page_spin_box.setMaximum(999)

        self.horizontalLayout_5.addWidget(self.page_spin_box)

        self.page_label = QLabel(self.page_navigation_frame)
        self.page_label.setObjectName(u"page_label")

        self.horizontalLayout_5.addWidget(self.page_label)

        self.next_page = QPushButton(self.page_navigation_frame)
        self.next_page.setObjectName(u"next_page")
        sizePolicy3.setHeightForWidth(self.next_page.sizePolicy().hasHeightForWidth())
        self.next_page.setSizePolicy(sizePolicy3)
        icon3 = QIcon()
        icon3.addFile(u":/resources/caret-right-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page.setIcon(icon3)

        self.horizontalLayout_5.addWidget(self.next_page)

        self.last_page = QPushButton(self.page_navigation_frame)
        self.last_page.setObjectName(u"last_page")
        sizePolicy3.setHeightForWidth(self.last_page.sizePolicy().hasHeightForWidth())
        self.last_page.setSizePolicy(sizePolicy3)
        icon4 = QIcon()
        icon4.addFile(u":/resources/skip-end-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.last_page.setIcon(icon4)

        self.horizontalLayout_5.addWidget(self.last_page)

        self.horizontalSpacer_2 = QSpacerItem(105, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.page_navigation.addWidget(self.page_navigation_frame)


        self.verticalLayout_5.addLayout(self.page_navigation)

        self.verticalLayout_5.setStretch(0, 1)

        self.main_layout.addWidget(self.main_layout_frame)


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
        self.verticalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.groupBox_2 = QGroupBox(self.main_layout_2_frame)
        self.groupBox_2.setObjectName(u"groupBox_2")
        font3 = QFont()
        font3.setFamilies([u"Verdana"])
        font3.setBold(False)
        self.groupBox_2.setFont(font3)
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.box_button = QPushButton(self.groupBox_2)
        self.box_button.setObjectName(u"box_button")
        sizePolicy4.setHeightForWidth(self.box_button.sizePolicy().hasHeightForWidth())
        self.box_button.setSizePolicy(sizePolicy4)
        self.box_button.setFont(font2)
        icon5 = QIcon()
        icon5.addFile(u":/resources/bounding-box-circles.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.box_button.setIcon(icon5)
        self.box_button.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.box_button)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.main_layout_2_frame)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setFont(font3)
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.tabWidget = QTabWidget(self.groupBox_3)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_6 = QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout_7.addWidget(self.label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.resize_factor_slider = QSlider(self.frame)
        self.resize_factor_slider.setObjectName(u"resize_factor_slider")
        self.resize_factor_slider.setMinimum(1)
        self.resize_factor_slider.setMaximum(50)
        self.resize_factor_slider.setPageStep(0)
        self.resize_factor_slider.setValue(5)
        self.resize_factor_slider.setTracking(True)
        self.resize_factor_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout.addWidget(self.resize_factor_slider)

        self.resize_factor_box = QSpinBox(self.frame)
        self.resize_factor_box.setObjectName(u"resize_factor_box")
        self.resize_factor_box.setAlignment(Qt.AlignCenter)
        self.resize_factor_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.resize_factor_box.setMinimum(1)
        self.resize_factor_box.setMaximum(50)
        self.resize_factor_box.setSingleStep(1)
        self.resize_factor_box.setValue(5)

        self.horizontalLayout.addWidget(self.resize_factor_box)


        self.verticalLayout_7.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_7.addWidget(self.label_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.median_blur_slider = QSlider(self.frame)
        self.median_blur_slider.setObjectName(u"median_blur_slider")
        self.median_blur_slider.setMinimum(1)
        self.median_blur_slider.setMaximum(50)
        self.median_blur_slider.setPageStep(0)
        self.median_blur_slider.setValue(1)
        self.median_blur_slider.setOrientation(Qt.Horizontal)

        self.horizontalLayout_3.addWidget(self.median_blur_slider)

        self.median_blur_box = QSpinBox(self.frame)
        self.median_blur_box.setObjectName(u"median_blur_box")
        self.median_blur_box.setAlignment(Qt.AlignCenter)
        self.median_blur_box.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.median_blur_box.setMinimum(1)
        self.median_blur_box.setMaximum(50)
        self.median_blur_box.setValue(1)

        self.horizontalLayout_3.addWidget(self.median_blur_box)


        self.verticalLayout_7.addLayout(self.horizontalLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer)


        self.verticalLayout_6.addWidget(self.frame)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_8 = QVBoxLayout(self.tab_2)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.tab_2)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 308, 146))
        self.verticalLayout_9 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.screenshot_preview_label = QLabel(self.scrollAreaWidgetContents)
        self.screenshot_preview_label.setObjectName(u"screenshot_preview_label")
        sizePolicy.setHeightForWidth(self.screenshot_preview_label.sizePolicy().hasHeightForWidth())
        self.screenshot_preview_label.setSizePolicy(sizePolicy)

        self.verticalLayout_9.addWidget(self.screenshot_preview_label)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.tabWidget.addTab(self.tab_2, "")

        self.verticalLayout_4.addWidget(self.tabWidget)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        self.groupBox = QGroupBox(self.main_layout_2_frame)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.groupBox.setFont(font3)
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
        self.translate_button.setFont(font2)

        self.verticalLayout.addWidget(self.translate_button)

        self.output_combo_box = QComboBox(self.groupBox)
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
        self.output_combo_box.addItem("")
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

        self.verticalLayout_2.setStretch(1, 2)
        self.verticalLayout_2.setStretch(2, 1)

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
        sizePolicy3.setHeightForWidth(self.fit.sizePolicy().hasHeightForWidth())
        self.fit.setSizePolicy(sizePolicy3)
        icon6 = QIcon()
        icon6.addFile(u":/resources/horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fit.setIcon(icon6)

        self.toolbar_layout.addWidget(self.fit)

        self.zoom_out = QPushButton(self.toolbar_frame)
        self.zoom_out.setObjectName(u"zoom_out")
        sizePolicy3.setHeightForWidth(self.zoom_out.sizePolicy().hasHeightForWidth())
        self.zoom_out.setSizePolicy(sizePolicy3)
        icon7 = QIcon()
        icon7.addFile(u":/resources/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_out.setIcon(icon7)

        self.toolbar_layout.addWidget(self.zoom_out)

        self.zoom_in = QPushButton(self.toolbar_frame)
        self.zoom_in.setObjectName(u"zoom_in")
        sizePolicy3.setHeightForWidth(self.zoom_in.sizePolicy().hasHeightForWidth())
        self.zoom_in.setSizePolicy(sizePolicy3)
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
        self.menubar.setGeometry(QRect(0, 0, 1237, 23))
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
        self.menuAbout.addAction(self.actionDocumentation)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionFit)
        self.menuPage.addAction(self.actionNext_Page)
        self.menuPage.addAction(self.actionPrevious_Page)
        self.menuPage.addAction(self.actionStart_Page)
        self.menuPage.addAction(self.actionLast_Page)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)
        self.input_combo_box.setCurrentIndex(4)
        self.output_combo_box.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comic Lens", None))
        self.actionOpen_PDF.setText(QCoreApplication.translate("MainWindow", u"Open", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.actionFit.setText(QCoreApplication.translate("MainWindow", u"Fit to Page", None))
        self.actionNext_Page.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.actionPrevious_Page.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.actionStart_Page.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.actionLast_Page.setText(QCoreApplication.translate("MainWindow", u"Last Page", None))
        self.actionBox_Screenshot.setText(QCoreApplication.translate("MainWindow", u"Box Screenshot", None))
        self.actionAsd.setText(QCoreApplication.translate("MainWindow", u"Asd", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.actionDocumentation.setText(QCoreApplication.translate("MainWindow", u"Documentation", None))
        self.label_6.setText("")
        self.start_label_1.setText(QCoreApplication.translate("MainWindow", u"1. Open up your favorite book\u2014be it a manga, comics, or even a webcomic. ", None))
        self.start_label_2.setText(QCoreApplication.translate("MainWindow", u"2. Select the language of the book and the output you fancy. Your reading, your rules!", None))
        self.start_label_3.setText(QCoreApplication.translate("MainWindow", u"3. Enable the box selection and start drawing a box around the texts or characters you want to translate! ", None))
        self.open_button.setText(QCoreApplication.translate("MainWindow", u"Open", None))
#if QT_CONFIG(tooltip)
        self.start_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the start page", None))
#endif // QT_CONFIG(tooltip)
        self.start_page.setText("")
#if QT_CONFIG(tooltip)
        self.previous_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the previous page", None))
#endif // QT_CONFIG(tooltip)
        self.previous_page.setText("")
        self.page_spin_box.setSuffix("")
        self.page_spin_box.setPrefix("")
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"of 0", None))
#if QT_CONFIG(tooltip)
        self.next_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the next page", None))
#endif // QT_CONFIG(tooltip)
        self.next_page.setText("")
#if QT_CONFIG(tooltip)
        self.last_page.setToolTip(QCoreApplication.translate("MainWindow", u"Go to the last page", None))
#endif // QT_CONFIG(tooltip)
        self.last_page.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
#if QT_CONFIG(tooltip)
        self.box_button.setToolTip(QCoreApplication.translate("MainWindow", u"Draw a box to select", None))
#endif // QT_CONFIG(tooltip)
        self.box_button.setText(QCoreApplication.translate("MainWindow", u" Box", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"Character Recognition", None))
#if QT_CONFIG(tooltip)
        self.label.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label.setText(QCoreApplication.translate("MainWindow", u"Resize Factor", None))
#if QT_CONFIG(tooltip)
        self.resize_factor_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Adjust the factor by which the image is resized</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.resize_factor_box.setSpecialValueText("")
#if QT_CONFIG(tooltip)
        self.label_2.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Median Blur", None))
#if QT_CONFIG(tooltip)
        self.median_blur_slider.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Adjust the kernel size for median blur</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Settings", None))
        self.screenshot_preview_label.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Preview", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.input_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese - Simplified", None))
        self.input_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese - Simplified (Vertical)", None))
        self.input_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"Chinese - Traditional", None))
        self.input_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"Chinese - Traditional (Vertical)", None))
        self.input_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"English", None))
        self.input_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"French", None))
        self.input_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Indonesian", None))
        self.input_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.input_combo_box.setItemText(8, QCoreApplication.translate("MainWindow", u"Japanese (Vertical)", None))
        self.input_combo_box.setItemText(9, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.input_combo_box.setItemText(10, QCoreApplication.translate("MainWindow", u"Spanish", None))
        self.input_combo_box.setItemText(11, QCoreApplication.translate("MainWindow", u"Spanish - Old", None))

#if QT_CONFIG(tooltip)
        self.input_combo_box.setToolTip(QCoreApplication.translate("MainWindow", u"Change the input's language", None))
#endif // QT_CONFIG(tooltip)
        self.input_combo_box.setCurrentText(QCoreApplication.translate("MainWindow", u"English", None))
#if QT_CONFIG(tooltip)
        self.translate_button.setToolTip(QCoreApplication.translate("MainWindow", u"Re-run the translation", None))
#endif // QT_CONFIG(tooltip)
        self.translate_button.setText(QCoreApplication.translate("MainWindow", u"Translate to", None))
        self.output_combo_box.setItemText(0, QCoreApplication.translate("MainWindow", u"Chinese - Simplified", None))
        self.output_combo_box.setItemText(1, QCoreApplication.translate("MainWindow", u"Chinese - Traditional", None))
        self.output_combo_box.setItemText(2, QCoreApplication.translate("MainWindow", u"English", None))
        self.output_combo_box.setItemText(3, QCoreApplication.translate("MainWindow", u"French", None))
        self.output_combo_box.setItemText(4, QCoreApplication.translate("MainWindow", u"Indonesian", None))
        self.output_combo_box.setItemText(5, QCoreApplication.translate("MainWindow", u"Japanese", None))
        self.output_combo_box.setItemText(6, QCoreApplication.translate("MainWindow", u"Korean", None))
        self.output_combo_box.setItemText(7, QCoreApplication.translate("MainWindow", u"Spanish", None))

#if QT_CONFIG(tooltip)
        self.output_combo_box.setToolTip(QCoreApplication.translate("MainWindow", u"Change the output's language", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.fit.setToolTip(QCoreApplication.translate("MainWindow", u"Fit to the page", None))
#endif // QT_CONFIG(tooltip)
        self.fit.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_out.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom out", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_out.setText("")
#if QT_CONFIG(tooltip)
        self.zoom_in.setToolTip(QCoreApplication.translate("MainWindow", u"Zoom in", None))
#endif // QT_CONFIG(tooltip)
        self.zoom_in.setText("")
        self.current_file_label.setText(QCoreApplication.translate("MainWindow", u"Open a PDF to start.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPage.setTitle(QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi


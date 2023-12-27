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
from PySide6.QtWidgets import (QApplication, QGroupBox, QHBoxLayout, QLabel,
    QLayout, QLineEdit, QMainWindow, QMenu,
    QMenuBar, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)
import rc_resource

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(587, 584)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
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
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy1)
        self.centralwidget.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.main = QHBoxLayout()
        self.main.setObjectName(u"main")
        self.main_layout = QVBoxLayout()
        self.main_layout.setObjectName(u"main_layout")
        self.page_layout = QHBoxLayout()
        self.page_layout.setObjectName(u"page_layout")
        self.page_layout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.page_layout.addWidget(self.label)


        self.main_layout.addLayout(self.page_layout)

        self.page_navigation = QHBoxLayout()
        self.page_navigation.setObjectName(u"page_navigation")
        self.page_navigation.setContentsMargins(0, -1, -1, -1)
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_navigation.addItem(self.horizontalSpacer_3)

        self.start_page = QPushButton(self.centralwidget)
        self.start_page.setObjectName(u"start_page")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.start_page.sizePolicy().hasHeightForWidth())
        self.start_page.setSizePolicy(sizePolicy2)
        icon = QIcon()
        icon.addFile(u":/resources/skip-start-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.start_page.setIcon(icon)

        self.page_navigation.addWidget(self.start_page)

        self.previous_page = QPushButton(self.centralwidget)
        self.previous_page.setObjectName(u"previous_page")
        sizePolicy2.setHeightForWidth(self.previous_page.sizePolicy().hasHeightForWidth())
        self.previous_page.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u":/resources/caret-left-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.previous_page.setIcon(icon1)

        self.page_navigation.addWidget(self.previous_page)

        self.page_line_edit = QLineEdit(self.centralwidget)
        self.page_line_edit.setObjectName(u"page_line_edit")
        sizePolicy2.setHeightForWidth(self.page_line_edit.sizePolicy().hasHeightForWidth())
        self.page_line_edit.setSizePolicy(sizePolicy2)
        self.page_line_edit.setMaximumSize(QSize(25, 16777215))
        self.page_line_edit.setAutoFillBackground(False)
        self.page_line_edit.setAlignment(Qt.AlignCenter)

        self.page_navigation.addWidget(self.page_line_edit)

        self.page_label = QLabel(self.centralwidget)
        self.page_label.setObjectName(u"page_label")

        self.page_navigation.addWidget(self.page_label)

        self.next_page = QPushButton(self.centralwidget)
        self.next_page.setObjectName(u"next_page")
        sizePolicy2.setHeightForWidth(self.next_page.sizePolicy().hasHeightForWidth())
        self.next_page.setSizePolicy(sizePolicy2)
        icon2 = QIcon()
        icon2.addFile(u":/resources/caret-right-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.next_page.setIcon(icon2)

        self.page_navigation.addWidget(self.next_page)

        self.last_page = QPushButton(self.centralwidget)
        self.last_page.setObjectName(u"last_page")
        sizePolicy2.setHeightForWidth(self.last_page.sizePolicy().hasHeightForWidth())
        self.last_page.setSizePolicy(sizePolicy2)
        icon3 = QIcon()
        icon3.addFile(u":/resources/skip-end-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.last_page.setIcon(icon3)

        self.page_navigation.addWidget(self.last_page)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.page_navigation.addItem(self.horizontalSpacer_2)


        self.main_layout.addLayout(self.page_navigation)

        self.main_layout.setStretch(0, 1)

        self.main.addLayout(self.main_layout)

        self.main_layout_2 = QVBoxLayout()
        self.main_layout_2.setObjectName(u"main_layout_2")
        self.main_layout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.horizontalLayout_2 = QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.box_screenshot = QPushButton(self.groupBox_2)
        self.box_screenshot.setObjectName(u"box_screenshot")
        icon4 = QIcon()
        icon4.addFile(u":/resources/bounding-box-circles.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.box_screenshot.setIcon(icon4)
        self.box_screenshot.setCheckable(True)

        self.horizontalLayout_2.addWidget(self.box_screenshot)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.main_layout_2.addWidget(self.groupBox_2)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy3)
        self.groupBox.setMinimumSize(QSize(250, 0))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")

        self.main_layout_2.addWidget(self.groupBox)

        self.main_layout_2.setStretch(1, 1)

        self.main.addLayout(self.main_layout_2)

        self.main.setStretch(0, 2)
        self.main.setStretch(1, 1)

        self.verticalLayout_3.addLayout(self.main)

        self.toolbar = QHBoxLayout()
        self.toolbar.setObjectName(u"toolbar")
        self.toolbar.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.toolbar_layout = QHBoxLayout()
        self.toolbar_layout.setObjectName(u"toolbar_layout")
        self.toolbar_layout.setContentsMargins(-1, -1, 0, -1)
        self.fit = QPushButton(self.centralwidget)
        self.fit.setObjectName(u"fit")
        sizePolicy2.setHeightForWidth(self.fit.sizePolicy().hasHeightForWidth())
        self.fit.setSizePolicy(sizePolicy2)
        icon5 = QIcon()
        icon5.addFile(u":/resources/horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.fit.setIcon(icon5)

        self.toolbar_layout.addWidget(self.fit)

        self.zoom_out = QPushButton(self.centralwidget)
        self.zoom_out.setObjectName(u"zoom_out")
        sizePolicy2.setHeightForWidth(self.zoom_out.sizePolicy().hasHeightForWidth())
        self.zoom_out.setSizePolicy(sizePolicy2)
        icon6 = QIcon()
        icon6.addFile(u":/resources/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_out.setIcon(icon6)

        self.toolbar_layout.addWidget(self.zoom_out)

        self.zoom_in = QPushButton(self.centralwidget)
        self.zoom_in.setObjectName(u"zoom_in")
        sizePolicy2.setHeightForWidth(self.zoom_in.sizePolicy().hasHeightForWidth())
        self.zoom_in.setSizePolicy(sizePolicy2)
        icon7 = QIcon()
        icon7.addFile(u":/resources/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.zoom_in.setIcon(icon7)

        self.toolbar_layout.addWidget(self.zoom_in)


        self.toolbar.addLayout(self.toolbar_layout)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.toolbar.addItem(self.horizontalSpacer)

        self.current_file_label = QLabel(self.centralwidget)
        self.current_file_label.setObjectName(u"current_file_label")

        self.toolbar.addWidget(self.current_file_label)


        self.verticalLayout_3.addLayout(self.toolbar)

        self.verticalLayout_3.setStretch(0, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 587, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuPage = QMenu(self.menubar)
        self.menuPage.setObjectName(u"menuPage")
        self.menuTranslation = QMenu(self.menubar)
        self.menuTranslation.setObjectName(u"menuTranslation")
        MainWindow.setMenuBar(self.menubar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPage.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuTranslation.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.menuFile.addAction(self.actionOpen_PDF)
        self.menuView.addAction(self.actionZoom_In)
        self.menuView.addAction(self.actionZoom_Out)
        self.menuView.addAction(self.actionFit)
        self.menuPage.addAction(self.actionNext_Page)
        self.menuPage.addAction(self.actionPrevious_Page)
        self.menuPage.addAction(self.actionStart_Page)
        self.menuPage.addAction(self.actionLast_Page)
        self.menuTranslation.addAction(self.actionBox_Screenshot)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Comic Lens", None))
        self.actionOpen_PDF.setText(QCoreApplication.translate("MainWindow", u"Open PDF", None))
        self.actionZoom_In.setText(QCoreApplication.translate("MainWindow", u"Zoom In", None))
        self.actionZoom_Out.setText(QCoreApplication.translate("MainWindow", u"Zoom Out", None))
        self.actionFit.setText(QCoreApplication.translate("MainWindow", u"Fit", None))
        self.actionNext_Page.setText(QCoreApplication.translate("MainWindow", u"Next Page", None))
        self.actionPrevious_Page.setText(QCoreApplication.translate("MainWindow", u"Previous Page", None))
        self.actionStart_Page.setText(QCoreApplication.translate("MainWindow", u"Start Page", None))
        self.actionLast_Page.setText(QCoreApplication.translate("MainWindow", u"Last Page", None))
        self.actionBox_Screenshot.setText(QCoreApplication.translate("MainWindow", u"Box Screenshot", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.start_page.setText("")
        self.previous_page.setText("")
        self.page_label.setText(QCoreApplication.translate("MainWindow", u"of", None))
        self.next_page.setText("")
        self.last_page.setText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
        self.box_screenshot.setText(QCoreApplication.translate("MainWindow", u"Box Screenshot", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.fit.setText("")
        self.zoom_out.setText("")
        self.zoom_in.setText("")
        self.current_file_label.setText(QCoreApplication.translate("MainWindow", u"Open a PDF to start.", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPage.setTitle(QCoreApplication.translate("MainWindow", u"Page", None))
        self.menuTranslation.setTitle(QCoreApplication.translate("MainWindow", u"Selection", None))
    # retranslateUi


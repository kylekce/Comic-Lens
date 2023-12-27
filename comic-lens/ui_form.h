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
from PySide6.QtWidgets import (QApplication, QGridLayout, QGroupBox, QHBoxLayout,
    QLayout, QMainWindow, QMenu, QMenuBar,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(970, 695)
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.actionOpen_PDF = QAction(MainWindow)
        self.actionOpen_PDF.setObjectName(u"actionOpen_PDF")
        self.actionZoom_In = QAction(MainWindow)
        self.actionZoom_In.setObjectName(u"actionZoom_In")
        icon = QIcon()
        icon.addFile(u":/resources/zoom-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_In.setIcon(icon)
        self.actionZoom_Out = QAction(MainWindow)
        self.actionZoom_Out.setObjectName(u"actionZoom_Out")
        icon1 = QIcon()
        icon1.addFile(u":/resources/zoom-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionZoom_Out.setIcon(icon1)
        self.actionFit = QAction(MainWindow)
        self.actionFit.setObjectName(u"actionFit")
        icon2 = QIcon()
        icon2.addFile(u":/resources/horizontal.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionFit.setIcon(icon2)
        self.actionNext_Page = QAction(MainWindow)
        self.actionNext_Page.setObjectName(u"actionNext_Page")
        icon3 = QIcon()
        icon3.addFile(u":/resources/caret-right-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNext_Page.setIcon(icon3)
        self.actionPrevious_Page = QAction(MainWindow)
        self.actionPrevious_Page.setObjectName(u"actionPrevious_Page")
        icon4 = QIcon()
        icon4.addFile(u":/resources/caret-left-fill.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrevious_Page.setIcon(icon4)
        self.actionStart_Page = QAction(MainWindow)
        self.actionStart_Page.setObjectName(u"actionStart_Page")
        icon5 = QIcon()
        icon5.addFile(u":/resources/backward-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStart_Page.setIcon(icon5)
        self.actionLast_Page = QAction(MainWindow)
        self.actionLast_Page.setObjectName(u"actionLast_Page")
        icon6 = QIcon()
        icon6.addFile(u":/resources/forward-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.actionLast_Page.setIcon(icon6)
        self.actionSpacer = QAction(MainWindow)
        self.actionSpacer.setObjectName(u"actionSpacer")
        self.actionSpacer.setEnabled(False)
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
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy2)
        self.groupBox.setMinimumSize(QSize(250, 0))

        self.verticalLayout.addWidget(self.groupBox)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 970, 25))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuAbout = QMenu(self.menubar)
        self.menuAbout.setObjectName(u"menuAbout")
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
        self.actionSpacer.setText("")
#if QT_CONFIG(statustip)
        self.actionSpacer.setStatusTip("")
#endif // QT_CONFIG(statustip)
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"Translation", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"File", None))
        self.menuAbout.setTitle(QCoreApplication.translate("MainWindow", u"About", None))
        self.menuView.setTitle(QCoreApplication.translate("MainWindow", u"View", None))
        self.menuPage.setTitle(QCoreApplication.translate("MainWindow", u"Page", None))
    # retranslateUi


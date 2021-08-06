import os
import sys
# pip install PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
# pip install PyQtWebEngine
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl('http://google.com'))
        self.setCentralWidget(self.browser)
        self.showMaximized()


        # navbar
        navbar = QToolBar()
        self.addToolBar(navbar)

        # BACK BUTTON
        back_btn = QAction('Back', self)
        back_btn.triggered.connect(self.browser.back)
        navbar.addAction(back_btn)

        # FORWARD BUTTON
        forward_btn = QAction('Forward', self)
        forward_btn.triggered.connect(self.browser.forward)
        navbar.addAction(forward_btn)

        # RELOAD BUTTON
        reload_btn = QAction('reload', self)
        reload_btn.triggered.connect(self.browser.reload)
        navbar.addAction(reload_btn)

        # HOME BUTTON
        home_btn = QAction('Home', self)
        home_btn.triggered.connect(self.navigate_home)
        navbar.addAction(home_btn)

        # STOP BUTTON
        stop_btn = QAction('Stop', self)
        stop_btn.setStatusTip('Stop loading current page')
        navbar.addAction(stop_btn)

        # ADD SEPARATOR TO NAVIGATOR BAR
        navbar.addSeparator()


        # SECURITY ICON
        # self.httpsicon = QLabel()
        # self.httpsicon.setPixmap(QPixmap(os.path.join('icons', 'cli-lock-unlocked.png')))
        # navbar.addWidget(self.httpsicon)


        # URL BAR
        self.url_bar = QLineEdit()
        self.url_bar.returnPressed.connect(self.navigate_to_url)
        navbar.addWidget(self.url_bar)
        self.browser.urlChanged.connect(self.update_url)

        # TOP MENU
        # FILE MENU
        file_menu = self.menuBar().addMenu("&File")

        # MENU ACTIONS
        # new_tab_action = QAction(QIcon(os.path.join('icons', 'cli-library-add.png')))
        # new_tab_action.setStatusTip("Open a new tab")
        # file_menu.addAction(new_tab_action)

        # HELP MENU
        help_menu = self.menuBar().addMenu("&Help")
        # TOOLS MENU
        tools_menu = self.menuBar().addMenu("&Tools")




    def navigate_home(self):
        self.browser.setUrl(QUrl('http://youtube.com'))

    def navigate_to_url(self):
        url = self.url_bar.text()
        self.browser.setUrl(QUrl(url))

    def update_url(self, q):
        self.url_bar.setText(q.toString())


app = QApplication(sys.argv)
QApplication.setApplicationName('OPTIMAL')
window = MainWindow()
app.exec_()

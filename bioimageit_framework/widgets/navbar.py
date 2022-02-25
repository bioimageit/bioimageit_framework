import qtpy.QtCore
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import (QLineEdit, QHBoxLayout, QWidget, QToolButton)

from .widget import BiWidget
from bioimageit_framework.theme import BiThemeAccess

class BiNavigationBar(BiWidget):
    PREVIOUS = 'previous'
    NEXT = 'next'
    HOME = 'home'
    EDIT = 'edit'

    def __init__(self):
        super().__init__()

        widget = QWidget(self.widget)
        globalLayout = QHBoxLayout()
        globalLayout.setContentsMargins(0,0,0,0)
        self.widget.setLayout(globalLayout)
        globalLayout.addWidget(widget)

        layout = QHBoxLayout()
        layout.setSpacing(2)
        widget.setLayout(layout)
        widget.setAttribute(qtpy.QtCore.Qt.WA_StyledBackground, True)
        widget.setObjectName("bi-toolbar")

        # previous
        previousButton = QToolButton()
        previousButton.setIcon(QIcon(BiThemeAccess.instance().icon('arrow-left')))
        previousButton.setObjectName("bi-navigation-bar-previous")
        previousButton.setToolTip(self.widget.tr("Previous"))
        previousButton.released.connect(self.previous)
        layout.addWidget(previousButton, 0, qtpy.QtCore.Qt.AlignLeft)

        # next
        nextButton = QToolButton()
        nextButton.setIcon(QIcon(BiThemeAccess.instance().icon('arrow-right')))
        nextButton.setToolTip(self.widget.tr("Next"))
        nextButton.released.connect(self.next)
        layout.addWidget(nextButton, 0, qtpy.QtCore.Qt.AlignLeft)

        # home
        homeButton = QToolButton()
        homeButton.setIcon(QIcon(BiThemeAccess.instance().icon('home')))
        homeButton.setToolTip(self.widget.tr("Home"))
        homeButton.released.connect(self.home)
        layout.addWidget(homeButton, 0, qtpy.QtCore.Qt.AlignLeft)

        # bar
        self.lineEdit = QLineEdit()
        self.lineEdit.setAttribute(qtpy.QtCore.Qt.WA_MacShowFocusRect, False)
        self.lineEdit.returnPressed.connect(self.edit)
        layout.addWidget(self.lineEdit, 1)

    def set_path(self, path: str):
        self.lineEdit.setText(path)

    def path(self):
        self.lineEdit.text()    

    def previous(self):
        self.emit(BiNavigationBar.PREVIOUS)

    def next(self):
        self.emit(BiNavigationBar.NEXT)   

    def home(self):
        self.emit(BiNavigationBar.HOME)   

    def edit(self):
        self.emit(BiNavigationBar.EDIT)

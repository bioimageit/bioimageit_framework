import qtpy.QtCore
from qtpy.QtGui import QIcon
from qtpy.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout

from .widget import BiWidget
from .buttons import BiClosableButton

class BiAppBar(BiWidget):
    OPEN = 'open'
    CLOSE = 'close'

    def __init__(self):
        super().__init__()
        self.clicked_id = None
        self.current_tab_id = -1
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(QWidget(), 1, qtpy.QtCore.Qt.AlignTop)

        # global
        layout = QHBoxLayout()
        w = QWidget()
        w.setObjectName("bi-app-toolbar")
        layout.addWidget(w, 1, qtpy.QtCore.Qt.AlignHCenter)
        layout.setContentsMargins(0, 7, 0, 0)
        w.setLayout(self.layout)

        # total
        tlayout = QHBoxLayout()
        wt = QWidget()
        tlayout.addWidget(wt, 1, qtpy.QtCore.Qt.AlignHCenter)
        tlayout.setContentsMargins(0, 0, 0, 0)
        wt.setLayout(layout)
        wt.setObjectName("bi-app-toolbar")
        wt.setFixedWidth(52)
        self.widget.setObjectName("bi-app-toolbar")
        self.widget.setFixedWidth(52)
        self.widget.setLayout(tlayout)

    def add_button(self, icon: str, toolTip: str, id: int, closable: bool):
        button = BiClosableButton(closable)
        button.setObjectName('bi-app-toolbar-button')
        button.setCheckable(True)
        button.setIcon(QIcon(icon))
        if (toolTip != ""):
            button.setToolTip(toolTip)
        button.setId(id)
        self.layout.insertWidget(self.layout.count() -1, button, 0, qtpy.QtCore.Qt.AlignHCenter)

        button.clicked.connect(self.open)
        button.closed.connect(self.close)

    def open(self, id):
        self.current_tab_id = id
        self.emit(BiAppBar.OPEN)

    def close(self, id):
        self.current_tab_id = id
        self.emit(BiAppBar.CLOSE)    

    def print_buttons(self):
        for i in range(self.layout.count()-1, -1, -1):
            item = self.layout.itemAt(i)
            button = item.widget()
            if button:
                if isinstance(button, BiClosableButton):
                    print("button:", button.id())

    def remove_button(self, id: int):
        for i in range(self.layout.count()-1, -1, -1):
            item = self.layout.itemAt(i)
            button = item.widget()
            if button:
                if isinstance(button, BiClosableButton):
                    if (button.id() == id):
                        button.deleteLater()
                    #elif button.id() > id:
                    #    button.id = button.id()-1              

    def set_checked(self, id: int, update_current: bool):
        self.current_tab_id = id
        for i in range(0, self.layout.count()):
            button = self.layout.itemAt(i).widget()
            if isinstance(button, BiClosableButton):
                if button.id() == id and update_current:
                    button.setChecked(True)   
                else:
                    button.setChecked(False)


class BiAppMainWidget(BiWidget):
    AppTabCanged = 'app_tab_changed'

    def __init__(self):
        super().__init__()
        self.current_id = 0
        self.app_bar = BiAppBar()
        self.central_area = QWidget()
        self.central_layout = QVBoxLayout()
        self.central_layout.setContentsMargins(0, 0, 0, 0)
        self.central_area.setLayout(self.central_layout)
        
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.addWidget(self.app_bar.widget)
        self.layout.addWidget(self.central_area)
        self.widget.setLayout(self.layout)

        self._widgets = []
        self._count = -1

        self.app_bar.connect(BiAppBar.OPEN, self._open)
        self.app_bar.connect(BiAppBar.CLOSE, self._close)

    def add(self, widget, icon, tooltip, closable=False):
        self._count += 1    
        self._widgets.append({'id': self._count, 'widget': widget})
        self.central_layout.addWidget(widget.widget)
        self.app_bar.add_button(icon, tooltip, self._count, closable)
        self.open(self._count, False)
        self.app_bar.set_checked(self._count, update_current=True)
        return self._count

    def open(self, id, update_current=True):
        self.current_id = id
        self.app_bar.set_checked(id, update_current=update_current)        
        for i in range(self.central_layout.count()):
            item = self.central_layout.itemAt(i)
            widget = item.widget()
            if widget:
                if i == id:
                    widget.setVisible(True)
                else:
                    widget.setVisible(False) 
        self.emit(BiAppMainWidget.AppTabCanged)            

    def _open(self, origin):
        id = origin.current_tab_id
        self.open(id, False)
   
    def _close(self, origin):
        idx = origin.current_tab_id
        print('close button id=', idx)
        self.app_bar.remove_button(idx)
        
        for i in range(self.central_layout.count()):
            item = self.central_layout.itemAt(i)
            widget = item.widget()
            if widget == self._widgets[idx]:
                widget.deleteLater()

        self._widgets.pop(idx)
        self.open(0, True)
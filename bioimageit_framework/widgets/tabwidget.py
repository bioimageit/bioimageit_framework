from qtpy.QtWidgets import QWidget, QVBoxLayout

from .widget import BiWidget
from .toolbars import BiToolBar


class BiTabWidget(BiWidget):
    def __init__(self):
        super().__init__()
        self.name = 'BiTabWidget'
        self.widget = QWidget()
        self.widget.setObjectName('BiTabWidget')
        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.widget.setLayout(self.layout)
        # internal list of widgets
        self.widgets = []
        # toolbar
        self.toolbar = BiToolBar()
        self.layout.addWidget(self.toolbar.widget)
        # widgets area
        self.widgetsarea = QWidget()
        self.widgetsarea.setContentsMargins(0, 0, 0, 0)
        self.widgets_area_layout = QVBoxLayout()
        self.widgetsarea.setLayout(self.widgets_area_layout)
        self.layout.addWidget(self.widgetsarea)

    def add_tab(self, widget, name, tooltip=''):
        """Add a new widget to the tab
        
        Parameters
        ----------
        widget: BiWidget
            Widget to add
        name: str
            Name of the widget in the toolbar
        tooltip: str
            Tooltip displayed when the mouse pointer is over the tool button

        """ 
        self.widgets_area_layout.addWidget(widget.widget)
        self.toolbar.add_pushbutton(name, '', tooltip)
        self.widgets.append({'name': name, 'widget': widget})
        self.toolbar.connect(name, self._switch)

    def switch_tab(self, id):
        """Switch the view to a specific tab"""
        self.toolbar.switch(id)
        for widget_info in self.widgets:
            if widget_info['name'] == id:
                widget_info['widget'].set_visible(True)
            else:
                widget_info['widget'].set_visible(False) 

    def _switch(self, origin):
        for widget_info in self.widgets:
            if widget_info['name'] == origin.active_item:
                widget_info['widget'].set_visible(True)
            else:
                widget_info['widget'].set_visible(False)    

import os
import sys

import qtpy.QtCore
from qtpy.QtWidgets import QApplication, QWidget, QVBoxLayout

from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiButtonDanger, BiFileSelector, BiGroupBox, BiLineEdit




if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load the theme
    BiThemeAccess(os.path.join(dir_path, 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    # build the widget
    widget = QWidget()
    layout = QVBoxLayout()
    widget.setLayout(layout)

    w1 = BiButtonDanger('This is a danger button', popup=True)
    w2 = BiFileSelector()
    group_box1 = BiGroupBox('Group 1')
    group1_layout = QVBoxLayout()
    group_box1.setLayout(group1_layout)
    group1_layout.addWidget(w1)
    group1_layout.addWidget(w2)
    group1_layout.addWidget(BiLineEdit())

    layout.addWidget(group_box1)
    layout.addWidget(QWidget(), 1, qtpy.QtCore.Qt.AlignTop)
    widget.show()
 
    # Run the main Qt loop
    sys.exit(app.exec_())

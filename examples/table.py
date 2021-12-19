import sys
import os
from qtpy.QtWidgets import QApplication

from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiTable


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load and set the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    headers = ['x', 'y', 'z']
    data = [[12, 26, 2], [14, 27, 3], [16, 28, 4]]

    table = BiTable()
    # Header
    table.set_header(headers)
    # Set a matrix content
    table.set_data(data)
    # Add an extra line
    table.add_line([17, 25, 3])

    table.widget.show() 
 
    # Run the main Qt loop
    sys.exit(app.exec_())

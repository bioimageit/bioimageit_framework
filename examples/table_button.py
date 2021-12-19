import sys
import os
from qtpy.QtWidgets import QApplication

from bioimageit_framework.theme import BiThemeAccess, BiThemeSheets
from bioimageit_framework.widgets import BiWidget, BiTable, showInfoBox


class MyExampleTable(BiWidget):
    """Create a table with an open button in the first row

    Parameters
    ----------
    header: list
        List of the header labels
    data: ndarray
        data matrix    
    """
    def __init__(self, headers, data):
        self.table = BiTable()
        self.widget = self.table.widget

        self.table.prepare_header(headers)
        self.table.prepare_data(data)
        self.table.prepare_col_button(0, 'primary', 'Open', self.open)
        self.table.build()

    def open(self, emitter): 
        showInfoBox(f'you clicked the button open row {emitter.content["row"]}')          


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(["BioImageIT"])
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # load and set the theme
    BiThemeAccess(os.path.join(dir_path, '..', 'theme', 'dark'))
    BiThemeAccess.instance().set_stylesheet(app, BiThemeSheets.sheets())

    headers = ['', 'x', 'y', 'z']
    data = [[12, 26, 2], [14, 27, 3], [16, 28, 4]]
    table = MyExampleTable(headers, data)
    table.widget.show() 
 
    # Run the main Qt loop
    sys.exit(app.exec_())

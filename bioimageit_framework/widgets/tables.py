

from qtpy.QtWidgets import QTableWidget, QAbstractItemView, QTableWidgetItem, QPushButton, QTableWidget

from bioimageit_framework.widgets import BiButtonPrimary


class BiTable:
    def __init__(self):
        self.name = 'table'
        self._prepare = {'headers': [], 'data': [], 'col_btns': []}
        self._buttons = []

        self.widget = QTableWidget()
        self.widget.setAlternatingRowColors(True)
        self.widget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.widget.horizontalHeader().setStretchLastSection(True)
        self.widget.verticalHeader().setVisible(False) 
        

    def set_header(self, labels):
        """set the header labels

        Parameters
        ----------
        labels: list
            List of the header labels
        """
        self.widget.setColumnCount(len(labels))
        self.widget.setHorizontalHeaderLabels(labels)

    def set_data(self, data):

        self.widget.setRowCount(0)
        self.widget.setRowCount(len(data))
          
        row_id = -1 
        for row in data:
            row_id += 1
            col_id = -1
            for item in row: 
                col_id += 1
                self.widget.setItem(row_id, col_id, QTableWidgetItem(str(item)))

    def add_line(self, data):
        row_id = self.widget.rowCount()
        self.widget.setRowCount(row_id+1)
        col_id = -1
        for item in data:
            col_id += 1
            self.widget.setItem(row_id, col_id, QTableWidgetItem(str(item)))

    def reserve_line(self):
        self.widget.setRowCount(self.widget.rowCount()+1)  

    def resize(self, row, col=None):
        self.widget.setRowCount(row)
        if col:
            self.widget.setColumnCount(col)

    def set_item(self, row, col, item):
        self.widget.setItem(row, col, QTableWidgetItem(str(item)))   

    def set_widget(self, row, col, widget):
        self.widget.setCellWidget(row, col, widget)                   

    def prepare_header(self, headers):
        self._prepare['headers'] = headers 

    def prepare_data(self, data):    
        self._prepare['data'] = data

    def prepare_col_button(self, col, type, title, callback):
        self._prepare['col_btns'].append({'col': col, 'type':type, 'title': title, 'callback': callback})

    def build(self):
        # set the header
        col_count = len(self._prepare['headers'])
        self.set_header(self._prepare['headers'])

        # init rows
        row_count = len(self._prepare['data'])
        self.widget.setRowCount(0)
        self.widget.setRowCount(row_count)

        # add the buttons
        for btn in self._prepare['col_btns']:
            col = btn['col']
            for row in range(row_count):
                btn_w = BiButtonPrimary(btn['title'])
                btn_w.connect(BiButtonPrimary.CLICKED, btn['callback'])
                btn_w.content['row'] = row
                self._buttons.append(btn_w)
                self.set_widget(row, col, btn_w.widget)

        # add the data
        row_id = -1 
        for row in self._prepare['data']:
            row_id += 1
            col_id = -1 + len(self._prepare['col_btns'])
            for item in row: 
                col_id += 1
                self.widget.setItem(row_id, col_id, QTableWidgetItem(str(item)))

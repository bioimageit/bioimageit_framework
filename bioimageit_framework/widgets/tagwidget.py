import qtpy.QtCore
from qtpy.QtWidgets import QWidget, QHBoxLayout, QLineEdit, QPushButton

from .widget import BiWidget


class BiTagWidget(BiWidget):
    REMOVE = 'remove'

    def __init__(self):
        super().__init__()

        self.tag_to_remove = None
        layout = QHBoxLayout()
        layout.setContentsMargins(0,0,0,0)
        self.tag_name = QLineEdit()
        self.tag_name.setReadOnly(True)
        layout.addWidget(self.tag_name)
        removeButton = QPushButton(self.tr("Remove"))
        removeButton.setObjectName("btn-danger")
        layout.addWidget(removeButton, 0, qtpy.QtCore.Qt.AlignRight)
        removeButton.released.connect(self.emit_remove)

        self.widget.setLayout(layout)

    def set_content(self, content: str):
        self.tag_name.setText(content)

    def content(self) -> str:
        return self.tag_name.text()

    def emit_remove(self):
        self.tag_to_remove = self.tag_name.text()
        self._emit(BiTagWidget.REMOVE)

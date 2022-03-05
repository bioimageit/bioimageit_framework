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
        self._tag_name = QLineEdit()
        self._tag_name.setReadOnly(True)
        layout.addWidget(self._tag_name)
        removeButton = QPushButton(self.widget.tr("Remove"))
        removeButton.setObjectName("btn-danger")
        layout.addWidget(removeButton, 0, qtpy.QtCore.Qt.AlignRight)
        removeButton.released.connect(self.emit_remove)

        self.widget.setLayout(layout)

    def set_tag_name(self, content: str):
        self._tag_name.setText(content)

    def tag_name(self) -> str:
        return self._tag_name.text()

    def emit_remove(self):
        self.tag_to_remove = self._tag_name.text()
        self._emit(BiTagWidget.REMOVE)

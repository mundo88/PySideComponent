from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from .AccordionItem import AccordionItem

class Accordion(QFrame):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)
        self.layout.setAlignment(Qt.AlignTop)
        self.setObjectName('accordion')
        self.items:list[AccordionItem] = []
    def addItem(self,item:AccordionItem):
        self.layout.addWidget(item)
        self.items.append(item)
        
    
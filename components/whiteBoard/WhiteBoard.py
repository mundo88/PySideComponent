from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS





class WhiteBoard(QFrame):
    style = {
        "background-color": TAILWIND_COLORS.WHITE,
        "border-radius": "12px",
        "border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
    }
    class ShadowValue(Enum):
        sm = 10
        md = 20
        lg = 30
        xl = 40
    def __init__(self,
            parent:QWidget=None,
            shadow:ShadowValue=ShadowValue.md.name,
            padding:QMargins=QMargins(16,16,16,16),
            gap:int=0,
        ):
        super().__init__(parent=parent)
        self.shadow = shadow
        self.padding = padding
        self.gap = gap
        
        self.initUi()
        self.initContainer()
        
    def initContainer(self):
        self.container = QWidget(self)
        containerObjectName = f"{self.objectName()}_container"
        self.container.setObjectName(containerObjectName)
        self.containerLayout = QVBoxLayout(self.container)
        self.containerLayout.setContentsMargins(self.padding)
        self.containerLayout.setSpacing(self.gap)
        self.container.setLayout(self.containerLayout)
        self.scrollBar = QScrollArea()
        self.scrollBar.setWidgetResizable(True)
        self.scrollBar.setMinimumHeight(360)
        self.scrollBar.setWidget(self.container)
        self.layout.addWidget(self.scrollBar)
        
    def initUi(self):
        objectName = "whiteBoard_"+uuid.uuid4().hex
        self.setObjectName(objectName)
        scrollBarQss = """
            QWidget {
                border: none;
                background: transparent;
            }
            QScrollBar:horizontal {
                border: none;
                background: white;
                height: 8px;
                margin: 0px;
                border-radius: 0px;
            }
            QScrollBar::handle:horizontal {
                background: #d4d4d8;
                min-width: 25px;
                border-radius: 4px
            }
            QScrollBar::handle:horizontal::hover {
                background: #9ca3af;
                min-width: 25px;
                border-radius: 4px
            }
            QScrollBar::add-line:horizontal {
                width: 0;
            }
            QScrollBar::sub-line:horizontal {
                width: 0;
            }
            QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
            {
                background: none;
            }
            QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
            {
                background: none;
            }
            QScrollBar:vertical {
                border: none;
                background: white;
                width: 8px;
                margin: 0;
                border-radius: 0px;
            }
            
            QScrollBar::handle:vertical {	
                background: #d4d4d8;
                min-height: 25px;
                border-radius: 4px
            }
            QScrollBar::handle:vertical::hover {	
                background: #9ca3af;
            }
            QScrollBar::add-line:vertical {
                height: 0px;
            }
            QScrollBar::sub-line:vertical {
                height: 0px;
            }
            QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {
                background: none;
            }

            QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
                background: none;
            }
        """
        qss = QssParse.toQss(f"QFrame#{objectName}",self.style) + scrollBarQss
        self.setStyleSheet(qss)
        
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(4,4,4,4)
        self.setLayout(self.layout)
        self.layout.setSpacing(0)
        if self.shadow:
            self.initShadow()
    def addWidget(self,widget:QWidget):
        self.containerLayout.addWidget(widget)
    def removeWidget(self,widget:QWidget):
        self.containerLayout.removeWidget(widget)
    def initShadow(self):
        shadowValue = self.ShadowValue[self.shadow].value
        self.shadowEffect = QGraphicsDropShadowEffect(self)
        self.shadowEffect.setBlurRadius(10)
        self.shadowEffect.setXOffset(0)
        self.shadowEffect.setYOffset(1)
        self.shadowEffect.setColor(QColor(0, 0, 0, shadowValue))
        self.setGraphicsEffect(self.shadowEffect)

    def gap(self):
        return self.containerLayout.spacing()
    def setGap(self,gap:int):
        self.containerLayout.setSpacing(gap)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setFont(QFont("Inter", 14))
    window = QWidget()
    window.resize(800, 600)
    card = WhiteBoard(window)
    card.setGeometry(100, 100, 300, 200)
    window.show()
    sys.exit(app.exec())
from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS





class Card(QFrame):
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
    def __init__(self,parent:QWidget=None,shadow:ShadowValue=ShadowValue.md.name):
        super().__init__(parent=parent)
        self._shadow = shadow
        objectName = "card_"+uuid.uuid4().hex
        self.setObjectName(objectName)

        if self._shadow:
            self.initShadow()
        
        self.setStyleSheet(QssParse.toQss(f"QFrame#{objectName}",self.style))
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(24,24,24,24)
        self.setLayout(self.layout)
        self.layout.setSpacing(16)
    def initShadow(self):
        shadowValue = self.ShadowValue[self._shadow].value
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(10)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(1)
        self.shadow.setColor(QColor(0, 0, 0, shadowValue))
        self.setGraphicsEffect(self.shadow)
        
    def initWidgets(self):
        self.card_header = CardHeader(self)
        self.card_title = CardTitle(self)
        self.card_description = CardDescription(self)

        self.card_header.layout.addWidget(self.card_title)
        self.card_header.layout.addWidget(self.card_description)

        self.layout.addWidget(self.card_header)


class CardHeader(QFrame):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent=parent)
        self.setObjectName("card_header_"+uuid.uuid4().hex)
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0,0,0,0)
        self.layout.setSpacing(4)
        self.setLayout(self.layout)       
        self.layout.setAlignment(Qt.AlignTop)
         
class CardTitle(QLabel):
    style = {
        "font-size": "16px",
        "font-weight": "600",
        "font-family": "Inter",
        "color": TAILWIND_COLORS.ZINC_900,
    }
    def __init__(self,parent:QWidget=None,text:str='Create project'):
        super().__init__(parent=parent)
        self._text = text
        self.setObjectName("card_title_"+uuid.uuid4().hex)
        self.setText(text)
        self.setWordWrap(True)
        self.setStyleSheet(QssParse.toQss(f"QLabel#{self.objectName()}",self.style))
        
class CardDescription(QLabel):
    style = {
        "font-size": "14px",
        "font-weight": "500",
        "font-family": "Inter",
        "color": TAILWIND_COLORS.ZINC_500,
    }
    def __init__(self,parent:QWidget=None,text:str="Deploy your new project in one-click."):
        super().__init__(parent=parent)
        self._text = text
        self.setObjectName("card_description_"+uuid.uuid4().hex)
        self.setText(text)
        self.setWordWrap(True)
        self.setStyleSheet(QssParse.toQss(f"QLabel#{self.objectName()}",self.style))
        
class CardContent(QFrame):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent=parent)
        self.setObjectName("card_content_"+uuid.uuid4().hex)
class CardFooter(QFrame):
    def __init__(self,parent:QWidget=None):
        super().__init__(parent=parent)
        self.setObjectName("card_footer_"+uuid.uuid4().hex)
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setFont(QFont("Inter", 14))
    window = QWidget()
    window.resize(800, 600)
    card = Card(window)
    card.initWidgets()
    card.show()
    window.show()
    sys.exit(app.exec())
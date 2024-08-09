from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from typing import Callable
from PySideComponent.components import Button


class Input(QLineEdit):
    styleSignal = Signal(str)
    onDisableChange = Signal(bool)
    onKeyPressed = Signal(QEvent)
    class Style:
        base = {
            "background-color": TAILWIND_COLORS.WHITE,
            "outline": TAILWIND_COLORS.NONE,
            "border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
            "border-radius": "6px",
            "padding": "7px 12px",
            "font-size": "14px",
            "color": TAILWIND_COLORS.ZINC_700,
            'font-weight': "550",
        }
        focus = {
            "border": f"1px solid {TAILWIND_COLORS.ZINC_500}",
        }
        disabled =   {
            "border": f"1px solid {TAILWIND_COLORS.ZINC_100}",
            "color": TAILWIND_COLORS.ZINC_400,
        }
    def __init__(
            self,parent:QWidget=None,
            value:str="",placeholder:str=None,
            onChange:Callable = None,
            disabled:bool=False,
            disableChanged:Callable=None,
            isPasswordField:bool=False,
        ):
        super().__init__(parent=parent)
        self._placeholder = placeholder
        self.disabled = disabled
        objectName = "input_"+uuid.uuid4().hex
        self.setObjectName(objectName)
        
        self.baseStyle = QssParse.toQss(f"QLineEdit#{objectName}",self.Style.base)
        self.focusStyle = QssParse.toQss(f"QLineEdit#{objectName}:focus",self.Style.focus)
        self.disableStyle = QssParse.toQss(f"QLineEdit#{objectName}:disabled",self.Style.disabled)
        self._textStyle = self.baseStyle + self.focusStyle + self.disableStyle
        
        self.setStyle(self._textStyle)
        self.setText(value)
        self.setPlaceholderText(placeholder)
        self.textChanged.connect(onChange)
        self.styleSignal.connect(self.setStyle)
        self.setDisabled(disabled)
        self._isPasswordField = isPasswordField
        if isPasswordField:
            self.setEchoMode(QLineEdit.Password)
    @property
    def textStyle(self):
        return self._textStyle
    @textStyle.setter
    def textStyle(self,value):
        self._textStyle = value
        self.styleSignal.emit(value)
    @Slot(str)
    def setStyle(self,textStyle):
        self.setStyleSheet(textStyle)
    def setDisabled(self,disabled:bool):
        self.onDisableChange.emit(disabled)
        super().setDisabled(disabled)    
    def keyPressEvent(self, event:QKeyEvent):
        super(Input,self).keyPressEvent(event)
        self.onKeyPressed.emit(event)
        
class Label(QLabel):
    class Style:
        base = {
            "font-size": "14px",
            "color": TAILWIND_COLORS.ZINC_700,
            "font-weight": "550",
        }
        disabled = {
            "color": TAILWIND_COLORS.ZINC_400,
        }
    def __init__(self,parent:QWidget=None,text:str="",forInput:Input=None):
        super().__init__(parent=parent)
        self._text = text
        self.setObjectName("label_"+uuid.uuid4().hex)
        self.setText(text)
        self.setStyleSheet(QssParse.toQss("QLabel",self.Style.base)+QssParse.toQss("QLabel:disabled",self.Style.disabled))
        
        if forInput:
            self.disabled = not forInput.isEnabled()
            self.mousePressEvent = lambda e: forInput.setFocus()
            forInput.onDisableChange.connect(self.setDisabled)
            self.setDisabled(self.disabled)
        
    @property
    def text(self):
        return self._text
    @text.setter
    def text(self,value):
        self._text = value
        self.setText(value)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    app.setFont(QFont("Inter", 14))
    window = QWidget()
    window.setStyleSheet("background-color: #fff;")
    window.resize(800, 600)
    layout = QVBoxLayout(window)
    layout.setContentsMargins(24,24,24,24)
    layout.setSpacing(12)
    input1 = Input(window)
    input2 = Input(window)
    label = Label(window,"Email",forInput=input2)
    layout.addWidget(input1)
    layout.addWidget(label)
    layout.addWidget(input2)
    layout.setAlignment(Qt.AlignTop)
    
    window.show()
    sys.exit(app.exec())
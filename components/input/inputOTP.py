from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from PySideComponent.components.input.Input import Input
from typing import Callable


class InputOTP(QWidget):
    class Values:
        def __init__(self,values:list[str]):
            self.values = values
        def toString(self):
            return "".join(self.values)
        def __call__(self):
            return self.values
        
    def __init__(self,parent:QWidget=None,maxLength:int=6,onComplete:Callable=None):
        super().__init__(parent=parent)
        self._maxLength = maxLength
        self._onComplete = onComplete
        self._currentInput = None
        self.layout = QHBoxLayout(self)
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)
        self.inputs:list[Input] = []
        self.createInput()
        
    
    def createInput(self):
        for i in range(self._maxLength):
            inp = Input(self)
            inp.setAlignment(Qt.AlignCenter)
            inp.setFixedSize(40,40)
            inp.textChanged.connect(self.onTextChanged)
            if i != 0:
                inp.setDisabled(True)
            self.inputs.append(inp)
            self.layout.addWidget(inp)

    def onTextChanged(self,value:str):
        inp = self.sender()
        index = self.inputs.index(inp)
        value = value.strip().replace(" ","")
        if value :
            inp.setText(value[-1])
            if index == self._maxLength - 1:
                self.onComplete()
            else:
                self.inputs[index+1].setDisabled(False)
                self.inputs[index+1].setFocus()
                inp.setReadOnly(True)
        else:
            self.inputs[index].setText("")
            if index == 0:
                self.inputs[index].setDisabled(False)
                self.inputs[index].setFocus()
                self.inputs[index].setReadOnly(False)
                return
            self.inputs[index-1].setFocus()
            self.inputs[index-1].setDisabled(False)
            self.inputs[index-1].setReadOnly(False)
            return
    def onComplete(self)->Values:
        values = [inp.text()for inp in self.inputs]
        if self._onComplete:
            self._onComplete(values)
        return self.Values(values)

if __name__ == "__main__":
    app = QApplication([])
    window = QWidget()
    window.setStyleSheet("background-color: #fff;")
    layout = QHBoxLayout()
    window.setLayout(layout)
    layout.setContentsMargins(60,60,60,60)
    layout.setSpacing(12)
    inputOTP = InputOTP(window)
    layout.addWidget(inputOTP,0,alignment=Qt.AlignCenter)
    window.show()
    app.exec()
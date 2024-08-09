from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from PySideComponent.components import Button,WhiteBoard,Input,Avatar
from typing import Callable



class Popover(QWidget):
    def __init__(self,title:str="",content:str="",onClose:Callable=None,target:QWidget=None,event:str="toggle"):
        super().__init__(parent=None)
        self._title = title
        self._content = content
        self._onClose = onClose
        self.setObjectName("popover")
        self.setFixedWidth(300)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.Popup | Qt.WindowStaysOnTopHint)

        self.setFocusPolicy(Qt.ClickFocus)
        
        self.mainLayout = QVBoxLayout(self)
        self.mainLayout.setContentsMargins(0,0,0,0)
        self.mainLayout.setSpacing(0)
        self.setLayout(self.mainLayout)
        
        self.container = QWidget(self)
        self.mainLayout.addWidget(self.container)
        self.containerLayout = QVBoxLayout(self.container)
        self.containerLayout.setContentsMargins(10,10,10,10)
        self.containerLayout.setSpacing(0)
        self.container.setLayout(self.containerLayout)
        
        self.whiteBoard = WhiteBoard(self,shadow=None,padding=QMargins(4,4,4,4))
        self.containerLayout.addWidget(self.whiteBoard)
        
        self.FadeEffect = QGraphicsOpacityEffect()
        self.FadeEffect.setOpacity(100)
        self.container.setGraphicsEffect(self.FadeEffect)
        self.fadeIn = QPropertyAnimation(self.FadeEffect,b"opacity")
        self.fadeIn.setDuration(100)
        self.fadeIn.setStartValue(0)
        self.fadeIn.setEndValue(1)
        self.fadeIn.finished.connect(self.setFocus())
        
        self.fadeOut = QPropertyAnimation(self.FadeEffect,b"opacity")
        self.fadeOut.setDuration(100)
        self.fadeOut.setStartValue(1)
        self.fadeOut.setEndValue(0)
        self.fadeOut.finished.connect(self.hide)
        
        self.setVisible(False)
        self._target = target
        if self._target:
            self.setTarget(target,event)
    
    
    def showEvent(self,event):
        super().showEvent(event)
        self.fadeIn.start()
        
    def updatePostion(self):
        targetWidth,targetHeight = self._target.size().toTuple()
        targetX,targetY = self._target.pos().toTuple()
        windowWidth,windowHeight = self.window().size().toTuple()
        windowCenterY = (windowHeight/2) - (targetHeight/2)
        
        w,h = self.size().toTuple()
        x = targetX - (w/2)+(targetWidth/2)
        y = targetY + targetHeight 
        maxH = windowHeight-y
        if targetY > windowCenterY : 
            y = targetY - h
            maxH = targetY
            
        self.setMaximumHeight(maxH)
        self.move(x,y)
        self.update()
        
    def target(self):
        return self._target
    def setTarget(self,widget:QWidget,event:str="toggle"):
        self._target = widget
        self.setParent(widget.window())
        self._target.resizeEvent = lambda e: self.updatePostion()
        self._target.moveEvent = lambda e: self.updatePostion()
        self.window().resizeEvent = lambda e: self.updatePostion()
        if event == "toggle":
            self._target.mousePressEvent = lambda e: self.toggle()
        elif event == "click":
            widget.mousePressEvent = lambda e: self.show()
        elif event == "hover":
            widget.enterEvent = lambda e: self.show()
            widget.leaveEvent = lambda e: self.hide()
        # self.window().mousePressEvent = self.mousePressEventWindow
    def toggle(self):
        if self.isVisible():
            self.fadeOut.start()
        else:
            self.show()
    def addWidget(self,widget:QWidget):
        self.whiteBoard.addWidget(widget)

        
class TestPopover(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Popover")
        self.resize(800,800)
        self.windget = QWidget(self)
        self.setCentralWidget(self.windget)
        self.windget.setStyleSheet("background-color: #fff;")

        self.avatar = Avatar(self,size=64,src="https://sbshouse.vn/wp-content/uploads/2020/06/ban-an-kieu-nhat-6-e1591086237736.jpg")
        self.avatar.move(200,300)
        
        button = Button(self,text="Button")
        button.move(200,200)
        
        self.popover = Popover(title="Popover Title",content="Popover Content")
        self.popover.setTarget(self.avatar)

        self.popover.whiteBoard.setGap(4)
        for i in range(50):
            button = QLabel(self.popover,text=f"Button {i+1}")
            self.popover.addWidget(button)
            
    def mousePressEvent(self,event:QMouseEvent):
        if not self.popover.underMouse():
            self.popover.fadeOut.start()
        super().mousePressEvent(event)
if __name__ == "__main__":
    
    import sys
    app = QApplication([])
    window = TestPopover()
    window.show()
    app.exec()
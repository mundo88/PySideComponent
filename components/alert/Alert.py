from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import uuid
from PySideComponent.tabler_icon import TablerIcons,OutlineIcon,FilledIcon
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from PySideComponent.components.button import Button
from PySideComponent.components.typography import H4,P
from enum import Enum
from typing import Union


class Alert(QWidget):
    class Icon(Enum):
        default = OutlineIcon.BELL
        info = OutlineIcon.INFO_CIRCLE
        warning = OutlineIcon.ALERT_TRIANGLE
        success = OutlineIcon.CHECKS
        danger = OutlineIcon.BUG
    def __init__(
            self,parent:QWidget=None, 
            title:str=None, 
            message:str=None,
            icon:QPixmap|str="default",
            iconSize:int=20,
            closeBtn:bool=True,
            margin:int=10,
            postion:str='top-center',
            duration:int=500,
        ):
        super(Alert, self).__init__(parent=parent)
        self._title = title
        self._message = message
        self._icon = icon
        self._closeBtn = closeBtn
        self._margin = margin
        self._postion = postion
        self._duration = duration
        self._iconSize = iconSize
        
        self.initUi()
        self.hide()
    def initUi(self):
        self.setObjectName('alert')
        self.setFixedSize(self.window().size())
        self.setStyleSheet(
            "QWidget#alert{"
                "background-color:white;"
            "}"
        )
        self.container = QWidget(self)
        self.container.setFixedWidth(400)
        objectName = 'alert_'+uuid.uuid1().hex
        self.container.setObjectName(objectName)
        
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(10)
        self.shadow.setColor(QColor(0,0,0,50))
        self.shadow.setOffset(0,1)
        self.container.setGraphicsEffect(self.shadow)
        
        self.container.setStyleSheet(
            f'QWidget#{objectName}''{'
                'border:1px solid #d1d5db;'
                'border-radius:8px;'
                f'background-color:{TAILWIND_COLORS.WHITE};'
            '}'
        )
        if self._closeBtn:
            self.closeIcon = QIcon(TablerIcons.svgToQPixmap(icon=OutlineIcon.X, color=TAILWIND_COLORS.ZINC_500))
            self.closeButton = Button(self.container,variant='ghost',icon=self.closeIcon,size='icon')
            self.closeButton.setFixedSize(24,24)
            self.closeButton.setIconSize(QSize(16,16))
            self.closeButton.clicked.connect(self.close)
            self.closeButton.setCursor(Qt.PointingHandCursor)
            self.closeButton.move(self.container.width()-self.closeButton.width()-4,4)
            
        self.containerLayout = QHBoxLayout()
        self.containerLayout.setContentsMargins(16,16,16,16)
        self.containerLayout.setSpacing(12)
        self.container.setLayout(self.containerLayout)
        
        if type(self._icon) == QIcon:
            self.alertIcon = self._icon
        else:
            self.iconPath = self.Icon[self._icon].value
            self.alertIcon = TablerIcons.svgToQPixmap(icon=self.iconPath, color=TAILWIND_COLORS.ZINC_900)
            
        self.iconLabel = QLabel()
        self.iconLabel.setPixmap(self.alertIcon)
        self.iconLabel.setFixedSize(self._iconSize,self._iconSize)
        self.iconLabel.setScaledContents(True)
        self.containerLayout.addWidget(self.iconLabel,0,Qt.AlignmentFlag.AlignTop)
        
        self.contentLayout = QVBoxLayout()
        self.contentLayout.setContentsMargins(0,0,0,0)
        self.contentLayout.setSpacing(2)
        self.containerLayout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.containerLayout.addLayout(self.contentLayout)
        
        self.titleLabel = H4(self._title,wordWrap=True)
        self.titleLabel.setStyleSheet(
            "QLabel{"
                f"color: {TAILWIND_COLORS.ZINC_900};"
                'font-size:16px;'
                'font-weight:550;'
            "}"
        )
        self.contentLayout.addWidget(self.titleLabel)
        
        self.messageLabel = P(self._message,wordWrap=True,color=TAILWIND_COLORS.ZINC_500)
        self.messageLabel.setFont(QFont('Inter',10))
        self.messageLabel.setStyleSheet(
            "QLabel{"
                f"color: {TAILWIND_COLORS.ZINC_700};"
            "}"
        )
        self.contentLayout.addWidget(self.messageLabel)

        self.container.resizeEvent = lambda e : self.updatePos(self._postion) 
        
        self.slideAnimation = QPropertyAnimation(self,b"pos")
        self.slideAnimation.setDuration(self._duration)  
        self.slideAnimation.setEasingCurve(QEasingCurve.InBounce)
        
        self.autoClose = QTimer()
        self.autoClose.setSingleShot(True)
        self.autoClose.setInterval(3000)
        self.autoClose.timeout.connect(self.hide)

        self.container.resizeEvent = lambda e : self.updatePos()
        
    @property
    def position(self):
        return self._postion
    @position.setter
    def position(self,value):
        self._postion = value
        self.updatePos()
    def getPos(self):
        topStart = self._margin
        topEnd = topStart
        
        leftStart = -self.width()
        leftEnd = self._margin
        
        rightStart = self.container.width() + self.width()
        rightEnd =self.width() - self.container.width() - self._margin
        
        bottomStart = self.height() - self.container.height() - self._margin
        bottomEnd = bottomStart
        
        center = (self.width()/2) - (self.container.width()/2)
        
        topCenterStart = - self.height()
        topCenterEnd = self._margin
        
        bottomCenterStart = self.height() + self.container.height()
        bottomCenterEnd = self.height() - self.container.height() - self._margin
        
        startValues = {
            'top-left':QPoint(leftStart,topStart),
            'top-right':QPoint(rightStart,topStart),
            'bottom-left':QPoint(leftStart,bottomStart),
            'bottom-right':QPoint(rightStart,bottomStart),
            'top-center':QPoint(center,topCenterStart),
            'bottom-center':QPoint(center,bottomCenterStart),
        }
        endValues = {
            'top-left':QPoint(leftEnd,topEnd),
            'top-right':QPoint(rightEnd,topStart),
            'bottom-left':QPoint(leftEnd,bottomStart),
            'bottom-right':QPoint(rightEnd,bottomStart),
            'top-center':QPoint(center,topCenterEnd),
            'bottom-center':QPoint(center,bottomCenterEnd),
        }
        startValue = startValues[self._postion]
        endValue = endValues[self._postion]
        return startValue, endValue
    def updatePos(self):
        startValue, endValue = self.getPos()
        self.slideAnimation.setStartValue(startValue)
        self.slideAnimation.setEndValue(endValue)
    def showEvent(self, event):
        self.raise_()
        self.slideAnimation.start()
        super().showEvent(event)
    def __call__(self,title:str='Alert',message:str="Customer Alert Window Application",icon:QPixmap|str=None):
        if type(icon) == QPixmap:
            alertIcon = icon
        else:
            iconPath = self.Icon[icon].value
            alertIcon = TablerIcons.svgToQPixmap(icon=iconPath, color=TAILWIND_COLORS.ZINC_900)
            
        self.titleLabel.setText(title)
        self.messageLabel.setText(message)
        self.iconLabel.setPixmap(alertIcon)
        super().show()
    def info(self,title:str='Alert',message:str="Customer Alert Window Application"):
        icon = self.Icon.info.name
        self.__call__(title,message,icon)
    def success(self,title:str='Alert',message:str="Customer Alert Window Application"):
        icon = self.Icon.success.name
        self.__call__(title,message,icon)
    def warning(self,title:str='Alert',message:str="Customer Alert Window Application"):
        icon = self.Icon.warning.name
        self.__call__(title,message,icon)
    def danger(self,title:str='Alert',message:str="Customer Alert Window Application"):
        icon = self.Icon.danger.name
        self.__call__(title,message,icon)
    
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = QWidget()
    window.setObjectName('window')
    window.setFixedWidth(1400)
    window.setFixedHeight(600)
    
    layout = QHBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.setSpacing(12)
    window.setLayout(layout)
    layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
    
    alert = Alert(window,postion='top-right',iconSize=100)
    alert1 = Alert(window,postion='top-left')
    alert2 = Alert(window,postion='bottom-right')
    alert3 = Alert(window,postion='bottom-left')
    alert4 = Alert(window,postion='top-center')
    alert5 = Alert(window,postion='bottom-center')
    
    customerIcon = TablerIcons.svgToQPixmap(icon=FilledIcon.HEART,color=TAILWIND_COLORS.RED_500)
    title = 'Alert'
    message = 'Lo"Neque porro quisquam est qui dolorem ipsum quia dolor sit amet, consectetur, adipisci velit...'
    
    def pushAlert():
        alert(title=title,message=message,icon=customerIcon)
        
    def pushAlert1():
        alert1.info(title=title,message=message)
    def pushAlert2():
        alert2.success(title=title,message=message)
    def pushAlert3():
        alert3.warning(title=title,message=message)
    def pushAlert4():
        alert4.danger(title=title,message=message)
    def pushAlert5():
        alert5.info(title=title,message=message)
        
    button = Button(window,text='Alert Top Right',onClick=pushAlert)
    button1 = Button(window,text='Alert Top Left',onClick=pushAlert1)
    button2 = Button(window,text='Alert Bottom Right',onClick=pushAlert2)
    button3 = Button(window,text='Alert Bottom Left',onClick=pushAlert3)
    button4 = Button(window,text='Alert Top Center',onClick=pushAlert4)
    button5 = Button(window,text='Alert Bottom Center',onClick=pushAlert5)
    
    
    layout.addWidget(button)
    layout.addWidget(button1)
    layout.addWidget(button2)
    layout.addWidget(button3)
    layout.addWidget(button4)
    layout.addWidget(button5)
    
    window.show()
    sys.exit(app.exec())
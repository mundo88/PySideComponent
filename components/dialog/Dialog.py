from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import uuid
from PySideComponent.components.button import Button
from PySideComponent.tabler_icon import TablerIcons,OutlineIcon,FilledIcon


class Dialog(QWidget):
    def __init__(self,parent:QWidget=None, title:str="", message:str="",_show = False, closeBtn:bool = False,outSideClose = True):
        super(Dialog, self).__init__(parent=parent)
        self._title = title
        self._message = message
        self.closeBtn = closeBtn
        self._outSideClose = outSideClose
        self._show = _show
        self.initUi()
        if _show:
            self.show()
        else:
            self.hide()

    def initUi(self):
        self.objectName = 'alert_'+uuid.uuid1().hex
        self.setObjectName(self.objectName)
        self.setLayout(QVBoxLayout())
        self.layout().setContentsMargins(0,0,0,0)
        self.layout().setSpacing(0)
        self.w,self.h = self.parent().window().width(),self.parent().window().height()
        self.setGeometry(0,0,self.w,self.h)
        self.groupAnimation = QParallelAnimationGroup(self)
        self.effect = QGraphicsOpacityEffect(self, opacity=1.0)
        self.setGraphicsEffect(self.effect)            
        self.fadeInAnimation = QPropertyAnimation(
            self,
            propertyName=b"opacity",
            targetObject=self.effect,
            duration=100,
            startValue=0.0,
            endValue=1.0,
        )
        self.fadeInAnimation.setEasingCurve(QEasingCurve.Linear)
        self.fadeOutAnimation = QPropertyAnimation(
            self,
            propertyName=b"opacity",
            targetObject=self.effect,
            duration=100,
            startValue=1.0,
            endValue=0.0,
        )
        self.fadeOutAnimation.setEasingCurve(QEasingCurve.InOutQuad)
        self.fadeOutAnimation.finished.connect(self.close)
        
        self.initOverlay()
        self.initAlert()
        QShortcut(Qt.Key_Escape,self,self.fadeOut)

    def initOverlay(self):
        self.overlayWidget = QWidget(self)
        self.overlayWidget.setObjectName('overlay')
        
        self.overlayWidget.setStyleSheet(
            'QWidget#overlay{'
                'background-color:rgba(0,0,0,0.80);'
                'border:none;'
            '}'
        )
        self.overlayWidget.setGeometry(0,0,self.w,self.h)
        if self.outSideClose:
            self.overlayWidget.mousePressEvent = lambda event:self.fadeOut()

    def initAlert(self):
        self.alertWidget = QWidget(self)
        self.alertWidget.setStyleSheet('background-color:white;border-radius:8px;')
        self.alertWidget.setMinimumWidth(500)
        self.alertWidget.setObjectName('alert')
        self.alertLayout = QVBoxLayout()
        self.alertLayout.setContentsMargins(24,24,24,24)
        self.alertLayout.setSpacing(12)
        
        self.titleLabel = QLabel()
        self.titleLabel.setText(self.title)
        self.titleLabel.setStyleSheet('font-size:18px;font-weight:600;color:#1f2937;font-family:"Inter";')
        self.alertLayout.addWidget(self.titleLabel)
        self.messageLabel = QLabel()
        self.messageLabel.setText(self.message)
        self.messageLabel.setStyleSheet('font-size:14px;font-weight:400;color:#6b7280;font-family:"Inter";')
        self.messageLabel.setWordWrap(True)
        self.alertLayout.addWidget(self.messageLabel)
        
        self.footerWidget = QWidget(self)
        self.footerWidget.setObjectName('action')
        self.footerLayout = QHBoxLayout()
        self.footerLayout.setContentsMargins(0,12,0,0)
        self.footerWidget.setLayout(self.footerLayout)
        self.footerLayout.setSpacing(9)
        self.alertLayout.addWidget(self.footerWidget)
        self.cancelButton = Button(self.footerWidget,text='Hủy',variant='outline')
        self.cancelButton.clicked.connect(self.fadeOut)
        
        self.acceptButton = Button(self.footerWidget,text='Xác nhận')
        self.acceptButton.clicked.connect(self.accept)
        
        self.footerLayout.addWidget(self.cancelButton,1,Qt.AlignRight)
        self.footerLayout.addWidget(self.acceptButton,0,Qt.AlignRight)
        
        self.alertWidget.setLayout(self.alertLayout)
        self.layout().addWidget(self.alertWidget,0,Qt.AlignCenter)
        
        if self.closeBtn:
            self.alertWidget.resizeEvent = lambda e:self.initCloseButton(e)
    def accept(self):
        self.close()
        return True

    def initCloseButton(self,e):
        icon = QIcon(TablerIcons.svgToQPixmap(OutlineIcon.X))
        self.closeButton = Button(self,variant='ghost',size='icon',icon=icon)
        self.closeButton.setFixedSize(24,24)
        buttonSize = self.closeButton.size()
        size = e.size()
        x = self.w/2 + size.width()/2 - buttonSize.width() - buttonSize.width()/2
        y = self.h/2 - size.height()/2 + buttonSize.height()/2
        self.closeButton.move(x,y)
        self.closeButton.clicked.connect(self.fadeOut)
        self.closeButton.show()
        
    def fadeIn(self):
        self.fadeInAnimation.start()
    def fadeOut(self):
        self.fadeOutAnimation.start()
        
    def showEvent(self, event):
        self.raise_()
        self.activateWindow()
        self.fadeIn()
        return super().showEvent(event)
    
    
    def getOutSideClose(self):
        return self._outSideClose
    def setOutSideClose(self, value):
        self._outSideClose = value
        if self._outSideClose:
            self.overlayWidget.mousePressEvent = lambda event:self.fadeOut()
        else:
            self.overlayWidget.mousePressEvent = lambda event: False
    outSideClose = Property(bool,getOutSideClose,setOutSideClose)
    def getTitle(self):
        return self._title
    def setTitle(self, value):
        self._title = value
        self.titleLabel.setText(self.title)
    title = Property(str,getTitle,setTitle)
    
    def getMessage(self):
        return self._message
    def setMessage(self, value):
        self._message = value
        self.messageLabel.setText(self.message)
    message = Property(str,getMessage,setMessage)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedWidth(800)
    window.setFixedHeight(500)
    widget = QWidget(window)
    widget.setStyleSheet('background-color:white;')
    widget.setObjectName('widget')
    alert = Dialog(widget,title='Are you absolutely sure?',message='This action cannot be undone. This will permanently delete your account and remove your data from our servers.')
    pushButton = Button(widget,text='Show Dialog',variant='primary')
    pushButton.clicked.connect(lambda:alert.show())
    layout = QVBoxLayout()
    layout.setContentsMargins(0,0,0,0)
    layout.setSpacing(0)
    layout.setAlignment(Qt.AlignCenter)
    layout.addWidget(pushButton)
    widget.setLayout(layout)
    window.setCentralWidget(widget)
    window.show()
    sys.exit(app.exec())
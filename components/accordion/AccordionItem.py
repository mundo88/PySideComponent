from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import uuid
from . import Accordion
class AccordionItem(QFrame):
    signal = Signal(bool)
    def __init__(self, parent:Accordion=None,title='Test accordion',content="Lorem Ipsum is simply dummy text of the printing and typesetting industry",show=False):
        super(AccordionItem,self).__init__(parent=parent)
        self.title = title
        self.content = content
        self._show = show
        self.signal.connect(self.toggle)
        self.initUi()

    def initUi(self):
        self.objectName = 'accordionItem_'+str(uuid.uuid4())
        self.setObjectName(self.objectName)
        self.setCursor(Qt.PointingHandCursor)
        
        self.containerLayout = QVBoxLayout()
        self.containerLayout.setContentsMargins(0,14,0,14)
        
        self.topLayout = QHBoxLayout()
        self.topLayout.setContentsMargins(0,0,0,0)
        self.containerLayout.addLayout(self.topLayout)
        
        self.createContent()
        self.createTitle()
        self.createArrowButton()
        
        self.setLayout(self.containerLayout)
        self.setStyleSheet(
            f'QFrame#{self.objectName}''{'
                'border:none;'
                'border-bottom:1px solid #d1d5db;'
            '}'
        )

        
    def createContent(self):
        self.contentLabel = QLabel()
        self.contentLabel.setText(self.content)
        self.contentLabel.setStyleSheet('color:#374151')
        self.containerLayout.addWidget(self.contentLabel)
        self.contentLabel.setVisible(self._show)
        self.contentLabel.setWordWrap(True)
    def createTitle(self):
        self.titleLabelStyle = 'font-size: 14px; font-weight: 550; color: #1f2937;font-family: "Inter";'
        self.titleLabel = QLabel()
        self.titleLabel.setText(self.title)
        self.titleLabel.setStyleSheet(self.titleLabelStyle)
        self.topLayout.addWidget(self.titleLabel)
        self.topLayout.setAlignment(self.titleLabel, Qt.AlignLeft)
        
    def createArrowButton(self):
        self.arrowButton = QLabel()
        self.arrowPixmap = QPixmap("./Resource/tabler_icon/svg/outline/chevron-down.svg")
        self.arrowButton.setPixmap(self.arrowPixmap)
        self.arrowButton.setFixedSize(16,16)
        self.arrowPixmap.scaled(16,16,Qt.KeepAspectRatio)
        self.arrowPixmap.transformed(QTransform().rotate(90))
        self.arrowButton.setScaledContents(True)
        self.topLayout.addWidget(self.arrowButton)
        self.topLayout.setAlignment(self.arrowButton, Qt.AlignRight)

    def enterEvent(self, event):
        self.titleLabel.setStyleSheet(self.titleLabelStyle+"text-decoration: underline;")
    def leaveEvent(self, event):
        self.titleLabel.setStyleSheet(self.titleLabelStyle)
        
    def mousePressEvent(self, event):
        for item in self.parent().items:
            if item!= self:
                item.show = False
        self.show = not self.show
        
    @property
    def show(self):
        return self._show
    
    @show.setter
    def show(self,value):
        if type(value) == bool:
            self._show = value
            self.signal.emit(self._show)
        else:
            raise TypeError("show must be a boolean")
    @Slot(bool)
    def toggle(self,value):
        if value:
            self.arrowPixmap = QPixmap("./Resource/tabler_icon/svg/outline/chevron-up.svg")
            self.arrowButton.setPixmap(self.arrowPixmap)
        else:
            self.arrowPixmap = QPixmap("./Resource/tabler_icon/svg/outline/chevron-down.svg")
            self.arrowButton.setPixmap(self.arrowPixmap)
        self.contentLabel.setVisible(self.show)
if __name__ == '__main__':
    app = QApplication()
    window = QWidget()
    window.setFixedWidth(500)
    window.setMinimumHeight(300)
    layout = QVBoxLayout()
    layout.addWidget(AccordionItem())
    layout.addWidget(AccordionItem())
    layout.addWidget(AccordionItem())
    layout.setContentsMargins(60,24,60,24)
    layout.setAlignment(Qt.AlignVCenter)
    window.setLayout(layout)
    window.show()
    app.exec()
from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid
from PySideComponent.tailwind_colors import TAILWIND_COLORS

class Typography(QLabel):
    def __init__(
            self,
            parent:QWidget=None,
            id:str='typography',
            color:str=TAILWIND_COLORS.PRIMARY,
            *args,
            **kwargs
        ):
        super(Typography, self).__init__(parent,*args,**kwargs)
        objectName = "_".join([id,uuid.uuid4().hex])
        self.setObjectName(objectName)
        self.setStyleSheet(QssParse.toQss('QLabel',{'color':color}))
        
class H1(Typography):
    def __init__(self,parent:QWidget=None,*args,**kwargs):
        super(H1, self).__init__(parent,font=QFont("Inter",36, QFont.ExtraBold),id="h1",*args,**kwargs)
        
class H2(Typography):
    def __init__(self,parent:QWidget=None,*args,**kwargs):
        super(H2, self).__init__(parent,font=QFont("Inter",30, QFont.Bold),id="h2",*args,**kwargs)

class H3(Typography):
    def __init__(self,parent:QWidget=None,*args,**kwargs):
        super(H3, self).__init__(parent,font=QFont("Inter",24, QFont.DemiBold),id="h3",*args,**kwargs)

class H4(Typography):
    def __init__(self,parent:QWidget=None,*args,**kwargs):
        super(H4, self).__init__(parent,font=QFont("Inter",20, QFont.DemiBold),id="h4",*args,**kwargs)

class P(Typography):
    def __init__(self,parent:QWidget=None,*args,**kwargs):
        super(P, self).__init__(parent,font=QFont("Inter",14, QFont.Normal),id="p",*args,**kwargs)

class Link(P):
    def __init__(self,parent:QWidget=None,href:str="",textDecoration='underline',hoverColor=TAILWIND_COLORS.SKY_600,*args,**kwargs):
        super(Link, self).__init__(parent,*args,**kwargs)
        self.setOpenExternalLinks(True)
        self._href = href
        self._text = kwargs.get('text','')
        self._textDecoration = textDecoration
        self._color = kwargs.get('color',TAILWIND_COLORS.PRIMARY)
        self._hoverColor = hoverColor
        self._duration = kwargs.get('duration',100)
        self.setCursor(Qt.CursorShape.PointingHandCursor)
        self.setText(f'<a href="{self._href}" style="color:{self._color};text-decoration:{self._textDecoration};">{self._text}</a>')
        self.hoverAni = QVariantAnimation(
            startValue=QColor(self._color),
            endValue=QColor(self._hoverColor),
            valueChanged=self.onHovered,
            duration=150,
        )
        
        
    def onHovered(self,color:QColor):
        self.setText(f'<a href="{self._href}" style="color:{color.name()};text-decoration:{self._textDecoration};">{self._text}</a>')
    def hover(self):
        self.hoverAni.stop()
        self.hoverAni.setStartValue(QColor(self._color))
        self.hoverAni.setEndValue(QColor(self._hoverColor))
        self.hoverAni.start()
    def unhover(self):
        self.hoverAni.stop()
        self.hoverAni.setStartValue(QColor(self._hoverColor))
        self.hoverAni.setEndValue(QColor(self._color))
        self.hoverAni.start()
    def enterEvent(self, event):
        self.hover()
        super().enterEvent(event)
    def leaveEvent(self, event):
        self.unhover()
        super().leaveEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    w = QWidget()
    w.resize(800,800)
    w.setStyleSheet("background-color: #fff;")
    layout = QVBoxLayout(w)
    layout.setContentsMargins(0,0,0,0)
    layout.setSpacing(12)
    layout.setAlignment(Qt.AlignCenter)
    w.setLayout(layout)
    h1 = H1(w,text="This is H1",color=TAILWIND_COLORS.RED_500)
    h2 = H2(w,text="This is H2",color=TAILWIND_COLORS.PURPLE_500)
    h3 = H3(w,text="This is H3",color=TAILWIND_COLORS.BLUE_500)
    h4 = H4(w,text="This is H4",color=TAILWIND_COLORS.GREEN_500)
    p = P(w,text="This is P")
    link = Link(w,href="https://www.google.com",text="This is Link: https://google.com",textDecoration="none",color=TAILWIND_COLORS.AMBER_700,hoverColor=TAILWIND_COLORS.AMBER_500)
    
    layout.addWidget(h1)
    layout.addWidget(h2)
    layout.addWidget(h3)
    layout.addWidget(h4)
    layout.addWidget(p)
    layout.addWidget(link)
    w.show()
    app.exec()
        
        
        
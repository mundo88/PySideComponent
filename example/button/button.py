from PySideComponent.components import Button
from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from PySideComponent.tabler_icon import TablerIcons,OutlineIcon,FilledIcon

class TestButton(QWidget):
    def __init__(self,parent:QWidget=None):
        super(TestButton,self).__init__(parent=None)
        self.setStyleSheet(f"background-color:{TAILWIND_COLORS.GRAY_050}")
        self.setWindowTitle("Test Button")
        layout = QHBoxLayout()
        self.setLayout(layout)
        layout.setContentsMargins(120,120,120,120)
        layout.setSpacing(12)
        
        defaultButton = Button(self,text='Button')
        layout.addWidget(defaultButton)
        
        secondaryButton = Button(self,variant="secondary",text='Secondary')
        layout.addWidget(secondaryButton)
    
        whiteButton = Button(self,variant="white",text='White Button')
        layout.addWidget(whiteButton)
        
        outlineButton = Button(self,variant="outline",text='OutLine')
        layout.addWidget(outlineButton)
        
        ghostButton = Button(self,variant="ghost",text='Ghost')
        layout.addWidget(ghostButton)
        
        destructiveButton = Button(self,variant="destructive",text="Destructive")
        layout.addWidget(destructiveButton)
        
        linkButton = Button(self,variant="link",text='Link')
        layout.addWidget(linkButton)
        
        emailIcon = QIcon(TablerIcons.svgToQPixmap(icon=OutlineIcon.MAIL, color=TAILWIND_COLORS.ZINC_050))
        button_with_icon=Button(self,variant='primary',text='Login With Email',icon=emailIcon)
        layout.addWidget(button_with_icon)
        
        icon = QIcon(TablerIcons.svgToQPixmap(icon=FilledIcon.MAIL, color=TAILWIND_COLORS.ZINC_900))
        buttonOnlyIcon = Button(self,variant='outline',icon=icon,size='icon')
        layout.addWidget(buttonOnlyIcon)
        
        
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = TestButton()
    window.show()
    app.exec()
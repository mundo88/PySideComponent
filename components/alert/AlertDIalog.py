from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
import uuid
from PySideComponent.components.dialog import Dialog
from PySideComponent.components.button import Button




class AlertDialog(Dialog):
    def __init__(self,parent:QWidget=None, title:str="", message:str="",show = False):
        super(AlertDialog, self).__init__(parent=parent,title=title, message=message,_show = show, closeBtn = False,outSideClose = False)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.setFixedWidth(800)
    window.setFixedHeight(500)
    widget = QWidget(window)
    widget.setStyleSheet('background-color:white;')
    widget.setObjectName('widget')
    alert = AlertDialog(window,title='Are you absolutely sure?',message='This action cannot be undone. This will permanently delete your account and remove your data from our servers.')
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
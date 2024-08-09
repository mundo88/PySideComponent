"""
Widget: Button
Version: 0.0.1

Contributors: Minh Phung
Email: minhphung8898@gmail.com

Description: A QPushButton customised 
"""
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# Importing from the MadQt package Widgets folder
from PySideComponent.components import Button

from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon
from PySide6.QtDesigner import (QExtensionManager,
    QDesignerCustomWidgetInterface,
    QDesignerFormWindowInterface)

DOM_XML = """
<ui>
    <widget class='Button' name='button'>
    </widget>
</ui>
"""

class ButtonPlugin(QObject, QDesignerCustomWidgetInterface):
    def __init__(self):
        QObject.__init__(self)
        QDesignerCustomWidgetInterface.__init__(self)
        self.initialized = False

    def createWidget(self, parent):
        return Button(parent=parent,text='Button')

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'components'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'icon.ico')
        return QIcon(imgLocation)

    def includeFile(self):
        # Importing from the MadQt package Widgets folder
        return 'PySideComponent.components.button.Button'

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isContainer(self):
        return False

    def isInitialized(self):
        return self.initialized

    def name(self):
        return 'Button'

    def toolTip(self):
        return 'A QPushButton customised'

    def whatsThis(self):
        return self.toolTip()

  
"""
Widget: Widget
Version: 0.0.1

Contributors: Minh Phung
Email: minhphung8898@gmail.com

Description: Alert
"""
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

# Importing from the MadQt package Widgets folder
from PySideComponent.components import AlertDialog

from PySide6.QtCore import QObject
from PySide6.QtGui import QIcon
from PySide6.QtDesigner import (QExtensionManager,
    QDesignerCustomWidgetInterface,
    QDesignerFormWindowInterface)

DOM_XML = """
<ui language='c++'>
    <widget class='AlertDialog' name='alertDialog'/>
</ui>
"""

class AlertDialogPlugin(QObject, QDesignerCustomWidgetInterface):
    def __init__(self):
        QObject.__init__(self)
        QDesignerCustomWidgetInterface.__init__(self)
        self.initialized = False

    def createWidget(self, parent):
        return AlertDialog(parent=parent,title='Are you absolutely sure?',message='This action cannot be undone. This will permanently delete your account and remove your data from our servers.')
    
    def domXml(self):
        return DOM_XML

    def group(self):
        return 'components'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR,'icon-dialog.ico')
        return QIcon(imgLocation)

    def includeFile(self):
        # Importing from the MadQt package Widgets folder
        return 'PySideComponent.components.alert.AlertDialog'

    def initialize(self, core):
        if self.initialized:
            return
        self.initialized = True

    def isContainer(self):
        return False

    def isInitialized(self):
        return self.initialized

    def name(self):
        return 'AlertDialog'

    def toolTip(self):
        return 'Alert Dialog'

    def whatsThis(self):
        return self.toolTip()

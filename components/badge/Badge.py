from PySideComponent.modules import *
from PySideComponent.utils import QssParse
from enum import Enum
import uuid 
from PySideComponent.tailwind_colors import TAILWIND_COLORS

class BadgeStyle(Enum):
	primary     = {
		'style':{
			"background-color": TAILWIND_COLORS.PRIMARY,
   			"color": TAILWIND_COLORS.ZINC_100,
	  	},
		'hover'  :{
			"background-color": TAILWIND_COLORS.PRIMARY_HOVER,
	   },
	}
	secondary   = {
		'style':{
			"background-color": TAILWIND_COLORS.SECONDARY,
  			"color": TAILWIND_COLORS.PRIMARY
		},
		'hover'  : {
	  		"background-color":TAILWIND_COLORS.SECONDARY_HOVER
		},
	}
	destructive = {
		'style':{
			"background-color": TAILWIND_COLORS.DESTRUCTIVE,
			"color": TAILWIND_COLORS.ZINC_100
	   	},
		'hover'  :{
			"background-color": TAILWIND_COLORS.DESTRUCTIVE_HOVER
	  	}
	}
	outline     = {
		'style':{
			"background-color":TAILWIND_COLORS.WHITE,
			"color": TAILWIND_COLORS.PRIMARY,
			"border":f"1px solid {TAILWIND_COLORS.ZINC_200}"
	   	},
		'hover'  : {
			"background-color":TAILWIND_COLORS.ZINC_100,
	  	},
	}


class Badge(QLabel):
	def __init__(self,parent:QWidget=None,text:str='',variant:str=BadgeStyle.primary.name,size:str='md',rounded:int=6):
		super(Badge, self).__init__(parent)
		objectName = "badge_"+uuid.uuid4().hex
		self.setObjectName(objectName)
		self._text = text
		self._variant = variant
		self._size = size
		self._rounded = rounded
		self.setText(self._text)
		self.setStyleSheet(self.getStyle(variant))
	def getStyle(self,variant):
		defaultStyle = {
			"border-radius"	: f"{self._rounded}px",
			"font-weight"	: "600",
			"font-size" 	: "12px",
			"font-family"	: "Inter",
			"padding"		: "3px 8px",
		}
		style = defaultStyle | BadgeStyle[variant].value['style']
		hoverStyle = BadgeStyle[variant].value['hover']
		styleSheet = QssParse.toQss("QLabel",style)
		hoverStyleSheet = QssParse.toQss("QLabel:hover",hoverStyle)
		return styleSheet + hoverStyleSheet


if __name__ == "__main__":
	app = QApplication([])
	window = QWidget()
	window.setStyleSheet("background-color: #fff;")
	layout = QHBoxLayout()
	window.setLayout(layout)
	layout.setContentsMargins(60,60,60,60)
	layout.setSpacing(12)
	
	default_badge = Badge(text='Badge')
	layout.addWidget(default_badge,0,alignment=Qt.AlignCenter)
	
	secondary_badge = Badge(variant="secondary",text='Secondary')
	layout.addWidget(secondary_badge,0,alignment=Qt.AlignCenter)
 
	outline_badge = Badge(variant="outline",text='OutLine')
	layout.addWidget(outline_badge,0,alignment=Qt.AlignCenter)

	destructive_badge = Badge(variant="destructive",text="Destructive")
	layout.addWidget(destructive_badge,0,alignment=Qt.AlignCenter)
	
	window.show()

	app.exec()

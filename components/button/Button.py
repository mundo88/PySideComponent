from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import uuid
from enum import Enum
from PySideComponent.tailwind_colors import TAILWIND_COLORS
from PySideComponent.tabler_icon import TablerIcons,OutlineIcon,FilledIcon
from PySideComponent.utils import QssParse
from typing import Callable


class ButtonStyle(Enum):
	primary     = {
		'style':{
			"background-color": TAILWIND_COLORS.ZINC_900,
   			"color": TAILWIND_COLORS.ZINC_100,
	  		"padding":"8px 16px"
	  	},
		'hover'  :{
			"background-color": TAILWIND_COLORS.ZINC_800,
		},
		'checked' :{
			"background-color": TAILWIND_COLORS.ZINC_950,
		}
	}
	secondary   = {
		'style':{
			"background-color": TAILWIND_COLORS.ZINC_200,
  			"color": TAILWIND_COLORS.ZINC_900
		},
		'hover'  : {
	  		"background-color":TAILWIND_COLORS.ZINC_100
		},
  		'checked' :{
			"border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
		}
	}
	white   = {
		'style':{
			"background-color": "#ffffff",
	   		"color":TAILWIND_COLORS.ZINC_900
		},
		'hover'  :{
			"background-color":TAILWIND_COLORS.ZINC_100
	  	},
		'checked' :{
			"border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
		}
	}
	destructive = {
		'style':{
			"background-color": TAILWIND_COLORS.RED_500,
			"color": TAILWIND_COLORS.ZINC_100
	   	},
		'hover'  :{
			"background-color": TAILWIND_COLORS.RED_400
	  	},
  		'checked' :{
			"border": f"1px solid {TAILWIND_COLORS.RED_600}",
		}
	}
	outline     = {
		'style':{
			"background-color":TAILWIND_COLORS.WHITE,
			"color": TAILWIND_COLORS.ZINC_900,
			"border":f"1px solid {TAILWIND_COLORS.ZINC_200}"
	   	},
		'hover'  : {
			"background-color":TAILWIND_COLORS.ZINC_100,
	  	},
		'checked' :{
			"border-color": f"1px solid {TAILWIND_COLORS.ZINC_500}",
		}
	}
	ghost       = {
		"style" : {
			"background-color":TAILWIND_COLORS.TRANSPARENT,
			"border": TAILWIND_COLORS.NONE,
			"color": TAILWIND_COLORS.ZINC_900
		},
		'hover'  : {
			"background-color":TAILWIND_COLORS.ZINC_100
	  	},
		'checked' :{
			"border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
		}
	}
	link        = {
		'style': {
			"background-color":TAILWIND_COLORS.TRANSPARENT,
			"border": TAILWIND_COLORS.NONE,
			"color": TAILWIND_COLORS.ZINC_900
		},
		'hover'  : {
			"text-decoration": "underline"
	  	},
  		'checked' :{
			"border": f"1px solid {TAILWIND_COLORS.ZINC_300}",
		}
	}

class Button(QPushButton):
	variantChanged  = Signal(object)
	toggleChanged 	= Signal(bool)
	class ButtonVariant(Enum):
		primary 	= 0
		secondary 	= 1
		white 		= 2
		destructive = 3
		outline 	= 4
		ghost 		= 5
		link 		= 6
	enum_test = QEnum(ButtonVariant)
	def __init__(self, 
			parent:QWidget=None, 
			variant:ButtonStyle=ButtonStyle.primary.name,
			rounded:int=6,
			size='default',
			toggle:bool=False,
			onClick:Callable=None,
			*args,
			**kwargs
		):
	 
		super().__init__(parent=parent,*args,**kwargs)
  
		self.setObjectName('button_'+uuid.uuid4().hex)
		self._variant = variant.lower()
		self.rounded = rounded
		self._toggle = toggle
		self.setStyleSheet(self.getStyle(variant))
		self.setIconSize(QSize(16,16))
		if size =='icon':
			self.setFixedWidth(36)
			self.setFixedHeight(36)
		self.variantChanged.connect(self.onVariantChanged)
		if self._toggle:
			self.setCheckable(True)
			self.clicked.connect(self.onToggleChanged)
   
		if onClick:
			self.clicked.connect(onClick)
		self.show()
	def setIcon(self,icon):
		if self.text() and icon:
			self.setText(" "+self.text())
		super().setIcon(icon)
	def setText(self,text):
		if self.icon() and text:
			text = " "+text
		super().setText(text)
	def getStyle(self,variant):
		defaultStyle = {
			"border-radius"	: f"{self.rounded}px",
			"font-weight"	: "550",
			"font-size" 	: "14px",
			"font-family"	: "Inter",
		}
		if self.icon and not self.text:
			defaultStyle['padding']= '8px'
		else:
			defaultStyle['padding']='8px 16px'
		style = defaultStyle | ButtonStyle[variant].value['style']
		hoverStyle = ButtonStyle[variant].value['hover']
		checkedStyle = ButtonStyle[variant].value['checked']
		styleSheet = QssParse.toQss("QPushButton",style)
		hoverStyleSheet = QssParse.toQss("QPushButton:hover",hoverStyle)
		checkedStyleSheet = QssParse.toQss("QPushButton:checked",checkedStyle)
		return styleSheet + hoverStyleSheet + checkedStyleSheet
	@Property("ButtonVariant", notify=variantChanged,designable=True)
	def variant(self):
		return self._variant
	@variant.setter
	def variant(self, value):
		self._variant = value
		self.variantChanged.emit(value)
	@Slot(object)
	def onVariantChanged(self,value):
		self.setStyleSheet(self.getStyle(value))
		self.update()
	def onToggleChanged(self,checked):
		self.toggleChanged.emit(checked)
  
	
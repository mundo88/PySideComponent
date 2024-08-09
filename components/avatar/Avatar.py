from PySideComponent.modules import *
from PySideComponent.tailwind_colors import TAILWIND_COLORS
import requests
import validators,os


class Avatar(QLabel):
    def __init__(self, parent=None, src=None, size=64,fallback="A"):
        super(Avatar, self).__init__(parent)
        self._src = src
        self._size = size
        self._fallback = fallback
        self.setFixedSize(size, size)
        self.thread = QThreadPool(self)
        self.thread.start(self.getAvatarFromUrl)

    def drawingFallback(self):
        painter = QPainter(self)
        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(TAILWIND_COLORS.ZINC_300, Qt.SolidPattern))
        painter.drawEllipse(0,0,self._size,self._size)
        painter.end()
        if self._fallback:
            text = QPainter(self)
            brush = QBrush()
            text.setFont(QFont('Inter', 14, QFont.Bold))
            text.setPen(TAILWIND_COLORS.ZINC_500)
            text.drawText(QRect(0, 0, self._size, self._size), Qt.AlignCenter, self._fallback)
            text.end()
    def getAvatarFromUrl(self):
        if validators.url(self._src):
            self.drawingAvatar(requests.get(self._src).content)
        elif os.path.isfile(self._src):
            with open(self._src, "rb") as f:
                self.drawingAvatar(f.read())
            print(self._src)
        self.thread.quit()
        self.thread.wait()
        self.update()
    def drawingAvatar(self, imgdata):
        image = QImage.fromData(imgdata) 
        image.convertToFormat(QImage.Format_ARGB32) 
        imgsize = min(image.height(),image.width())
        rect = QRect( 
            (image.width() - imgsize) / 2, 
            (image.height() - imgsize) / 2, 
            imgsize, 
            imgsize, 
        ) 
        image = image.copy(rect) 
        out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32) 
        out_img.fill(Qt.transparent) 
        brush = QBrush(image) 
        painter = QPainter(out_img) 
        painter.setBrush(brush) 
        painter.setPen(Qt.NoPen) 
        painter.drawRoundedRect(0,0,imgsize,imgsize,rect.width()/2,rect.height()/2) 
        painter.end() 
        
        pr = QWindow().devicePixelRatio() 
        pm = QPixmap.fromImage(out_img) 
        pm.setDevicePixelRatio(pr) 
        self._size *= pr 
        pm = pm.scaled(int(self._size), int(self._size), Qt.KeepAspectRatio,  
                                Qt.SmoothTransformation) 
        self.setPixmap(pm)
        
    def paintEvent(self, event:QPaintEvent):
        self.drawingFallback()
        super(Avatar, self).paintEvent(event)
  
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    widget = Avatar(size=500,src="https://scontent.fhan14-3.fna.fbcdn.net/v/t39.30808-6/453489625_2351312458372346_4195638393277769262_n.jpg?stp=cp6_dst-jpg_s1080x2048&_nc_cat=103&ccb=1-7&_nc_sid=bdeb5f&_nc_ohc=8wAkhRC0SYsQ7kNvgGa4WZU&_nc_ht=scontent.fhan14-3.fna&oh=00_AYCIZdYpVFljflONs2ABG_Eg4PlozwzCP90SI9YgJOEW4A&oe=66B30024")
    widget.show()
    sys.exit(app.exec())
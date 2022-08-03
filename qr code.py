#first run these codes to install packages

!pip install pyqrcode
!pip install pypng


#then run this code

import pyqrcode
import png
from pyqrcode import QRCode
s = "www.codingforfree.com"
url = pyqrcode.create(s)
url.svg("myqr.svg", scale = 8)
url.png('myqr.png', scale = 8)
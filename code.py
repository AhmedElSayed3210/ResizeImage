
from PIL import Image
size=(128,128)
# resize image name
saved=('1.png')
try:
    im=Image.open('0.png')
except:
    print('unaple to open image')
    
im.thumbnail(size)
im.save(saved)
im.show()

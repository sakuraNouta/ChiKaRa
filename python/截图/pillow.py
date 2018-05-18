from PIL import ImageGrab 

bbox = (760,0,1160,1080)
im = ImageGrab.grab(bbox)
#im = ImageGrab.grab()

im.show()
#im.save('as.png')

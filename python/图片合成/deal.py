'''
960 * 720 -> 960*2 , 720*2
将rfid文件夹内所有图片4合为1
'''

from PIL import Image
import os

path = 'RFID/'
fs = os.listdir(path)
print(fs)

#arr = ['p1.JPG','p2.JPG','p3.JPG','p4.JPG']

index = 0
while(index < len(fs)):
    if(index < len(fs)-len(fs)%4):
        toImage = Image.new('RGBA',(960*3+5,720*3),'black')
    else:
        toImage = Image.new('RGBA',(960*3+5,720*3),'white')
    for i in range(9):
        if(index < len(fs)):
            fromImage = Image.open(path + fs[index])
            index += 1
            print(index)
            loc = ((int(i/3) * 965), (i % 3) * 720)
            #print(loc)
            toImage.paste(fromImage, loc)

    toImage = toImage.resize((960*3+5,720*3-30))
    toImage.save('merged' + str(int((index+8)/9)) + '.png')

    

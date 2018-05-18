import os

path1 = 'E:/ccs/ccsv5/tools/compiler/c6000_7.4.4/lib'
path2 = 'E:/ccs/ccsv5/tools/compiler/c6000_7.4.4/lib/rtssrc'

fs1 = os.listdir(path1)
fs2 = os.listdir(path2)

for f1 in fs1:
    for f2 in fs2:
        if f1 == f2:
            file = path1 + '/' + f1
            #print(file)
            os.remove(file)

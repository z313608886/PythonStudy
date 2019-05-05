import pickle
#压缩数据
lyst=[60,'king',1997]
fileobj=open('item.dat','wb')
for  zt in lyst:
    pickle.dump(zt,fileobj)
fileobj.close()

#读取数据
lyst=list()
fileobj=open('item.dat','rb')
while True:
    try:
        item=pickle.load(fileobj)
        lyst.append(item)
    except EOFError:
        fileobj.close()
        break
print(lyst)

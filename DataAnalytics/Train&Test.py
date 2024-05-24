import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)

page_speed=np.random.normal(3.0,1.0,1000)
page_amount=np.random.normal(50.0,1.0,1000)
plt.scatter(page_speed,page_amount)

trainX=page_speed[:80]
testX=page_speed[80:]

trainY=page_amount[:80]
testY=page_amount[80:]
plt.scatter(trainX,trainY)

x=np.array(trainX)
y=np.array(trainY)



xp=np.linspace(0,7,100)

p4=np.poly1d(np.polyfit(x,y,4))
axes=plt.axes()
axes.set_xlim([0,7])
axes.set_ylim([0,200])
plt.scatter(x,y)
plt.plot(xp,p4(xp),c='r')
plt.show()

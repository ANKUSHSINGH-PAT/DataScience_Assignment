import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
np.random.seed(2)
pagespeed=np.random.normal(3.0,1.0,1000)
purchaseamount=np.random.normal(50.0,10.0,1000)
plt.scatter(pagespeed,purchaseamount)
x=np.array(pagespeed)
y=np.array(purchaseamount)
p4=np.poly1d(np.polyfit(x,y,4))
xp=np.linspace(0,7,1000)
plt.scatter(x,y)
plt.plot(xp,p4(xp),c='r')
plt.show()
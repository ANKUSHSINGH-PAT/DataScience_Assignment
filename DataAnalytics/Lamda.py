import numpy as np
#
# seq=[1,2,3,4,5]
# k=list(map(lambda  num:num*3,seq))
# print(k)

# print(np.linspace(0,5,100))
arr=np.arange(10,50).reshape(10,4)
k=list(map(lambda  num:num%2,arr))
print(k)
print(arr)



# print(np.ones(10)*5)
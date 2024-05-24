import numpy as np
import pandas as pd
labels=np.array(['a','b','c'])
arr=np.array([1,7,9])
print(pd.Series(arr,labels))

df=pd.DataFrame(np.random.randn(5,4),['A','B','C','D','E'],['W','X','Y','Z'])
print(df)

df['M']=df['W']+df['X']
print(df)
df.drop('M',axis=1,inplace=True)
print(df)

print(df.loc['A'])
print(df.iloc[1])
print(df.loc[['A','B'],['W','X']])


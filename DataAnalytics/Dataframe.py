import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
'''
outside=['G1','G1','G1','G2','G2','G2']
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
df=pd.DataFrame(numpy.random.randn(6,2),hier_index,['A','B'])
print(df)
print((df.loc['G1']))
df.index.names=['Group','Num']
print(df)

'''

iris = load_iris()
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
df['target'] = iris.target
print(df)

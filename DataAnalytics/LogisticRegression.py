import numpy as np
import pandas as pd
import plotly.express as px
import plotly.figure_factory as ff
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report

data=pd.read_csv("DataAnalytics\Input\Advertising.csv")
df=pd.DataFrame(data)
fig = px.histogram(data, x="Age",nbins=30)

X = df[['Daily Time Spent on Site', 'Age', 'Area Income','Daily Internet Usage', 'Male']]

fig = ff.create_scatterplotmatrix(data.select_dtypes(include='number'), height=800, width=800)
fig.show()
y = df['Clicked on Ad']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

logmodel = LogisticRegression()
logmodel.fit(X_train,y_train)
predictions = logmodel.predict(X_test)
print(classification_report(y_test,predictions))

print(predictions)


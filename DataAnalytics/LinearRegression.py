import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import numpy as np
import plotly.express as px



'''
dt=pd.read_csv('Input/USA_Housing.csv')
csv_data=pd.DataFrame(dt)

#sns.pairplot(csv_data)
#print(csv_data.info())

X = csv_data[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
               'Avg. Area Number of Bedrooms', 'Area Population']]
y = csv_data['Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
lm=LinearRegression()
lm.fit(X_train,y_train)
print(lm.intercept_)

coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
#print(coeff_df)

predictions=lm.predict(X_test)
print(predictions)

RME=metrics.root_mean_squared_error(y_test,predictions)
print(RME)
'''


dt=pd.read_csv("DataAnalytics\\Input\\Ecommerce Customers.csv")
csv_data=pd.DataFrame(dt)
print(csv_data.columns)

X = csv_data[['Avg. Session Length', 'Time on App','Time on Website', 'Length of Membership']]
y = csv_data['Yearly Amount Spent']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm=LinearRegression()
lm.fit(X_train,y_train)
print(lm.intercept_)

coeff_df = pd.DataFrame(lm.coef_,X.columns,columns=['Coefficient'])
print(coeff_df)

predictions=lm.predict(X_test)



fig = px.scatter(x=y_test, y=predictions, labels={'x': 'Y Test', 'y': 'Predicted Y'})
fig.show()

# print(predictions)

RME=metrics.root_mean_squared_error(y_test,predictions)
print(RME)

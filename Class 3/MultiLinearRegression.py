import matplotlib.pyplot as plt
import numpy as np
import random
from sklearn import datasets, linear_model, metrics
count =100
limit =1000

X=list()
Y=list()

for i in range(0,count):
	x1=random.randint(0,limit)
	x2=random.randint(0,limit)
	x3=random.randint(0,limit)
	y=x1+3*x2+4*x3
	X.append([x1,x2,x3])
	Y.append([y])
# load the boston dataset
#boston = datasets.load_boston(return_X_y=False)
 
# defining feature matrix(X) and response vector(y)
#X = boston.data
#y = boston.target
print(X)
# splitting X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4,
                                                    random_state=1)
 
# create linear regression object
reg = linear_model.LinearRegression()
 
# train the model using the training sets
reg.fit(X_train, y_train)
 
# regression coefficients
print('Coefficients: \n', reg.coef_)
 
# variance score: 1 means perfect prediction
print('Variance score: {}'.format(reg.score(X_test, y_test)))
 
# plot for residual error
 
## setting plot style
plt.style.use('fivethirtyeight')
 
## plotting residual errors in training data
plt.scatter(reg.predict(X_train), reg.predict(X_train) - y_train,
            color = "green", s = 10, label = 'Train data')
 
## plotting residual errors in test data
plt.scatter(reg.predict(X_test), reg.predict(X_test) - y_test,
            color = "blue", s = 10, label = 'Test data')
 
## plotting line for zero residual error
plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)
 
## plotting legend
plt.legend(loc = 'upper right')
 
## plot title
plt.title("Residual errors")
 
## function to show plot
plt.show()
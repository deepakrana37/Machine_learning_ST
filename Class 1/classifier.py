from sklearn import neighbors
# [height, weight, shoe_size]
X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40],
     [190, 90, 47], [175, 64, 39],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['male', 'male', 'female', 'female', 'male', 'male', 'female', 'female',
     'female', 'male', 'male']

clf = neighbors.KNeighborsClassifier()

# CHALLENGE - ...and train them on our data
clf = clf.fit(X, Y)

prediction = clf.predict([[170, 60, 33]])
#res=map(int,prediction)
#for i in range(len(prediction)):
#	prediction[i]=int(prediction[i])
print(str(prediction).strip('[]'))
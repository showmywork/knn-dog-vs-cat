from sklearn.neighbors import KNeighborsClassifier

X = [[30, 5], [45, 10], [50, 12], [65, 25], [70, 30], [80, 35]]

y = [0, 0, 0, 1, 1, 1]

knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X, y)

prediction = knn.predict([[60, 20]])
if prediction[0] == 0:
    print("It's a Cat")
else:
    print("It's a Dog")
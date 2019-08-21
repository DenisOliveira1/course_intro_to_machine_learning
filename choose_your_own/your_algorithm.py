#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()


### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#pip install matplotlib

from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC
from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier 

def nb():#0.88
    return GaussianNB()

def svm(kernel = "rbf", C):#0.92
    return SVC(kernel, C)

def dt(min_samples_split = 2):#0.90
    return tree.DecisionTreeClassifier(min_samples_split)

def ada():#0.92
    return AdaBoostClassifier()

def rf():#0.91  
    return omForestClassifier()

def knn():#0.92
    return KNeighborsClassifier

file_name = "teste"
clf = svm("linear", 10000)

clf.fit(features_train, labels_train)
pred = clf.predict(features_test)

from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "precisao:", accuracy, "\n"

print "o número de instâncias é:", len(features_train)
print "o número de atributos de cada instância é:", len(features_train[0])



try:
    prettyPicture(clf, features_test, labels_test, file_name)
except NameError:
    pass

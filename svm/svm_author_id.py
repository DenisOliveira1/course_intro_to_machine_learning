#!/usr/bin/python
# -*- coding: cp1252 -*-

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

def svm(kernel = "rbf",C = 1, divisor = 1):
    global features_train, features_test, labels_train, labels_test 

    features_train_this = features_train[:len(features_train)/divisor]
    labels_train_this = labels_train[:len(labels_train)/divisor]

    print "*** kernel:", kernel ,"C:", c,"divisor:",
    
    clf = SVC(kernel, C)

    t0 = time()
    clf.fit(features_train_this, labels_train_this)
    print "tempo de treinamento:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "tempo de predicao:", round(time()-t0, 3), "s"

    accuracy = accuracy_score(pred, labels_test)
    print "precisao:", accuracy, "\n"

    #print pred[10], pred[26], pred[50]

    #chris = 0
    #for i in pred:
    #    if i == 1:
    #        chris = chris + 1
    #print chris

#svm("linear",1,1)#0.98
#svm("linear",1,100)#0.88
#svm("rbf",1,100)#0.61
#svm("rbf",10,100)#0.61
#svm("rbf",100,100)#0.61
#svm("rbf",1000,100)#0.82
#svm("rbf",10000,100)#0.89
#svm("rbf",10000,1)#0.99
    
#########################################################

#parâmetros

#kernel: os kerneis são responsaveis por criarem as novas features que
#possibilitarao que a classificacao seja feita linearmente. A solucao linear
#ao ser representada nas features originais não serao lineares. Dependendo
#do kernal pode haver overfitting.

#C: faz com que a linha de decisao tente classificar o maior número de
#instâncias corretamente. Quanto maior C mais instâncias sao classificadas
#corretamente e isso gera curvas. Um C pequeno tende a ter algumas classificacoes
#erradas, porém mantem a uniformidade da linha e um menor overfitting.

#gamma: define quais instâncias tem influencia sobre a linha de decisao.
#Um gamma grande define que somente instâncias próximas á linha a influenciam,
#gerando curvas, enquanto um gamma pequeno é influenciado pelas instâncias
#distantes, que mantem a uniformidade da linha e um menor overfitting.


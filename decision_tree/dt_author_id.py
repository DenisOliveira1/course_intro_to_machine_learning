#!/usr/bin/python
# -*- coding: cp1252 -*-

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
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
from sklearn import tree
from sklearn.metrics import accuracy_score

def dt(min_samples_split = 2, divisor = 1):
    global features_train, features_test, labels_train, labels_test 

    features_train_this = features_train[:len(features_train)/divisor]
    labels_train_this = labels_train[:len(labels_train)/divisor]

    print "***min_samples_split:", min_samples_split, "divisor:", divisor, "***"

    clf = tree.DecisionTreeClassifier(min_samples_split)

    t0 = time()
    clf.fit(features_train_this, labels_train_this)
    print "tempo de treinamento:", round(time()-t0, 3), "s"

    t0 = time()
    pred = clf.predict(features_test)
    print "tempo de predicao:", round(time()-t0, 3), "s"

    accuracy = accuracy_score(pred, labels_test)
    print "precisao:", accuracy, "\n"

#dt(40)#0.97
print "o n�mero de inst�ncias �:", len(features_train)
print "o n�mero de atributos de cada inst�ncia �:", len(features_train[0])

#########################################################

#par�metros

#min_samples_split: � o n�mero de amostras necessarias para que uma nova
#ramificacao seja feita a partir de um n�. O padrao � 2, ou seja, a �rvore pode� continuar a
#se dividir enquanto o n� possuir ao menos 2 amostras. Quanto menor esse n�mero
#maior � a tendencia de gerar overfitting pois uma nova ramifica��o ser� feita
#para classificar corretamente um unico ponto que pode estar muito distante.

#########################################################

#observacoes

#entropy: v�ria de 0 a 1. Entropia � o aposto de pureza. Se no n� em questao
#todas as amostras sao da mesma classe este n� � puro, ouseja, 0.
#Se no n� houver uma amostra de cada classe do problama a enropia � 1, ou seja,
#totalmente impuro. V�rios ganhos de entropia s�o calculados, cada um baseado
#em um atributo. A divisao tiver maior ganho (menor entropia em ambos os filhos)
#� realizada.

#percentile: paramentro no email_preprocess.py que define a porcentagem de par�metros
#que sera usada.

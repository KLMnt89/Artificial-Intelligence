import os
import math

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
from datasetCrio import dataset
from sklearn.naive_bayes import GaussianNB

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    dataset = [[int(num) if num.isdigit() else float(num) for num in row] for row in dataset]

    # subset_size = len(dataset) // 4
    # subset1 = dataset[:subset_size]
    # subset2 = dataset[subset_size:2 * subset_size]

    # train_sets = [subset1, subset2, subset3] #test_set = subset4 #classifiers=[]

    train_set = dataset[:int(0.85 * len(dataset))] #delete
    test_set = dataset[int(0.85 * len(dataset)):]

    train_x = [row[:-1] for row in train_set]  # for i in range (3)
    train_y = [row[-1] for row in train_set]

    test_x = [row[:-1] for row in test_set]  # delete
    test_y = [row[-1] for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)  # classifiers.append(classifier)

    ct = 0
    # total = 0
    for i in range(0, len(test_set)):
        predicted = classifier.predict([test_x[i]])[0]  # test_set[i][:-1]
        true_class = test_y[i]
        # predictions = [classifier.predict([test_x])[0] for classifier in classifiers]
        if predicted == true_class:  # predictions.count(true_class) >= 2
            ct += 1
        # total++ # print(ct/total)

    entry = [int(num) if num.isdigit() else float(num) for num in input().split(' ')]
    # entry_predictions = [classifier.predict([entry])[0] for classifier in classifiers]

    print(ct / len(test_set)) # if len(set(entry
    print(classifier.predict([entry])[0]) #(entry_predictions[0])
    print(classifier.predict_proba([entry])) #(classifiers[0].predict_proba([entry]))

    #submit_train_data(train_x,train_y)  # submit_train_data([row[:-1] for row in train_sets[0]], [row[-1] for row in train_sets[0]])
    #submit_test_data(test_x, test_y)  # ([row[:-1] for row in test_set], [row[-1] for row in test_set])
    #submit_classifier(classifier)

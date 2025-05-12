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

    subset_size = len(dataset) // 4
    subset1 = dataset[:subset_size]
    subset2 = dataset[subset_size:2 * subset_size]
    subset3 = dataset[2 * subset_size:3 * subset_size]
    subset4 = dataset[3 * subset_size:]

    train_sets = [subset1, subset2, subset3]
    test_set = subset4

    classifiers=[]

    for i in range(3):
        train_x = [row[:-1] for row in train_sets[i]]
        train_y = [row[-1] for row in train_sets[i]]

        classifier = GaussianNB()
        classifier.fit(train_x, train_y)
        classifiers.append(classifier)

    ct = 0
    total_count = 0
    for i in range(0, len(test_set)):
        predicted = test_set[i][:-1]
        true_class = test_set[i][-1]

        predictions = [classifier.predict([predicted])[0] for classifier in classifiers]

        if predictions.count(true_class) >= 2:
            ct += 1
        total_count+=1

    print(ct/total_count)

    entry = [int(num) if num.isdigit() else float(num) for num in input().split(' ')]

    entry_predictions = [classifier.predict([entry])[0] for classifier in classifiers]

    if len(set(entry_predictions)) == 1:
        print(entry_predictions[0])
        print(classifiers[0].predict_proba([entry]))
    else:
        print('klasata ne moze da bide odredena')

    # submit_train_data([row[:-1] for row in train_sets[0]], [row[-1] for row in train_sets[0]])
    # submit_train_data([row[:-1] for row in train_sets[1]], [row[-1] for row in train_sets[1]])
    # submit_train_data([row[:-1] for row in train_sets[2]], [row[-1] for row in train_sets[2]])
    # submit_test_data([row[:-1] for row in test_set], [row[-1] for row in test_set])
    # submit_classifier(classifier)

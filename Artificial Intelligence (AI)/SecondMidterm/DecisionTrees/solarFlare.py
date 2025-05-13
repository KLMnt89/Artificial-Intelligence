import os
from zad1_dataset import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # print(dataset)
    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    a = int(input())
    criterion = input()
    separator = 1 - float(a/100)

    train_set = dataset[int(separator*len(dataset)):]
    train_x = [row[:-1] for row in train_set ]
    train_y = [row[-1] for row in train_set ]
    train_x = encoder.transform(train_x)

    test_set = dataset[:int(separator*len(dataset))]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier = DecisionTreeClassifier(criterion=criterion,random_state=0)
    classifier.fit(train_x, train_y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')
    print(f'Accuracy: {classifier.score(test_x, test_y)}')

    feature_importances = list(classifier.feature_importances_)
    for i in range(len(feature_importances)):
        feature_importances[i]=float(feature_importances[i])

    mostImportant = feature_importances.index(max(feature_importances))
    print(f'Most important feature: {mostImportant}')

    leastImportant = feature_importances.index(min(feature_importances))
    print(f'Least important feature: {leastImportant}')



    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(classifier)

    # submit na encoderot
    # submit_encoder(encoder)

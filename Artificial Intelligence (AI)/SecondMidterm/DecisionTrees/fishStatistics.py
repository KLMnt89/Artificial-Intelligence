import os
from zad2_dataset import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
# from submission_script import *
# from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    encoder = OrdinalEncoder()
    encoder.fit(dataset)

    col_index = int(input())
    num_trees = int(input())
    criterion = input()

    train_set = [row[:col_index] + row[col_index + 1:] for row in dataset[:int(0.85 * len(dataset))]]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]

    test_set = [row[:col_index] + row[col_index + 1:] for row in dataset[int(0.85 * len(dataset)):]]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier = RandomForestClassifier(n_estimators=num_trees, criterion=criterion, random_state=0)
    classifier.fit(train_x, train_y)

    accuracy = classifier.score(test_x, test_y)

    entry = [int(num) for num in input().split(" ")]
    del entry[col_index]

    print("Accuracy: "+str(accuracy))
    print(classifier.predict([entry])[0])
    print(classifier.predict_proba([entry])[0])

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(classifier)

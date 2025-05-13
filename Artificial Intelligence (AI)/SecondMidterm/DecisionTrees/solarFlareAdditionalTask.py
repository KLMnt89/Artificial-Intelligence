import os
from zad1_dataset import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
from sklearn.metrics import classification_report, confusion_matrix


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

def clean_dataset(dataset):
    dataset_cleaned = []
    for row in dataset:
        if str(row[-1]) in ['0', '1']:
            dataset_cleaned.append(row)

    return dataset_cleaned



if __name__ == '__main__':
    # print(dataset)
    dataset = clean_dataset(dataset)

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

    col_index = int(input())
    dataset2 = [row[:col_index] + row[col_index + 1 :] for row in dataset]
    encoder2 = OrdinalEncoder()
    encoder2.fit([row[:-1] for row in dataset2])

    train_set2 = dataset2[int(separator * len(dataset2)):]
    train_x2 = [row[:-1] for row in train_set2]
    train_y2 = [row[-1] for row in train_set2]
    train_x2 = encoder2.transform(train_x2)

    test_set2 = dataset2[:int(separator * len(dataset2))]
    test_x2 = [row[:-1] for row in test_set2]
    test_y2 = [row[-1] for row in test_set2]
    test_x2= encoder2.transform(test_x2)

    classifier2 = DecisionTreeClassifier(criterion='gini', random_state=0)
    classifier2.fit(train_x2, train_y2)

    print(f'Depth (second): {classifier2.get_depth()}')
    print(f'Number of leaves (second): {classifier2.get_n_leaves()}')
    print(f'Accuracy (second): {classifier2.score(test_x2, test_y2)}')

    feature_importances2 = list(classifier2.feature_importances_)
    for i in range(len(feature_importances2)):
        feature_importances2[i] = float(feature_importances2[i])

    mostImportant2 = feature_importances2.index(max(feature_importances2))
    print(f'Most important feature (second): {mostImportant2}')

    leastImportant2 = feature_importances2.index(min(feature_importances2))
    print(f'Least important feature (second): {leastImportant2}')

    # Evaluate first classifier
    predictions1 = classifier.predict(test_x)
    print("\n--- Evaluation for First Classifier ---")
    print("Confusion Matrix:")
    print(confusion_matrix(test_y, predictions1) ) # <-- класа 0: 18 точно, 2 false positives
    print("Classification Report:")
    print(classification_report(test_y, predictions1))

    # Evaluate second classifier
    predictions2 = classifier2.predict(test_x2)
    print("\n--- Evaluation for Second Classifier ---")
    print("Confusion Matrix:")
    print(confusion_matrix(test_y2, predictions2))
    print("Classification Report:")
    print(classification_report(test_y2, predictions2))


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

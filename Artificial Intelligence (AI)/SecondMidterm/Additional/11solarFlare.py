from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier

from dataset11 import dataset

def del_col(dataset, col_index):
    dataset2 =[]
    for row in dataset:
        new_row = row[:col_index] + row[col_index+1:]
        dataset2.append(new_row)
    return dataset2

def calculate_accuracy(predictions, test_Y):
    acc = 0
    for pred, actual in zip(predictions, test_Y):
        if pred == actual:
            acc += 1

    tp, fp = 0, 0
    for pred, actual in zip(predictions, test_Y):
        if actual == 1:
            if pred == actual:
                tp += 1
        else:
            if pred != actual:
                fp += 1

    precision = tp / (tp + fp) if (tp + fp) != 0 else 0
    return acc / len(test_Y), precision

if __name__ == '__main__':
    x = int(input())  # broj na primeroci test-train
    clasificator = input()
    col_index = int(input())

    # Original dataset
    train_set = dataset[x:]
    test_set = dataset[:x]

    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    # Without one column
    train_set2 = del_col(train_set, col_index)
    test_set2 = del_col(test_set, col_index)

    train_x2 = [row[:-1] for row in train_set2]
    train_y2 = [row[-1] for row in train_set2]

    test_x2 = [row[:-1] for row in test_set2]
    test_y2 = [row[-1] for row in test_set2]

    classifier1 = None
    classifier2 = None
    # Classifier selection
    if clasificator == 'DT':
        classifier1 = DecisionTreeClassifier(random_state=0)
        classifier2 = DecisionTreeClassifier(random_state=0)
    elif clasificator == 'NB':
        classifier1 = GaussianNB()
        classifier2 = GaussianNB()
    elif clasificator == 'NN':
        classifier1 = MLPClassifier(hidden_layer_sizes=(3,), activation="relu", learning_rate_init=0.003, max_iter=200, random_state=0)
        classifier2 = MLPClassifier(hidden_layer_sizes=(3,), activation="relu", learning_rate_init=0.003, max_iter=200, random_state=0)

    # Training and prediction
    classifier1.fit(train_x, train_y)
    classifier2.fit(train_x2, train_y2)

    accuracy1, precision1 = calculate_accuracy(classifier1.predict(test_x), test_y)
    accuracy2, precision2 = calculate_accuracy(classifier2.predict(test_x2), test_y2)

    print(f"Accuracy with all cols: {accuracy1}, Precision: {precision1}")
    print(f"Accuracy with one col removed: {accuracy2}, Precision: {precision2}")

    # Output
    if accuracy1 > accuracy2:
        print("Klasifiktorot so site koloni ima pogolema tochnost")
        print(precision1)
    elif accuracy1 < accuracy2:
        print("Klasifiktorot so edna kolona pomalku ima pogolema tochnost")
        print(precision2)
    else:
        print("Klasifikatorite imaat ista tochnost")
        print(precision1)

    print()

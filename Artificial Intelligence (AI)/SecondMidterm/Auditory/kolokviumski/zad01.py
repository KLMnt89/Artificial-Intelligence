from dataset01 import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score


def split_train_test(data, percent):
    train = data[:int(len(data) * percent * 1.0 / 100)]
    test = data[int(len(data) * percent * 1.0 / 100):]

    return train, test


def split_x_y(data):
    data_x = [row[:-1] for row in data]
    data_y = [row[-1] for row in data]

    return data_x, data_y


if __name__ == '__main__':
    p = int(input())
    c = input()
    l = int(input())

    train_set, test_set = split_train_test(dataset, p)

    train_x, train_y = split_x_y(train_set)
    test_x, test_y = split_x_y(test_set)

    classifier = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    classifier.fit(train_x, train_y)

    predictions = classifier.predict(test_x)
    accuracy = accuracy_score(test_y, predictions)
    print(f"Accuracy with original classifier : {accuracy}")

    # ------binarna klasifikacija

    train_y_perch = [1 if y == "Perch" else 0 for y in train_y]
    test_y_perch = [1 if y == "Perch" else 0 for y in test_y]

    train_y_roach = [1 if y == "Roach" else 0 for y in train_y]
    test_y_roach = [1 if y == "Roach" else 0 for y in test_y]

    train_y_bream = [1 if y == "Bream" else 0 for y in train_y]
    test_y_bream = [1 if y == "Bream" else 0 for y in test_y]

    classifier_perch = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    classifier_perch.fit(train_x, train_y_perch)
    classifier_roach = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    classifier_roach.fit(train_x, train_y_roach)
    classifier_bream = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    classifier_bream.fit(train_x, train_y_bream)

    ac = 0
    for x, y in zip(test_x, test_y):
        perch = classifier_perch.predict([x])[0]
        roach = classifier_roach.predict([x])[0]
        bream = classifier_bream.predict([x])[0]

        if y == "Bream":
            if bream == 1 and perch == 0 and roach == 0:
                ac += 1
        elif y == "Perch":
            if perch == 1 and bream == 0 and roach == 0:
                ac += 1
        elif y == "Roach":
            if roach == 1 and bream == 0 and perch == 0:
                ac += 1

    ac = ac / len(test_y)

    print(f"Accuracy with collection of classifiers: {ac}")

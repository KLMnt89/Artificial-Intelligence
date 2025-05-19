from sklearn.naive_bayes import GaussianNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from dataset13 import dataset


def accuracy_classifiers(gaussian, decision_tree, random_forest,test_x,test_y):
    acc = 0
    for x,y in zip(test_x, test_y):
        ctr = 0
        pred0 = gaussian.predict([x])[0]
        pred1 = decision_tree.predict([x])[0]
        pred2 = random_forest.predict([x])[0]
        if pred0 == y:
            ctr += 1
        if pred1 == y:
            ctr += 1
        if pred2 == y:
            ctr += 1
        if ctr >= 2:
            acc += 1

    return acc / len(test_y)



if __name__ == '__main__':
    x1 = float(input())
    x2 = float(input())

    print(dataset)

    # Naiven klasifikator
    classifier0 = GaussianNB()
    train_set0 = dataset[:int(len(dataset) * x1)]
    train_x0 = [x[:-1] for x in train_set0]
    train_y0 = [x[-1] for x in train_set0]

    test_set = dataset[int(len(dataset) * x2):]
    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    classifier0.fit(train_x0, train_y0)

    # Drvo na odluka
    classifier1 = DecisionTreeClassifier(random_state=0)
    train_set1 = dataset[int(len(dataset) * x1):int(len(dataset) * x2)]
    train_x1 = [x[:-1] for x in train_set1]
    train_y1 = [x[-1] for x in train_set1]

    classifier1.fit(train_x1, train_y1)

    # Kolekcija od drva(shuma)
    classifier2 = RandomForestClassifier(n_estimators=3, random_state=0)
    train_set2 = dataset[:int(len(dataset) * x2)]
    train_x2 = [x[:-1] for x in train_set2]
    train_y2 = [x[-1] for x in train_set2]

    classifier2.fit(train_x2, train_y2)

    acc = accuracy_classifiers(classifier0,classifier1,classifier2,test_x,test_y)

    print(acc)
    print()

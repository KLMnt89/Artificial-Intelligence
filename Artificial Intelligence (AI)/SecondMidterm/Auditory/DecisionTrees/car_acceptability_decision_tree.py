from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder
import csv

def read_file(file):
    with open (file) as doc:
        csv_reader = csv.reader(doc,delimiter=',')
        dataset = list(csv_reader)[1:]

    return dataset

if __name__ == '__main__':
    dataset = read_file("car.csv")

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    # classifier = DecisionTreeClassifier(criterion='entropy',max_depth=5,max_leaf_nodes=20,random_state=0)
    classifier = DecisionTreeClassifier(criterion='entropy',random_state=0)
    classifier.fit(train_x, train_y) # karakteristikite na podatocnoto mnozestvo i klasite

    print(f'Tree depth : {classifier.get_depth()}')
    print(f'Number of leaves : {classifier.get_n_leaves()}')
    print(f'Accuracy : {classifier.score(test_x, test_y)}') # uspesnost na predviduvanje na klasata

    feature_importances = list(classifier.feature_importances_)
    for i in range(len(feature_importances)):
        feature_importances[i] = float(feature_importances[i])

    print(f'Feature importances: {feature_importances}')

    mostImportant = feature_importances.index(max(feature_importances))
    print(f'Index of most important feature: {mostImportant}')

    leastImportant = feature_importances.index(min(feature_importances))
    print(f'Index of least important feature: {leastImportant}')

    print()

    train_x_new1 = list()
    for t in train_x :
        row = [t[i] for i in range(len(t)) if i != mostImportant] # kopija na mnozestvoto bez najvaznata karakteristika
        train_x_new1.append(row)

    test_x_new1 = list()
    for t in test_x :
        row = [t[i] for i in range(len(t)) if i != mostImportant]
        test_x_new1.append(row)

    train_x_new2 = list()
    for t in train_x:
        row = [t[i] for i in range(len(t)) if i != leastImportant]  # kopija na mnozestvoto bez najvaznata karakteristika
        train_x_new2.append(row)

    test_x_new2 = list()
    for t in test_x:
        row = [t[i] for i in range(len(t)) if i != leastImportant]
        test_x_new2.append(row)

    classifier2 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier2.fit(train_x_new1, train_y)

    classifier3 = DecisionTreeClassifier(criterion='entropy', random_state=0)
    classifier3.fit(train_x_new2, train_y)

    print(f'Tree depth (without most important feature): {classifier2.get_depth()}')
    print(f'Number of leaves (without most important feature): {classifier2.get_n_leaves()}')
    print(f'Accuracy (without most important feature): {classifier2.score(test_x_new1, test_y)}')

    print()

    print(f'Tree depth (without least important feature): {classifier3.get_depth()}')
    print(f'Number of leaves (without least important feature): {classifier3.get_n_leaves()}')
    print(f'Accuracy (without least important feature): {classifier3.score(test_x_new2, test_y)}')


    print()


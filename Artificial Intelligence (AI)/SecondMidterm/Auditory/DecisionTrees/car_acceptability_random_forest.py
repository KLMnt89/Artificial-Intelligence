from sklearn.preprocessing import OrdinalEncoder
from sklearn.ensemble import RandomForestClassifier
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

    classifier = RandomForestClassifier(n_estimators=350,criterion='gini',random_state=0)
    classifier.fit(train_x, train_y)

    print(f'Accuracy : {classifier.score(test_x, test_y)}')

    feature_importances = list(classifier.feature_importances_)
    for i in range(len(feature_importances)):
        feature_importances[i] = float(feature_importances[i])

    print(f'Feature importances: {feature_importances}')

    mostImportant = feature_importances.index(max(feature_importances))
    print(f'Index of most important feature: {mostImportant}')

    leastImportant = feature_importances.index(min(feature_importances))
    print(f'Index of least important feature: {leastImportant}')
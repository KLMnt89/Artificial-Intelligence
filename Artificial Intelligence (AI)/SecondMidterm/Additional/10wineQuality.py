import os
import random

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler, OrdinalEncoder
from sklearn.exceptions import ConvergenceWarning
from dataset10 import dataset


def dataset_class(dataset):
    dataset_v2 = []
    for row in dataset:
        dataset_v2.append(row[:-1])
        if row[-1] >= 5:
            dataset_v2[-1].append(1)
        else:
            dataset_v2[-1].append(0)

    return dataset_v2


def del_class(dataset, index):
    dataset_v3 = []
    for row in dataset:
        new_row = row[:index] + row[index + 1:]
        dataset_v3.append(new_row)

    return dataset_v3


if __name__ == '__main__':
    warnings.filterwarnings('ignore', category=ConvergenceWarning)

    # Читање на процент за тестирање од стандардниот влез
    x = int(input()) / 100

    dataset = dataset_class(dataset)
    # encoder = OrdinalEncoder()
    # encoder.fit([x[:-1] for x in dataset])

    split_index = int(len(dataset) * x)
    print(split_index)
    train_set = dataset[split_index:]
    test_set = dataset[:split_index]
    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]
    # train_x = encoder.transform(train_x)


    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]
    # test_x = encoder.transform(test_x)

    classifier1 = DecisionTreeClassifier(criterion='gini', random_state=0)
    classifier1.fit(train_x, train_y)

    feature_importances = list(classifier1.feature_importances_)

    for i in range(len(feature_importances)):
        feature_importances[i] = float(feature_importances[i])

    least_important = feature_importances.index(min(feature_importances))
    dataset2 = del_class(dataset, least_important)

    #rabotime so nov dataset sega
    train2_set = dataset2[split_index:]
    test2_set = dataset2[:split_index]

    train2_x = [x[:-1] for x in train2_set]
    train2_y = [x[-1] for x in train2_set]

    test2_x = [x[:-1] for x in test2_set]
    test2_y = [x[-1] for x in test2_set]

    scaler1 = StandardScaler()
    scaler1.fit(train2_x)  # standardna devijacija
    scaler2 = MinMaxScaler()
    scaler2.fit(train2_x)

    classifier2 = MLPClassifier((15,), activation="relu", learning_rate_init=0.001, max_iter=200, random_state=0)

    classifier2.fit(scaler1.transform(train2_x), train2_y) #StandardScaler
    print(f"Tocnost so StandardScaler: {classifier2.score(scaler1.transform(test2_x), test2_y)}")
    classifier2.fit(scaler2.transform(train2_x), train2_y) #MinMaxScaler
    print(f"Tocnost so MinMaxScaler: {classifier2.score(scaler2.transform(test2_x), test2_y)}")

    print()

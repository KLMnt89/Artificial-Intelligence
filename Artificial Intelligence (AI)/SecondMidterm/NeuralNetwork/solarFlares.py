from sfDataset import dataset
import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier

warnings.filterwarnings("ignore")


def divide_class(dataset):
    dataset_class0, dataset_class1 = [], []
    for row in dataset:
        if row[-1] == 0:
            dataset_class0.append(row)
        else:
            dataset_class1.append(row)
    return dataset_class0, dataset_class1

def accuracy(predictions,test_y):
    acc = 0
    for pred,true in zip(predictions,test_y):
        if pred == true:
            acc += 1

    return acc/len(test_y)


if __name__ == '__main__':
    dataset0, dataset1 = divide_class(dataset)

    train_set0 = dataset0[:int(len(dataset0) * 0.8)]
    val_set0 = dataset0[int(len(dataset0) * 0.8):]
    train_x0 = [x[:-1] for x in train_set0]
    train_y0 = [x[-1] for x in train_set0]
    val_x0 = [x[:-1] for x in val_set0]
    val_y0 = [x[-1] for x in val_set0]

    train_set1 = dataset1[:int(len(dataset1) * 0.8)]
    val_set1 = dataset1[int(len(dataset1) * 0.8):]
    train_x1 = [x[:-1] for x in train_set1]
    train_y1 = [x[-1] for x in train_set1]
    val_x1 = [x[:-1] for x in val_set1]
    val_y1 = [x[-1] for x in val_set1]

    train_x = train_x0 + train_x1
    train_y = train_y0 + train_y1
    val_x = val_x0 + val_x1
    val_y = val_y0 + val_y1

    learning_rate = float(input())
    iter = int(input())
    classifier = MLPClassifier(hidden_layer_sizes=6,max_iter=iter,learning_rate_init=learning_rate, activation="tanh", random_state=0)
    classifier.fit(train_x, train_y)

    train_acc = accuracy(classifier.predict(train_x), train_y)
    val_acc = accuracy(classifier.predict(val_x), val_y)
    #val_acc = classifier.score(val_x, val_y)

    if train_acc - val_acc  > val_acc*0.15:
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    print(f"Tochnost so trenirachko mnozhestvo: {train_acc}")
    print(f"Tochnost so validacisko mnozhestvo: {val_acc}")

    print()
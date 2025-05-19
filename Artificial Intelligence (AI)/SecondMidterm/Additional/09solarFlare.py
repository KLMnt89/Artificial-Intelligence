import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

import warnings
from sklearn.neural_network import MLPClassifier
from dataset09 import dataset

warnings.filterwarnings("ignore")

if __name__ == "__main__":
    x_num = int(input())

    train_set = dataset[:-x_num]
    train_x = [x[:-1] for x in train_set]
    train_y = [int(x[-1]) for x in train_set]

    test_set = dataset[-x_num:]
    test_x = [x[:-1] for x in test_set]
    test_y = [int(x[-1]) for x in test_set]

    classifier = MLPClassifier((3,), activation='relu', learning_rate_init=0.003, max_iter=200, random_state=0)
    classifier.fit(train_x, train_y)

    tp,fp,tn,fn = 0,0,0,0
    predictions = classifier.predict(test_x)
    for pred, true in zip(predictions, test_y):
        if pred == true and true == 1:
            tp += 1
        elif pred == true and true == 0:
            tn += 1
        elif pred != true and true == 1:
            fn += 1
        elif pred != true and true == 0:
            fp += 1
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0
    print("Precision:", precision)
    print("Recall:", recall)



from wdbcDataset import dataset
from sklearn.preprocessing import MinMaxScaler
from sklearn.neural_network import MLPClassifier


def dataset_map(dataset):
    # ['M', 17.99, 10.38, 122.8, 1001.0, 0.1184, 0.2776, 0.3001, 0.1471, 0.2419, 0.07871, 1.095, 0.9053, 8.589, 153.4,
    #     0.006399, 0.04904, 0.05373, 0.01587, 0.03003, 0.006193, 25.38, 17.33, 184.6, 2019.0, 0.1622, 0.6656, 0.7119,
    #     0.2654, 0.4601, 0.1189]
    benign = []
    malignant = []
    for row in dataset:
        if row[0] == "B":
            row[0] = int(0)
            benign.append(row)
        else:
            row[0] = int(1)
            malignant.append(row)

    return benign, malignant


if __name__ == '__main__':
    benign, malignant = dataset_map(dataset)

    train_setB = benign[:int(len(benign) * 0.7)]
    train_xB = [x[1:] for x in train_setB]
    train_yB = [x[0] for x in train_setB]

    test_setB = benign[int(len(benign) * 0.7):]
    test_xB = [x[1:] for x in test_setB]
    test_yB = [x[0] for x in test_setB]

    train_setM = malignant[:int(len(malignant) * 0.7)]
    train_xM = [x[1:] for x in train_setM]
    train_yM = [x[0] for x in train_setM]

    test_setM = malignant[int(len(malignant) * 0.7):]
    test_xM = [x[1:] for x in test_setM]
    test_yM = [x[0] for x in test_setM]

    x_train = train_xM + train_xB
    y_train = train_yM + train_yB

    x_test = test_xM + test_xB
    y_test = test_yM + test_yB

    scaler = MinMaxScaler(feature_range=(-1, 1))
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

    hidden = int(input())
    classifier = MLPClassifier(hidden_layer_sizes=(hidden,), learning_rate_init=0.001, max_iter=20, activation="relu",
                               random_state=0)

    classifier.fit(x_train, y_train)

    # Evaluacija na trenirachko mnozhestvo
    train_predictions = classifier.predict(x_train)

    tp_train, fp_train, tn_train, fn_train = 0, 0, 0, 0
    for pred, true in zip(train_predictions, y_train):
        if pred == true and pred == 1:
            tp_train += 1
        elif pred == true and pred == 0:
            tn_train += 1
        elif pred != true and pred == 1:
            fp_train += 1
        elif pred != true and pred == 0:
            fn_train += 1

    precision_train = tp_train / (tp_train + fp_train)
    recall_train = tp_train / (tp_train + fn_train)

    print(f"Preciznost so trenirachkoto mnozhestvo: {precision_train}")
    print(f"Odziv so trenirachkoto mnozhestvo: {recall_train}")

    tp, fp, tn, fn = 0, 0, 0, 0
    predictions = classifier.predict(x_test)

    for pred, true in zip(predictions, y_test):
        if pred == true and pred == 1:
            tp += 1
        elif pred == true and pred == 0:
            tn += 1
        elif pred != true and pred == 1:
            fp += 1
        elif pred != true and pred == 0:
            fn += 1

    precision_test = tp / (tp + fp)
    recall_test = tp / (tp + fn)

    print(f"Preciznost so testirachkoto mnozhestvo: {precision_test}")
    print(f"Odziv so testirachkoto mnozhestvo: {recall_test}")


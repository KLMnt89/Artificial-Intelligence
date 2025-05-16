import csv
from wineQuality import read_dataset, divide_sets
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import MinMaxScaler, StandardScaler

if __name__ == "__main__":
    data = read_dataset()
    train_set, val_set, test_set = divide_sets(data)

    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    test_x = [x[:-1] for x in test_set]
    test_y = [x[-1] for x in test_set]

    scaler1 = StandardScaler()
    scaler1.fit(train_x)  # standardna devijacija
    scaler2 = MinMaxScaler()
    scaler2.fit(train_x)

    classifier1 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier2 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)
    classifier3 = MLPClassifier(10, activation="relu", learning_rate_init=0.001, max_iter=500, random_state=0)

    classifier1.fit(train_x, train_y)
    classifier2.fit(scaler1.transform(train_x), train_y)
    classifier3.fit(scaler2.transform(train_x), train_y)

    val_acc1 = 0
    val_predictions1 = classifier1.predict(val_x)
    for true, pred in zip(val_y, val_predictions1):
        if true == pred:
            val_acc1 += 1
    val_acc1 /= len(val_y)

    print(f"Accuracy for classifier 1 is {val_acc1} - this is without normalization")

    val_acc2 = 0
    val_predictions2 = classifier2.predict(scaler1.transform(val_x))
    for true, pred in zip(val_y, val_predictions2):
        if true == pred:
            val_acc2 += 1
    val_acc2 /= len(val_y)

    print(f"Accuracy for classifier 2 is {val_acc2} - this is with standard normalization")

    val_acc3 = 0
    val_predictions3 = classifier3.predict(scaler2.transform(val_x))
    for true, pred in zip(val_y, val_predictions3):
        if true == pred:
            val_acc3 += 1
    val_acc3 /= len(val_y)

    print(f"Accuracy for classifier 3 is {val_acc3} - this is with minmax normalization")

    tp,fp,tn,fn = 0,0,0,0
    predictions = classifier3.predict(scaler2.transform(test_x))
    for pred,true in zip(predictions,test_y):
        if pred == true and pred == "good":
            tp += 1
        elif pred == true and pred == "bad":
            tn += 1
        elif pred != true and pred == "good":
            fp += 1
        elif pred != true and pred == "bad":
            fn += 1

    acc = (tp+tn)/(tp+tn+fp+fn)
    precision = tp/(tp+fp)
    recall = tp/(tp+fn)
    f1 = 2*(precision*recall)/(precision+recall)
    print(f"Accuracy for final_classifier is {acc}")
    print(f"Precision for final_classifier is {precision}")
    print(f"Recall for final_classifier is {recall}")
    print(f"F1 for final_classifier is {f1}")



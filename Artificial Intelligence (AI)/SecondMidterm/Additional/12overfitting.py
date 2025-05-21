from dataset12 import dataset
from sklearn.preprocessing import StandardScaler, MinMaxScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier


def del_col(dataset, col_index):
    dataset2 = []
    for row in dataset:
        new_row = row[:col_index] + row[col_index + 1:]
        dataset2.append(new_row)
    return dataset2


def accuracy(predictions, test_Y):
    acc = 0
    for pred, actual in zip(predictions, test_Y):
        if pred == actual:
            acc += 1
    return acc / len(test_Y)


if __name__ == "__main__":
    hidden_neurons = int(input())  # broj na nevroni vo skrieniot sloj
    learning_rate = float(input())  # rata na ucenje
    col_index = int(input())  # broj na kolona za brisenje
    entry = [float(x) for x in input().split(" ")]

    train_set = dataset[:int(len(dataset) * 0.8)]
    train_x = [x[:-1] for x in train_set]
    train_y = [x[-1] for x in train_set]

    val_set = dataset[int(len(dataset) * 0.8):]
    val_x = [x[:-1] for x in val_set]
    val_y = [x[-1] for x in val_set]

    scaler = MinMaxScaler(feature_range=(-1, 1))
    scaler.fit(train_x)

    classifier1 = MLPClassifier(hidden_layer_sizes=hidden_neurons, activation="relu", learning_rate_init=learning_rate,
                                max_iter=20, random_state=0)
    classifier1.fit(scaler.transform(train_x), train_y)

    train_acc = accuracy(classifier1.predict(scaler.transform(train_x)), train_y)
    val_acc = accuracy(classifier1.predict(scaler.transform(val_x)), val_y)
    a = val_acc * 0.15

    if float(train_acc) - val_acc > float(a):
        train_x_new = del_col(train_x, col_index)
        print(train_x_new[0])
        scaler.fit(train_x_new)
        classifier1.fit(scaler.transform(train_x_new), train_y)
        entry = entry[:col_index] + entry[col_index + 1:]
        # print(entry)
        print("Se sluchuva overfitting")
    else:
        print("Ne se sluchuva overfitting")

    print(classifier1.predict(scaler.transform([entry]))[0])

    print()
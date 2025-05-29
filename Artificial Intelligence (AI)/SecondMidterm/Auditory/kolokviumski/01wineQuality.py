import csv

from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler


def read_dataset():
    data = []
    with open("winequality01.csv") as f:
        _ = f.readline()  # za headerite
        while True:
            line = f.readline().strip()  # prajme strip vo slucaj da mi prazni mesta
            if line == "":
                break
            parts = line.split(";")
            data.append(list(map(float, parts[:-1])) + [parts[-1]])
    return data


def sum_2column(dataset):
    data = []
    for row in dataset:
        new_row = row.copy()
        a1 = row[0]
        a2 = row[-2]
        sumColumn = a1 + a2
        new_row[0] = sumColumn
        del new_row[-2]
        data.append(new_row)
    return data


def split_dataset(dataset, C, P):
    # Раздели ги податоците според класата
    good_data = [row for row in dataset if row[-1] == 'good']
    bad_data = [row for row in dataset if row[-1] == 'bad']

    # Подели ги податоците според критериумот C
    def split(data, C, P):
        n = len(data)
        split_point = int(n * P / 100)
        if C == 0:
            train = data[:split_point]
            test = data[split_point:]
        else:
            train = data[-split_point:]
            test = data[:-split_point]
        return train, test

    good_train, good_test = split(good_data, C, P)
    bad_train, bad_test = split(bad_data, C, P)

    train_set = good_train + bad_train
    test_set = good_test + bad_test
    return train_set, test_set


if __name__ == "__main__":
    dataset = read_dataset()
    data = sum_2column(dataset)
    c = int(input())
    p = int(input()) / 100

    train_set, test_set = split_dataset(data, c, p)
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]

    classifier1 = GaussianNB()
    classifier1.fit(train_x, train_y)

    scaler = MinMaxScaler(feature_range=(-1, 1))
    train_x_scaled = scaler.fit_transform(train_x)
    test_x_scaled = scaler.transform(test_x)
    classifier2 = GaussianNB()
    classifier2.fit(train_x_scaled, train_y)

    print(f"Tochnost so zbir na koloni: {classifier1.score(test_x, test_y)}")
    print(f"Tochnost so zbir na koloni i skaliranje: {classifier2.score(test_x_scaled, test_y)}")
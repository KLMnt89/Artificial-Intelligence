import csv
from sklearn.naive_bayes import GaussianNB


def read_file(file):
    with open (file) as doc:
        csv_reader = csv.reader(doc,delimiter=',')
        dataset = list(csv_reader)[1:]

    dataset_v2 = []
    for row in dataset :
        row_v2 = [int(e) for e in row]
        dataset_v2.append(row_v2)

    return dataset_v2


if __name__ == '__main__':
    dataset = read_file("medical_data.csv")

    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set]  # karakteristikite do klasata
    train_y = [row[-1] for row in train_set]  # samo klasata

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set]  # karakteristikite do klasata
    test_y = [row[-1] for row in test_set]  # samo klasata

    classifier = GaussianNB()
    classifier.fit(train_x, train_y)

    accuracy = 0
    for i in range(len(test_x)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    print(f'Accuracy: {accuracy / len(test_x)}')
import csv
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder


def read_file(file_name):
    with open(file_name) as doc :
        csv_reader = csv.reader(doc, delimiter=',') #iterator koj obezbeduva pristap do site redovi
        dataset = list(csv_reader)[1:]

    return dataset

if __name__ == '__main__':
    dataset = read_file("car.csv")

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset]) #mapiranje na site elementi osven klasata

    #prvite najcesto se za treniranje
    train_set = dataset[:int(0.7 * len(dataset))]
    train_x = [row[:-1] for row in train_set] #karakteristikite do klasata
    train_y = [row[-1] for row in train_set] #samo klasata
    train_x = encoder.transform(train_x)

    test_set = dataset[int(0.7 * len(dataset)):]
    test_x = [row[:-1] for row in test_set] #karakteristikite do klasata
    test_y = [row[-1] for row in test_set] #samo klasata
    test_x = encoder.transform(test_x)

    classifier = CategoricalNB()
    classifier.fit(train_x, train_y) # sto e vlez a sto e izlez (kje presmeta frekfencii spored baesovata teorema)

    accuracy = 0
    for i in range(len(test_x)):
        predicted_class = classifier.predict([test_x[i]])[0]
        true_class = test_y[i]
        if predicted_class == true_class:
            accuracy += 1

    print(f'Accuracy: {accuracy / len(test_x)}') # tocnost na klasifikator

    entry = [e for e in input().split(' ')] # klasifikacija na nov primerok procitan od standarden vlez
    encoder_entry = encoder.transform([entry])
    predicted_class = classifier.predict(encoder_entry)[0]
    print(predicted_class)
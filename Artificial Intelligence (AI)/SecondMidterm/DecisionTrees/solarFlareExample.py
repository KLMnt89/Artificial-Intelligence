import os
os.environ['OPENBLAS_NUM_THREADS'] = '1'

from sklearn.preprocessing import OrdinalEncoder
from sklearn.tree import DecisionTreeClassifier
from zad3_dataset import dataset
from sklearn.metrics import confusion_matrix

if __name__ == '__main__':

    X = int(input())
    criteria = 'gini'
    classifier = DecisionTreeClassifier(criterion=criteria, random_state=0)


    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_set = dataset [:-X]
    train_x = [row[:-1] for row in train_set]
    train_y = [row[-1] for row in train_set]
    train_x = encoder.transform(train_x)

    test_set = dataset[-X:]
    test_x = [row[:-1] for row in test_set]
    test_y = [row[-1] for row in test_set]
    test_x = encoder.transform(test_x)

    classifier.fit(train_x, train_y)

    cm = confusion_matrix(test_y, classifier.predict(test_x))
    # Проверка дали има 2 класи
    if cm.shape == (1, 1):
        tn = cm[0][0]
        fp = fn = tp = 0  # нема негативни и позитивни примери, па ги поставуваме на 0
    else:
        tn, fp, fn, tp = cm.ravel()  # Распакување на конфузиската матрица на 4 вредности
    # TP - точно предвидени позитивни
    # FP - грешно предвидени позитивни
    # FN - грешно предвидени негативни
    # TN - точно предвидени негативни

    accuracy = (tp + tn) / (tp + tn + fp + fn)
    if int(tp + fp) > 0:
        precision = tp / (tp + fp)
    else:
        precision = 0.0

    print(f"Accuracy: {accuracy}")
    if precision ==0 :
        precision = 0.0
    print(f"Precision: {precision}")
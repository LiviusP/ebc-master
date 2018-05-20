import csv

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier


def main():
    train_data = []
    # read the training file
    with open("s3.training.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            train_data.append(row[:-1])

    classifier = KMeans(n_clusters=4, random_state=0)
    classifier.fit(train_data)

    test_data = []
    test_labels = []
    # read the training file
    with open("s3.test.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            test_data.append(row[:-1])

    predicted_labels = classifier.predict(test_data)

    for index in range(len(test_data)):
         print("For test number {}, predicted {}".format(index, predicted_labels[index]))



if __name__ == '__main__':
    main()

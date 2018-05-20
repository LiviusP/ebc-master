import csv

from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier


def main():
    train_data = []
    train_labels = []
    # read the training file
    with open("s3.training.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            train_data.append([float(x) for x in row[:-1]])  # get a list of all element but the last
            train_labels.append(row[-1])  # append the label for the above mentioned list

    classifier = DecisionTreeClassifier()
    classifier.fit(train_data, train_labels)

    test_data = []
    test_labels = []
    # read the training file
    with open("s3.test.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            test_data.append(row[:-1])  # get a list of all element but the last
            test_labels.append(row[-1])  # append the label for the above mentioned list

    predicted_labels = classifier.predict(test_data)

    for index in range(len(test_data)):
        print("For test number {}, predicted {}, expected {}".format(index, predicted_labels[index], test_labels[index]))

    print(metrics.classification_report(test_labels, predicted_labels))


if __name__ == '__main__':
    main()

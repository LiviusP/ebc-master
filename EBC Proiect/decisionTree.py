import csv
from sklearn import tree
from sklearn import metrics
import util


def main():
    slice_factor = 0.9
    data = []
    labels = []
    # read the file
    with open("auto.csv") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data.append(row[3:])  # get a list of all element but the last
            labels.append(row[0])  # append the label for the above mentioned list


    train_data = (data[10:],
                  labels[10:])  # create a tuple with first 90% of data and labels
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(train_data[0], train_data[1])

    expected_labels = labels[:10]
    predicted = classifier.predict(data[:10])  # predict the last 10% of data

    correct = len([item for item in zip(expected_labels, predicted) if item[0] == item[1]])
    print('correct:', correct, ' incorrect:', len(expected_labels) - correct)

    print(metrics.classification_report(expected_labels, predicted))

if __name__ == '__main__':
    main()

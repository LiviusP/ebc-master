import csv
from sklearn import tree
from sklearn import metrics


def main():
    slice_factor = 0.9
    data = []
    labels = []
    # read the file
    with open("iris.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            data.append(row[:-1])  # get a list of all element but the last
            labels.append(row[-1])  # append the label for the above mentioned list
    train_data = (data[:int(slice_factor * len(data))],
                  labels[:int(slice_factor * len(labels))])  # create a tuple with first 90% of data and labels
    classifier = tree.DecisionTreeClassifier()
    classifier.fit(train_data[0], train_data[1])

    expected_labels = labels[int(slice_factor * len(labels)):]
    predicted = classifier.predict(data[int(slice_factor * len(data)):])  # predict the last 10% of data

    correct = len([item for item in zip(expected_labels, predicted) if item[0] == item[1]])
    print('correct:', correct, ' incorrect:', len(expected_labels) - correct)

    print(metrics.classification_report(expected_labels, predicted))

if __name__ == '__main__':
    main()

import csv

from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.tree import DecisionTreeClassifier


def main():
    train_data = []
    # read the training file
    with open("iris.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            train_data.append(row[:-1])

    classifier = KMeans(n_clusters=3, random_state=0)
    classifier.fit(train_data)

    test_data = []
    test_labels = []
    test_clusters = []
    # read the training file
    with open("iris.data") as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            test_data.append(row[:-1])
            test_clusters.append(row[:])


    predicted_labels = classifier.predict(test_data)


    result_clusters = []

    for i in range(3):
        result_clusters.append({"Iris-setosa" : 0,
                "Iris-versicolor" : 0,
                "Iris-virginica" : 0
                })

    for index in range(len(test_data)):
         print("For test number {}, predicted {}, expected {}".format(index, predicted_labels[index], test_clusters[index][-1]))
         result_clusters[predicted_labels[index]][test_clusters[index][-1]] += 1
         

    for index, cluster in enumerate(result_clusters):
        n = 0
        suma = 0
        maxim = 0
        for key in cluster.keys():
            suma += cluster[key] 
            if cluster[key] > maxim:
                maxim = cluster[key]
            if cluster[key] > 0:
                n += 1
        print("Clusterul {} este performant in masura de: {}/{}".format(index, maxim, suma))

if __name__ == '__main__':
    main()

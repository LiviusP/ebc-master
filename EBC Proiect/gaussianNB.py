from sklearn.naive_bayes import GaussianNB
import util

def main():
    documents = util.getAutoFeaturesSk('auto')
    samples = documents[10:]
    test = documents[:10]
    sampleFeatures = [item['features'] for item in samples]
    sampleOutcomes = [item['outcome'] for item in samples]
    gnb = GaussianNB()
    c = gnb.fit(sampleFeatures, sampleOutcomes)
    testFeatures = [item['features'] for item in test]
    testOutcomes = [item['outcome'] for item in test]
    predicted = c.predict(testFeatures)

    correct = len([item for item in zip(testOutcomes, predicted) if item[0] == item[1]])
    print('correct : ', correct, ' |  incorrect  : ', 10 - correct)
    
if __name__ == '__main__':
    main()
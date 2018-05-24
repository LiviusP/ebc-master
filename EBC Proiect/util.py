def getAutoFeatures(filename, threshold = 0):
    results = []
    with open(filename + '.names') as f:
        names = [line.split(':')[0] for line in f.readlines()]
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [item.strip() for item in items]
            classification = items[0]
            features = items[1:]
            autoFeatures = []
            for index, item in enumerate(features):
                if item > threshold:
                    autoFeatures.append(item)
            result = {'features' : autoFeatures, 'outcome' : classification}
            results.append(result)
    return results

def getFeatures(item):
    return item['features']

def getAutoFeaturesSk(filename):
    results = []
    with open(filename + '.names') as f:
        names = [line.split(':')[0] for line in f.readlines()]
    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [item.strip() for item in items]
            classification = items[0]
            features = items[1:]
            autoFeatures = []
            for index, item in enumerate(features):
                if item.replace('.', '', 1).isdigit():
                    autoFeatures.append(float(item))
            result = {'features' : autoFeatures, 'outcome' : classification}
            results.append(result)
    return results

                    
def main():
    results = getAutoFeaturesSk('auto')
    print(results[:5])

if __name__ == '__main__':
    main()
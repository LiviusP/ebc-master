def loadAutoData(filename = 'auto'):
    with open(filename + '.names') as f:
        names = [line.split(':')[0] for line in f.readlines()]

    colnames = names[:]
    rownames = []
    data = []
    carNumber = 1000

    with open(filename + '.csv') as f:
        for line in f.readlines():
            items = line.split(',')
            items = [item.strip() for item in items]
            classification = items[0]
            rownames.append(str(carNumber) + items[2])
            carNumber+=1
            features = items[1:]
            del(features[1])
            for index, feature in enumerate(features):
              features[index] = float(feature)

            data.append(features)
    return rownames, colnames, data  

def main():
  rownames, colnames, data = loadAutoData()
  print(rownames[0])
  print(colnames[3])
  print(data[1])

if __name__ == '__main__':
  main()
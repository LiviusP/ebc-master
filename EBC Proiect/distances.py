from math import sqrt

def euclidean(v1, v2):
    sumSq = sum([(x - y) ** 2 for (x, y) in zip(v1, v2)])
    return 1 / (1 + sqrt(sumSq))

def main():
    sample1 = [0,0]
    sample2 = [1,1]
    print(euclidean(sample1, sample2))

if __name__ == '__main__':
    main()
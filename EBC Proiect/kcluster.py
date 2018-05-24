from loaders import loadAutoData
from distances import euclidean
from random import random
from PIL import Image, ImageDraw
from math import sqrt

def kcluster(rows, distance = euclidean, k = 5):
	ranges = [(min([row[i] for row in rows]), max([row[i] for row in rows])) for i in range(len(rows[0]))]
	print (ranges)
	clusters = [[random() * (ranges[i][1] - ranges[i][0]) + ranges[i][0] for i in range(len(rows[0]))] for j in range(k)]
	lastMatches = None
	for t in range(100):
		bestMatches = [[] for i in range(k)]
		for j in range((len(rows))):
			currentRow = rows[j]
			bestMatch = 0
			for i in range(k):
				d = distance(clusters[i], currentRow)
				if d > distance(clusters[bestMatch], currentRow):
					bestMatch = i
			bestMatches[bestMatch].append(j)
		if bestMatches == lastMatches:
			break
		lastMatches = bestMatches
		for i in range(k):
			avgs = [0.0] * len(rows[0])
			if (len(bestMatches[i]) > 0):
				for rowId in bestMatches[i]:
					for j in range(len(rows[rowId])):
						avgs[j] += rows[rowId][j]
				for j in range(len(avgs)):
					avgs[j] /= len(bestMatches[i])
				clusters[i] = avgs
	return bestMatches

def scaledown(data,distance = euclidean,rate = 0.03):
	n = len(data)
	realdist = [[distance(data[i],data[j]) for j in range(n)] for i in range(0,n)]
	loc=[[random(),random()] for i in range(n)]
	fakedist = [[0.0 for j in range(n)] for i in range(n)]
	lasterror = None
	for m in range(0,1000):
		for i in range(n):
			for j in range(n):
				fakedist[i][j]=sqrt(sum([pow(loc[i][x]-loc[j][x],2) for x in range(len(loc[i]))]))
		grad = [[0.0,0.0] for i in range(n)]
		totalerror = 0
		for k in range(n):
			for j in range(n):
				if j == k: 
					continue
				errorterm = (fakedist[j][k] - realdist[j][k]) / realdist[j][k]
				grad[k][0] += ((loc[k][0] - loc[j][0]) / fakedist[j][k]) * errorterm
				grad[k][1] += ((loc[k][1]-loc[j][1])/fakedist[j][k]) * errorterm
				totalerror += abs(errorterm)
		if lasterror and lasterror < totalerror: 
			break
		lasterror = totalerror
		for k in range(n):
			loc[k][0] -= rate * grad[k][0]
			loc[k][1] -= rate * grad[k][1]
	return loc

def draw2d(data, clusters, colors,labels,jpeg='kclusters.jpg'):  
	img = Image.new('RGB',(2000,2000),(255,255,255))
	draw = ImageDraw.Draw(img)
	for i in range(len(data)):
		cluster = get_cluster(i, clusters)
		x = (data[i][0] + 10000) * 0.02 + 800
		y = (data[i][1] + 10000) * 0.02 + 800
		if cluster:
			# draw.text((x,y),labels[i], colors[cluster])
			# print('drawing ', colors[cluster], x, y, labels[i])
			draw.text((x,y), labels[i], colors[cluster])
		else:
			draw.text((x,y), labels[i], (255,255,255))
	img.save(jpeg, 'JPEG')

def get_cluster(index, clusters):
	for i, cluster in enumerate(clusters):
		# print(str(i) + " " + str(cluster))
		if index in cluster:
			return i
	return None
				
def main():
	rownames, colnames, data = loadAutoData()
	clusters = kcluster(data, k = 5)
	print(clusters)
	# for k in range(0,5):
	# 	print('content of cluster ' + str(k))
	# 	print([rownames[r] for r in clusters[k]])
	colors = [(255,0,0),(0,255,0), (0,0,255), (255,255,0), (255,0,255)]
	coords = scaledown(data)
	# print(coords)
	draw2d(coords, clusters,colors,rownames)

if __name__ == '__main__':
	main()
from distances import euclidean
from loaders import loadAutoData
from PIL import Image, ImageDraw

class BiCluster:
	def __init__(self, vec, left = None, right = None, id = None, distance = 0.0):
		self.left = left
		self.right = right
		self.vec = vec
		self.id = id
		self.distance = distance

def hcluster(rows, distance = euclidean):
	currentClusterId = -1
	distances = {}
	clusters = [BiCluster(rows[i], id = i) for i in range(len(rows))]
	while len(clusters) > 1:
		# print(len(clusters))
		lowestPair = (0,1)
		closestDistance = distance(clusters[0].vec, clusters[1].vec)
		for i in range(len(clusters)):
			for j in range(i + 1, len(clusters)):
				if (clusters[i].id, clusters[j].id) not in distances:
					distances[(clusters[i].id, clusters[j].id)] = distance(clusters[i].vec, clusters[j].vec)
				if distances[(clusters[i].id, clusters[j].id)] > closestDistance:
					closestDistance = distances[(clusters[i].id, clusters[j].id)]
					lowestPair = (i, j)
		mergeVec = [(clusters[lowestPair[0]].vec[i] + clusters[lowestPair[1]].vec[i]) / 2.0 for i in range(len(clusters[0].vec))]
		newCluster = BiCluster(mergeVec, left = clusters[lowestPair[0]], right = clusters[lowestPair[1]], distance = closestDistance, id = currentClusterId)
		currentClusterId -= 1
		# print('pair ' + str(lowestPair[0]) + ',' + str(lowestPair[1]))
		# print('current length ' + str(len(clusters)))
		del clusters[lowestPair[1]]
		del clusters[lowestPair[0]]
		clusters.append(newCluster)
	return clusters[0]
		
def printClusters(cluster, labels = None, n = 0):
	for i in range(n):
		print(' ')
	if cluster.id < 0:
		print('-')
	else:
		if labels == None:
			print(cluster.id)
		else:
			print(labels[cluster.id])
	if cluster.left != None:
		printClusters(cluster.left, labels = labels, n = n + 1)
	if cluster.right != None:
		printClusters(cluster.right, labels = labels, n = n + 1)

def drawdendrogram(clust,labels,jpeg = 'clusters.jpg'):
	h = getheight(clust) * 20
	w = 1200
	depth = getdepth(clust)
	scaling = float(w - 150) / depth
	img = Image.new('RGB',(w,h),(255,255,255))
	draw = ImageDraw.Draw(img)
	draw.line((0,h / 2,10,h / 2),fill = (255,0,0))    
	drawnode(draw,clust,10,(h/2),scaling,labels)
	img.save(jpeg,'JPEG')

def getheight(clust):
	if clust.left == None and clust.right == None: 
		return 1
	return getheight(clust.left) + getheight(clust.right)

def getdepth(clust):
	if clust.left == None and clust.right == None: 
		return 0
	return max(getdepth(clust.left),getdepth(clust.right))+clust.distance

def drawnode(draw,clust,x,y,scaling,labels):
	if clust.id < 0:
		h1 = getheight(clust.left) * 20
		h2 = getheight(clust.right) * 20
		top = y - (h1 + h2) / 2
		bottom = y + (h1 + h2) / 2
		ll = clust.distance * scaling
		draw.line((x,top + h1 / 2,x,bottom - h2 / 2),fill = (255,0,0))    
		draw.line((x,top + h1 / 2,x + ll,top + h1/2),fill = (255,0,0))    
		draw.line((x,bottom - h2/2,x + ll,bottom - h2 / 2),fill = (255,0,0))        
		drawnode(draw,clust.left,x + ll,top + h1 / 2,scaling,labels)
		drawnode(draw,clust.right,x + ll,bottom - h2 / 2,scaling,labels)
	else:   
		draw.text((x + 5,y - 7),labels[clust.id],(0,0,0))

def main():
	rownames, colnames, data = loadAutoData()
	cluster = hcluster(data)
	# printClusters(cluster, labels = rownames)
	drawdendrogram(cluster, rownames)

if __name__ == '__main__':
	main()
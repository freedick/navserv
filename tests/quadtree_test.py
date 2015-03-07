max = 5
results = 0
messages = []
def run():
	global results,messages
	from util import quadtree
	qt = quadtree.QuadTree(2, 1.0, 1.0, 3.0, 3.0)
	from models.road import RoadPoint
	qt.addPoint(RoadPoint(1.9,2.1,1))
	qt.addPoint(RoadPoint(1.1,1.1,2))

	closest = qt.closestNeighbor(RoadPoint(1.9,1.9,11))
	if closest.lat==1.9 and closest.lng==2.1:
		results+=1
	else:
		messages.append("Closest neigbor check 1 failed")
	closest = qt.closestNeighbor(RoadPoint(1.9,1.9,10))
	if closest.lat==1.9 and closest.lng==2.1:
		results+=1
	else:
		messages.append("Closest neigbor check 2 failed")

	closest = qt.closestNeighbor(RoadPoint(1.3,1.3,9))
	if closest.lat==1.1 and closest.lng==1.1:
		results+=1
	else:
		messages.append("Closest neigbor check 3 failed")

	qt.addPoint(RoadPoint(0.5,1.5,3))

	closest = qt.closestNeighbor(RoadPoint(1.9,1.9,8))
	if closest.lat==1.9 and closest.lng==2.1:
		results+=1
	else:
		messages.append("Closest neigbor check 4 failed")

	qt.addPoint(RoadPoint(0.5,1.5,5))

	closest = qt.closestNeighbor(RoadPoint(1.9,1.9,6))
	if closest.lat==1.9 and closest.lng==2.1:
		results+=1
	else:
		messages.append("Closest neigbor check 5 failed")
def print_results():
	global results, max, messages
	print "tests succeded: %d/%d" % (results, max)
	if len(messages)>0:
		print "messages from tests:"
		for message in messages:
			print "\t",message

import models.road
def distance(pointa, pointb):
	if type(pointb) is Rectangle:
		return distance(pointb, pointa)
	if type(pointa) is Rectangle:
		rect = pointa
		point = pointb
		distances = []
		#Check perpendicular distances
		if rect.min_lat<point.lat<rect.max_lat:
			distances.append(abs(pointa.lng - rect.lng_min))
			distances.append(abs(pointa.lng - rect.lng_max))
		if rect.min_lngat<point.lng<rect.max_lng:
			distances.append(abs(pointa.lng - rect.lng_min))
			distances.append(abs(pointa.lng - rect.lng_max))
		#Check corner distances
		distances.append(distance(point, models.road.RoadPoint(rect.lat_min,rect.lng_min)))
		distances.append(distance(point, models.road.RoadPoint(rect.lat_min,rect.lng_max)))
		distances.append(distance(point, models.road.RoadPoint(rect.lat_max,rect.lng_min)))
		distances.append(distance(point, models.road.RoadPoint(rect.lat_max,rect.lng_max)))
		#Return least distance
		return min(distances)
	return ((pointa.lat-pointb.lat)**2 + (pointa.lng-pointb.lng)**2)**0.5
class Rectangle:
	def __init__(self, lat0, lng0, lat1, lng1):
		self.lat_min = min(lat0,lat1)
		self.long_min = min(lng0, lng1)
		self.lat_max = max(lat0,lat1)
		self.long_max = max(lng0, lng1)
	def contains(self, point):
		return self.lat_min<=point.lat<=self.lat_max and self.lng_min<=point.long<=self.lng_max
	def midpoint(self):
		return ((self.lat_min+self.lat_max)/2,(self.lng_min + self.lng_max)/2)
	def split(self):
		return [
			Rectangle(self.lat_min, self.lng_min, *(self.midpoint())),
			Rectangle(self.lat_min, self.lng_max, *(self.midpoint())),
			Rectangle(self.lat_max, self.lng_min, *(self.midpoint())),
			Rectangle(self.lat_max, self.lng_max, *(self.midpoint())),
			]
	def translate(lat,lng):
		width = self.lat_max - self.lat_min
		height = self.lng_max - self.lng_min
		return Rectangle(self.lat_min+lat*width,self.lng_min+lng*width, self.lat_max+lat*width,self.lng_max+lng*width)
class QuadTree:
	#Searches are faster with low max_points and insertions are faster with high max_points.
	def __init__(self, max_points, *rectangle):
		self.points = []
		self.children = []
		self.rect = Rectangle(*rectangle)
		self.max_points = max_points
	def addPoint(self, point):
		if self.rect.contains(point):
			if len(self.children)>0:
				for child in self.children:
					if child.contains(point):
						child.addPoint(point)
						break
			else:
				self.points.append(point)
				if len(self.points)>self.max_points:
					self.__divide()
		else:
			self.__extend()
			self.addPoint(point)
	def contains(self, point):
		return self.rect.contains(point)
	def closestNeighbor(self, point):
		if len(children)>0:
			closest = None
			for child in children:
				if child.contains(point):
					closest = child.closestNeighbor(point)
					break
			for child in children:
				if closest is None or distance(child.rect, point)<distance(closest, point):
					candidate = child.closestNeighbor(point)
					if closest is None or distance(point, cantdidate)<distance(point,closest):
						closest = candidate

		else:
			if len(points)>0:
				closest = self.points[0]
				for neighbor in self.points[1:]:
					if distance(neighbor,point)<distance(point,closest):
						closest = neighbor
				return closest
			else:
				return None
	def __divide(self):
		childrects = self.rect.split()
		for rect in childrects:
			self.children.append(QuadTree(self.max_points, rect))
		for point in points:
			for child in children:
				if child.contains(point):
					child.append(point)
					break
		self.points = []
	def __extend(self):
		rectangles = [self.rect.translate(-0.5((i/2)%2), -0.5+(i%2)) for i in xrange(4)]
		newQTs = [QuadTree(self.max_points, rect) for rect in rectangles]
		if len(children)>0:
			for i in xrange(4):
				newQTs[i].children = [[],[],[],[]]
				newQts[i].children[-i] = self.children[i]
			#new.points = self.points
		else:
			for old_point in self.points:
				for qt in newQTs:
					if qt.contains(old_point):
						qt.addPoint(old_point)
			self.points=[]
		self.children = newQTs
						


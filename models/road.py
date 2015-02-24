from util import dbc
class RoadSegment:
	def __init__(self, roadPointA, roadPointB, status, id=None):
		self.pointA=roadPointA
		self.pointB=roadPointB
		self.status=status
		if id is None:
			self.id=dbc.addSegment(roadPointA, roadPointB, self.status)
		else:
			self.id=id
	def update(self, status):
		self.status = status
		dbc.updateSegment(self, self.status)
	def toDict(self):
		return {'status':self.status, 'pointA':self.pointA, 'pointB':self.pointB}

class RoadPoint:
	def __init__(self, lat, lng, id=None):
		self.lat=lat
		self.lng=lng
		self.segments=[]
		if id is None:
			self.id = dbc.addPoint(self.lat,self.lng)
		else:
			self.id=id
	def toDict(self):
		return {'lng':self.lng, 'lat':self.lat}


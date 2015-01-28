class RoadSegment:
	def __init__(self, roadpointA, roadpointB):
		self.pointA=roadpointA
		self.pointB=roadpointB
	def toDict(self):
		return {'pointA':self.pointA, 'pointB':self.pointB}

class RoadPoint:
	def __init__(self, lat, lng, status):
		self.status=status
		self.lat=lat
		self.lng=lng
	def update(self, status):
		self.status = status
	def toDict(self):
		return {'status':self.status, 'lng':self.lng, 'lat':self.lat}



class RoadSegment:
	def __init__(self, roadpointA, roadpointB, status):
		self.pointA=roadpointA
		self.pointB=roadpointB
		self.status=status
	def update(self, status):
		self.status = status
	def toDict(self):
		return {'status':self.status, 'pointA':self.pointA, 'pointB':self.pointB}

class RoadPoint:
	def __init__(self, lat, lng):
		self.lat=lat
		self.lng=lng
	def toDict(self):
		return {'lng':self.lng, 'lat':self.lat}


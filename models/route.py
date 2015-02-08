from util import dbc
class Route:
	def __init__(self, name,id=None):
		self.name=name
		self.segments=[]
		if id is None:
			self.id=dbc.addRoute(name)
		else:
			self.id=id
	def addSegment(self, segment, new):
		self.segments.append(segment)
		if new:
			dbc.addSegmentToRoute(self, segment)
	def toDict(self):
		return {'segments':self.segments, 'name':self.name}

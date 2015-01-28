
class Route:
	def __init__(self, segments, name):
		self.segments=segments
		self.name=name
	def addSegment(self, segment):
		self.segments.append(segment)
	def toDict(self):
		return {'segments':self.segments, 'name':self.name}


class Route:
	def __init__(self, name, segments):
		self.name=name
		self.segments=segments
	def addSegment(self, segment):
		self.segments.append(segment)
	def toDict(self):
		return {'segments':self.segments, 'name':self.name}

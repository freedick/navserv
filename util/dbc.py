import MySQLdb

class DBC:
	def __init__(self, host, username, password, dbname):
		self.db = MySQLdb.connect(
			host="130.240.5.34",
			user=username,
			passwd=password,
			db=dbname)
	def query(self, query):
		cur = self.db.cursor() 
		cur.execute(query)
		return cur.fetchall(



	def addPoint(self,lat,lon):
		return self.query("INSERT INTO RoadPoints (Lat, Lon) VALUES (lat, lon)")

	def addSegment(self,pointa,pointb):
		temppointa = self.addPoint(pointa.Lat,pointa.Lon)
		temppontb = self.addpoint(pointb.Lat,pointb.Lon)
		return self.query("INSERT INTO RoadSegments (PointA, PointB, Status) VALUES (temppointa.ID, temppointb.ID, 0)")


	def addSegmentToRoute(self,routeid, segmentid):
		return self.query("INSERT INTO RouteSegments (RouteID,RoadSegemntID) VALUES (routeid, segmentid)")


	def addRoute(self,name):
		return self.query("INSERT INTO Routes (Name, Version) VALUES (name, 0)")
		

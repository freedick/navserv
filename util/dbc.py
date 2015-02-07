import MySQLdb
__DATABASE__ = None

def connect(host, username, password, dbname):
	global __DATABASE__
	__DATABASE__ = MySQLdb.connect(
		host=host,
		user=username,
		passwd=password,
		db=dbname)

def query(query):
	global __DATABASE__
	if query[-1] != ";":
		query=query+";"
	cur = __DATABASE__.cursor() 
	cur.execute(query)
	return cur.fetchall()

def addPoint(lat,lon):
	return query("INSERT INTO RoadPoints (Lat, Lon) VALUES (lat, lon)")

def addSegment(pointa,pointb):
	return query("INSERT INTO RoadSegments (PointA, PointB, Status) VALUES (%d, %d, 0)" % (pointa.id,pointb.id))

def addSegmentToRoute(routeid, segmentid):
	return query("INSERT INTO RouteSegments (RouteID,RoadSegemntID) VALUES (routeid, segmentid)")

def addRoute(name):
	return query("INSERT INTO Routes (Name, Version) VALUES (name, 0)")


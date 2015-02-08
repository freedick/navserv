import MySQLdb
__DATABASE__ = None

def connect(host, username, password, dbname):
	global __DATABASE__
	__DATABASE__ = MySQLdb.connect(
		host=host,
		user=username,
		passwd=password,
		db=dbname)

def query(query, commit=True):
	global __DATABASE__
	if query[-1] != ";":
		query=query+";"
	cur = __DATABASE__.cursor() 
	cur.execute(query)
	if commit:
		__DATABASE__.commit()
	#result = cur.fetchall()
	#cur.close()
	#return result
	return cur

def addPoint(lat,lng):
	cur = query("INSERT INTO RoadPoints (Lat, Lon) VALUES (%f, %f)"%(lat, lng))
	point_id = cur.lastrowid
	cur.close()
	return point_id

def addSegment(pointa,pointb,status):
	cur = query("INSERT INTO RoadSegments (PointA, PointB, Status) VALUES (%d, %d, %d)" % (pointa.id, pointb.id, status))
	segment_id = cur.lastrowid
	cur.close()
	return segment_id
def addSegmentToRoute(route, segment):
	cur = query("INSERT INTO RouteSegments (RouteID,RoadSegmentID) VALUES (%d, %d)" % (route.id, segment.id))
	route_segment_id = cur.lastrowid
	cur.close()
	return route_segment_id

def addRoute(name):
	cur = query("INSERT INTO Routes (Name, Version) VALUES ('%s', 0)" % (name.replace("'","\\'")))
	route_id = cur.lastrowid
	cur.close()
	return route_id
def updateSegment(segment):
	cur = query("UPDATE RoadSegments SET (Status=%d) WHERE id=% WHERE id=%d"%(segment.status,segment.id))
	cur.close()


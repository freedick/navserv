import MySQLdb
__DATABASE__ = None

#Connect to database 
def connect(host, username, password, dbname):
	global __DATABASE__
	__DATABASE__ = MySQLdb.connect(
		host=host,
		user=username,
		passwd=password,
		db=dbname)
#Query to the connected database
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
	
#Create a point in the database that has the cords lat and lng
def addPoint(lat,lng):
	cur = query("INSERT INTO RoadPoints (Lat, Lon) VALUES (%f, %f)"%(lat, lng))
	point_id = cur.lastrowid
	cur.close()
	return point_id
	
#Create a segment in the database that goes bettwen two points (pointa and pointb)
def addSegment(pointa,pointb,status):
	cur = query("INSERT INTO RoadSegments (PointA, PointB, Status) VALUES (%d, %d, %d)" % (pointa.id, pointb.id, status))
	segment_id = cur.lastrowid
	cur.close()
	return segment_id
	
#Add a segment to a route in the database
def addSegmentToRoute(route, segment):
	cur = query("INSERT INTO RouteSegments (RouteID,RoadSegmentID) VALUES (%d, %d)" % (route.id, segment.id))
	route_segment_id = cur.lastrowid
	cur.close()
	return route_segment_id

#Create a route in the database
def addRoute(name):
	cur = query("INSERT INTO Routes (Name, Version) VALUES ('%s', 0)" % (name.replace("'","\\'")))
	route_id = cur.lastrowid
	cur.close()
	return route_id

#Change the status of a segment in the database
def updateSegment(segment):
	cur = query("UPDATE RoadSegments SET (Status=%d) WHERE id=% WHERE id=%d"%(segment.status,segment.id))
	cur.close()

#Get all segments in the database
def getSegments():
	cur = query("SELECT * FROM RoadSegments")
	result = cur.fetchall()
	cur.close()
	return result

#Get all points in the database
def getPoints():
	cur = query("SELECT * FROM RoadPoints")
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all routesegments in the database
def getRouteSegments():
	cur = query("SELECT * FROM RouteSegments")
	result = cur.fetchall()
	cur.close()
	return result
#Get all routes in the database
def getRoutes():
	cur = query("SELECT * FROM Routes")
	result = cur.fetchall()
	cur.close()
	return result

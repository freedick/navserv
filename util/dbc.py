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
	cur = query("UPDATE RoadSegments SET (Status=%d) WHERE id=%d"%(segment.status,segment.id))
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

#Create a car in the database
def addCar(carid,typevalue):
	cur = query("INSERT INTO Cars (ID, Status, Type) VALUES (%d, 0, %d)" % (carid,typevalue))
	car_id = cur.lastrowid
	cur.close()
	return car_id
	
#Create a assignment in the database	
def addAssignment(carid,typevalue):
	cur = query("INSERT INTO Assignments (CarID, Type, 0) VALUES (%d, %d)" % (carid, typevalue))
	assignment_id = cur.lastrowid
	cur.close()
	return assignment_id
	
#Add a segment to an assignment
def addAssignmentSegment(assid,segid):
	cur = query("INSERT INTO AssignmentSegments (AssignmentID, SegmentID) VALUES (%d, %d)" % (assid, segid))
	assignmentsegment_id = cur.lastrowid
	cur.close()
	return assignmentsegment_id

#Change the status of a car in the database
def changeCarStatus(carid,status):
	cur = query("UPDATE Cars SET (Status=%d) WHERE id=%d"%(status,carid))
	cur.close()
	
#Change the type of a car in the database
def changeCarType(carid,typevalue):
	cur = query("UPDATE Cars SET (Type=%d) WHERE id=%d"%(typevalue,carid))
	cur.close()

#Change the status of a assignment in the database
def changeAssignmentStatus(assid,status):
	cur = query("UPDATE Assignments SET (Status=%d) WHERE id=%d"%(status,assid))
	cur.close()

#Assign a assignment to a car int the database
def assignAssingmentToCar(assid,carid):
	cur = query("UPDATE Assignments SET (CarID=%d) WHERE id=%d"%(carid,assid))
	cur.close()

#Get all car that have the type (typevalue)
def getCarsOnType(typevalue):
	cur = query("SELECT * FROM Cars WHERE Type = %d"%(typevalue))
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all car that have the status (status)
def getCarsOnStatus(status):
	cur = query("SELECT * FROM Cars WHERE Status = %d"%(status))
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all cars 
def getCars():
	cur = query("SELECT * FROM Cars)
	result = cur.fetchall()
	cur.close()
	return result

#Get all assignments that have the type (typevalue)
def getAssignmentsOnType(typevalue):
	cur = query("SELECT * FROM Assignments WHERE Type = %d"%(typevalue))
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all assignments that have the status (status)
def getAssignmentsOnStatus(status):
	cur = query("SELECT * FROM Assignments WHERE Status = %d"%(status))
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all assignments
def getAssignmentsOnStatus():
	cur = query("SELECT * FROM Assignments )
	result = cur.fetchall()
	cur.close()
	return result
	
#Get all segemnts for a assignment
def getAssignmentsSegments(assid):
	cur = query("SELECT * FROM AssignmentSegments WHERE AssignmentID = %d"%(assid))
	result = cur.fetchall()
	cur.close()
	return result

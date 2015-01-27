#!/usr/bin/env python
import web
import json
import urllib, httplib2
import MySQLdb

class DB:
	db = MySQLdb.connect(host="130.240.5.34", # your host, usually localhost
                     user="root", # your username
                      passwd="", # your password
                      db="Navigator")
                      
	cur = db.cursor() 
	cur.execute("SELECT * FROM YOUR_TABLE_NAME")
	for row in cur.fetchall() :
    		print row[0]

class RouteEncoder(json.JSONEncoder):
	def default(self, obj):
		dict = obj.toDict()
		return dict

class Route:
	def __init__(self, segments, name):
		self.segments=segments
		self.name=name
	def addSegment(self, segment):
		self.segments.append(segment)
	def toDict(self):
		return {'segments':self.segments, 'name':self.name}

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


class index:
	def GET(self):
		output = '<html><body><p>Navserv is up and running.</p>'
		output += '<form method="POST" action="points/1">'
		output += '<p>status: <input type="text" name="status"/></p>'
		output += '<input type="submit"/>'
		output += '</form>'
		output += '</body></html>'
		return output

class list_routes:
	def GET(self):
		output = json.dumps(routes, cls=RouteEncoder)
		return output

class get_route:
	def GET(self, route_id):
		output = json.dumps(routes[int(route_id)], cls=RouteEncoder)
		return output

class point_handler:
	def GET(self, point_id):
		output = json.dumps(points[int(point_id)], cls=RouteEncoder)
		return output
	def POST(self, point_id):
		point_id=int(point_id)
		status = web.input('status')
		if point_id < len(points):
			print "aoeu"
			points[point_id].update(status)
			return "success"
		return "error"

class google_test:
	def GET(self):
		googleurl = "http://maps.googleapis.com/maps/api/directions/json"
		input = web.input('origin','destination')
		origin = input['origin']
		destination = input['destination']
		print origin, destination
		data = urllib.urlencode({'origin':origin,'destination':destination})

		h = httplib2.Http(".cache")
		resp, content = h.request(googleurl+"?"+data,"GET")
		print content[0:50]
		directions = json.loads(content)
		#Do something here?
		output = json.dumps({"directions":directions})
		return output

routes = []
points = [RoadPoint(1.0,1.0,"ok"),RoadPoint(1.1,1.1,"ok"),RoadPoint(1.2,1.4,"slippery"),RoadPoint(1.4,1.0,"slippery"),RoadPoint(1.1,1.0,"sanded")]
segments = [RoadSegment(points[0],points[1]),RoadSegment(points[0],points[4]),RoadSegment(points[1],points[2]),RoadSegment(points[1],points[4]),RoadSegment(points[2],points[3]),RoadSegment(points[4],points[3])]
routesegments=[segments[0],segments[2],segments[4]]
routes.append(Route(routesegments,"herts via centrum"))
routesegments=[segments[0],segments[1],segments[5]]
routes.append(Route(routesegments,"centrum via herts"))

#print routes[0].__dict__
urls = (
	'/'			,index,
	'/routes/?'		,list_routes,	#matches '/routes' and '/routes/'
	'/routes/([0-9]+)'	,get_route,
	'/points/([0-9]+)'	,point_handler,
	'/google/'		,google_test,
	'/report/'		,DB,
)

app = web.application(urls, {'routes':routes,'points':points})

if __name__ == "__main__":
	app.run()

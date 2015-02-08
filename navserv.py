#!/usr/bin/env python

#Import required libraries
import web
import json
import urllib, httplib2

#Import essential datamodelsures and custom made API's
import util
from models.road import RoadSegment, RoadPoint
from models.route import Route
import settings

#TODO: move theese and import them instead

#Connect to the database
util.dbc.connect(settings.MYSQL_HOST,settings.MYSQL_USERNAME,settings.MYSQL_PASSWORD, settings.MYSQL_DBNAME)



#Test data
"""routes = []
points = [RoadPoint(1.0,1.0),RoadPoint(1.1,1.1),RoadPoint(1.2,1.4),RoadPoint(1.4,1.0),RoadPoint(1.1,1.0)]
segments = [RoadSegment(points[0],points[1],1),RoadSegment(points[0],points[4],2),RoadSegment(points[1],points[2],1),RoadSegment(points[1],points[4],2),RoadSegment(points[2],points[3],1),RoadSegment(points[4],points[3],3)]
routesegments=[segments[0],segments[2],segments[4]]
routes.append(Route("herts via centrum",routesegments))
routesegments=[segments[0],segments[1],segments[5]]
routes.append(Route("centrum via herts",routesegments))"""
pointlist = util.dbc.getPoints()
points = {}
for point in pointlist:
	point_id = point[0]
	point_lat = point[1]
	point_lng = point[2]
	points[point_id] = RoadPoint(point_lat, point_lng, point_id)
segmentlist = util.dbc.getSegments()
segments = {}
for segment in segmentlist:
	segment_id = segment[0]
	pointa = points[segment[1]]
	pointb = points[segment[2]]
	status = segment[3]
	segments[segment_id] = RoadSegment(pointa, pointb, status, segment_id)
routelist = util.dbc.getRoutes()
routes = {}
for route in routelist:
	route_id = route[0]
	name = route[1]
	routes[route_id] = Route(name, route_id)
routesegmentslist = util.dbc.getRouteSegments()
for routesegment in routesegmentslist:
	route_id = routesegment[1]
	segment_id = routesegment[2]
	routes[route_id].addSegment(segments[segment_id],False)

class NavigatorApplication(web.application):
    def run(self, port=80, *middleware):
        func = self.wsgifunc(*middleware)
        return web.httpserver.runsimple(func, ('0.0.0.0', port))

def loadState(handler):
	#These will be available as global variables within web.py classes. It should contain the datamodelsures required for full functionality.
	#Remember to mutex these when altered, maybe write exclusive and read exclusive locks for performance.
	web.ctx.routes = routes
	web.ctx.segments = segments
	web.ctx.points = points
	return handler()

#Import all services
from services.route import list_routes, get_route
from services.main import index
from services.point import *
from services.google import google_test
from services.report import RequestHandler

#Bind urls to services 
#TODO: make recursive url decoding, so that each service decides which suburl decodes to what.
#TODO: move these to a settings.py file.
urls = (
	'/'			,'index',
	'/routes/?'		,'list_routes',	#matches '/routes' and '/routes/'
	'/routes/([0-9]+)'	,'get_route',
	'/points/([0-9]+)'	,'point_handler',
	'/google/'		,'google_test',
	'/report/'		,'RequestHandler',
)

if __name__ == "__main__":
	app = NavigatorApplication(urls, globals())
	app.add_processor(loadState)
	app.run(port=settings.PORT)


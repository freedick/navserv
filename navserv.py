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



#Test data
routes = []
points = [RoadPoint(1.0,1.0),RoadPoint(1.1,1.1),RoadPoint(1.2,1.4),RoadPoint(1.4,1.0),RoadPoint(1.1,1.0)]
segments = [RoadSegment(points[0],points[1],"ok"),RoadSegment(points[0],points[4],"slippery"),RoadSegment(points[1],points[2],"ok"),RoadSegment(points[1],points[4],"slippery"),RoadSegment(points[2],points[3],"ok"),RoadSegment(points[4],points[3],"snowy")]
routesegments=[segments[0],segments[2],segments[4]]
routes.append(Route("herts via centrum",routesegments))
routesegments=[segments[0],segments[1],segments[5]]
routes.append(Route("centrum via herts",routesegments))

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

#Bind urls to services 
#TODO: make recursive url decoding, so that each service decides which suburl decodes to what.
#TODO: move these to a settings.py file.
urls = (
	'/'			,'index',
	'/routes/?'		,'list_routes',	#matches '/routes' and '/routes/'
	'/routes/([0-9]+)'	,'get_route',
	'/points/([0-9]+)'	,'point_handler',
	'/google/'		,'google_test',
)

if __name__ == "__main__":
	app = NavigatorApplication(urls, globals())
	app.add_processor(loadState)
	app.run(port=settings.PORT)


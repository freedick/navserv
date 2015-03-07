import settings
import re
import web,json
from util.encoder import RouteEncoder
import util.polyline
import models.route
import models.road
class admin_index:
	def GET(self):
		template_file = open('services/html/map.html', 'r')
		template = template_file.read()
		matches = re.findall("\{\{(.+?)\}\}", template)
		output = template
		for match in matches:
			output = output.replace("{{%s}}"%(match), eval(match))
			output += "<pre>['%s','%s']</pre>"%("{{%s}}"%(match), eval(match))
		return output
class admin_route:
	def POST(self):
		#Load global states
		routes=web.ctx.routes
		points=web.ctx.points
		point_quadtree=web.ctx.point_quadtree
		#Load post data
		post_data= web.input()
		route_name = str(post_data['route_name'])
		polyline = str(post_data['polyline'])
		#Create route
		route = models.route.Route(route_name)
		#Convert polyline to point list
		point_list=util.polyline.decode(polyline)
		filtered_list = []
		last_point=None
		last_existed=False
		for point in point_list:
			temp_point=models.road.RoadPoint(point[1], point[0], -1)
			closest = point_quadtree.closestNeighbor(temp_point)
			if closest is not None and util.quadtree.distance(closest,temp_point)<0.00005:#This constant will vary depending on latitudal location.
				filtered_list.append(closest)
			else:
				new_point = models.road.RoadPoint(point[1], point[0])#Create a permanent point(no id adds to database
				filtered_list.append(new_point)
				points[new_point.id] = new_point#Add it to the list of points
				point_quadtree.addPoint(new_point)#Insert the point into the quadtree
		for i in xrange(len(filtered_list)-1):
			point_from = filtered_list[i]
			point_to = filtered_list[i+1]
			segment_between=None
			if len(point_to.segments)>0:
				for segment in point_from.segments:
					if segment.pointA==point_to or segment.pointB==point_to:
						segment_between=segment
						break
			if segment_between is None:
				segment_between = models.road.RoadSegment(point_from, point_to, 0)
			route.addSegment(segment_between, True)
			routes[route.id]=route
		return "Success: %s" % route			
		#if route_id in routes:
		#	del routes['route_id']
		#if route_id in routes:
		#	return "Route exists"
		#else:
		#	return util.polyline.decode(polyline)

import json,web
import util.polyline
import util.encoder
import urllib, httplib2
from models.road import RoadPoint, RoadSegment
from models.route import Route
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
		#Load response
		directions = json.loads(content)
		routes = directions['routes']
		coordinates = []
		#Decode polyline encoded routes
		for route in routes:
			polyline_str = route["overview_polyline"]["points"]
			coordinates.extend(util.polyline.decode(polyline_str))
		points = [RoadPoint(*coordinates[0])]
		segments = []
		for coordinate in coordinates[1:]:
			points.append(RoadPoint(*coordinate))
			segments.append(RoadSegment(points[-2],points[-1],"null"))
		route = Route("googleRoute", segments)
		#TODO: Save to database
		#Return response
		output = json.dumps(route, cls=util.encoder.RouteEncoder)#{"directions":directions})
		return output

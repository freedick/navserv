import json,web
import util.polyline
import urllib, httplib2
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
		#TODO: Save to database
		#Return response
		output = json.dumps(coordinates)#{"directions":directions})
		return output

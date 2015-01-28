import json,web
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

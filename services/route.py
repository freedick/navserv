import json, web
from util.encoder import RouteEncoder
class list_routes:
	def GET(self):
		output = json.dumps(web.ctx.routes, cls=RouteEncoder)
		return output

class get_route:
	def GET(self, route_id):
		output = json.dumps(web.ctx.routes[int(route_id)], cls=RouteEncoder)
		return output

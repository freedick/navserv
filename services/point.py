import json, web
from util.encoder import RouteEncoder
class point_handler:
	def GET(self, point_id):
		output = json.dumps(points[int(point_id)], cls=RouteEncoder)
		return output
	def POST(self, point_id):
		points=web.ctx.points
		point_id=int(point_id)
		status = web.input('status')
		if point_id < len(points):
			print "aoeu"
			points[point_id].update(status)
			return "success"
		return "error"

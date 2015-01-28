import json
class RouteEncoder(json.JSONEncoder):
	def default(self, obj):
		dict = obj.toDict()
		return dict

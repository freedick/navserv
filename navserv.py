#!/usr/bin/env python
import web

class index:
	def GET(self):
		output = 'Navserv is up and running'
		return output

class list_routes:
	def GET(self):
		output = 'Not yet implemented.'
		return output

class get_route:
	def GET(self, route_id):
		output = 'Not yet implemented. route_id=%d.'%int(route_id)
		return output

urls = (
	'/'			,index,
	'/routes/?'		,list_routes,	#matches '/routes' and '/routes/'
	'/routes/([0-9]+)'	,get_route,
)

app = web.application(urls, globals())

if __name__ == "__main__":
	app.run()

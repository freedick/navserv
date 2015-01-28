class index:
	def GET(self):
		output = '<html><body><p>Navserv is up and running.</p>'
		output += '<form method="POST" action="points/1">'
		output += '<p>status: <input type="text" name="status"/></p>'
		output += '<input type="submit"/>'
		output += '</form>'
		output += '</body></html>'
		return output

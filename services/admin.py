import settings
import re
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

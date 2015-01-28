import MySQLdb

class DBC:
	def __init__(self, host, username, password, dbname):
		self.db = MySQLdb.connect(
			host="130.240.5.34",
			user=username,
			passwd=password,
			db=dbname)
	def query(self, query):
		cur = self.db.cursor() 
		cur.execute(query)
		return cur.fetchall()

#Installation (using easy_install)
##easy_install
	sudo apt-get install python-setuptools
##web.py
	sudo easy_install web.py
##httplib2
	sudo easy_install httplib2
##MySQLdb
	sudo apt-get install python-mysqldb
#Configuration
##settings.py.sample
	cp settings.py.sample settings.py
Fill in the approporiate settings and save the file. settings.py is ignored by git.
#Running the server
To run the server either make sure it has the execute flag and run this command.
	./navserv.py
You can also invoke the python interpreter directly.
	python navserv.py
To check that the server is working you can enter the ip, at which it is hosted and the port specified in the settings file in the url bar of your webbrowser. For example:
http://130.240.5.34:8080/
#Running tests
To run the tests defined you can invoke 
	python test.py
from a terminal.

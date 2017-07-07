REQUIREMENT :
	- Python 3.5
	- Flask 

INSTRUCTION TO RUN :
	- Download Python 3.5 on your system or download any Python ide like spyder or pycharm.
	- Install Flask by using "pip command" as pip install flask
	- Run task.py in your ide or cmd as python task.py.
	- There are two tasks in the code with id as 1 and 2.
	-1st task :
		- Use your browser to run it as shown:
		- http://127.0.0.1:5000/api/request?connid=1&&timeout=80
	-2nd task :
		-Use your browser or curl command to run it as shown
		-Browser : http://127.0.0.1:5000/api/serverstatus
		-curl : curl -i http://127.0.0.1:5000/api/serverstatus
	- 3rd task :
		- Use curl command to run this as api as shown:
		- curl -i -H "Content-Type: application/json" -X PUT -d "{\"connid\":2}" http://localhost:5000/api/kill 
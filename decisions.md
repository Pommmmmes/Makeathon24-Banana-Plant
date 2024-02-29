# All the Project decisions

## Backend

skunert:
 - in ./server/main.py FFlask server on localhost (127.0.0.1) and port 8080 it responds to index file with route ('/', GET) and with route ('/recieve', POST)

 - route ('/', GET) gives you the file in ./server/templates/hello.html which displays I squared for testing

 - route ('/recieve', POST) does the simplest json convertion and returns the time of the json file if it exists otherwise it prints an error to the screen

- venv directory created which is needed by the flask framework to store the virtual environment

- .gitignore file created to ignore the venv directory so it doesnt get pushed


fbock:
- added a database file on the route ./server/measurements.db

- added databae files coded with the sqlite3 library on route ./server/sqlite_utils.py and contains three functions:
		- initialize the database: def initialize_db():
		- add data to the database:  def add_row(uuid: str, id: str, timestamp: int , temp: int,
            							humidity: int, red: int, green: int, blue: int):
		- delete a row in the databse: def delete_row(row_uuid):
- two more function are added in the sqlite_utils.py are commented out because they are not finished

- these function are not used yet but are implemented to be used later on

njantsch:
- added function for calculating ripeness in percentage

- added matplotlib diagram creation for moisture of last 7 days

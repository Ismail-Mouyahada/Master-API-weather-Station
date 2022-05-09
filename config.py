from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'TEAM'
app.config['MYSQL_DATABASE_PASSWORD'] = 'CESI-2022'
app.config['MYSQL_DATABASE_DB'] = 'database_meteo'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)
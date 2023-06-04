#Importar el conector de Python con Mysql.
import  mysql.connector as db

#Con el conector importado creamos un objeto de conexion.
mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "InfoAeropuertos"
)

#Con la conexion creamos un objeto cursor.
my_cursor = mydb.cursor()

#Creamos una sentencia SQL asociado a una variable.
sqlsentense = " SELECT * FROM InfoAeropuertos.aeropuertos ;"

#Invocamos con execute sobre el objeto cursor, la sentencia SQL que aplicaremos a la base de datos.
my_cursor.execute(sqlsentense)

for x in my_cursor:

    registro = my_cursor.fetchone()

    print (registro)


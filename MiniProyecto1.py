import  mysql.connector as db

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "InfoAeropuertos"
)

cursor = mydb.cursor()


SQLCrear_Registro = 'INSERT INTO aeropuertos (id, ident, type, name, elevation_ft, municipality, iata_code, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

registros = [ 
    (39340, 'SHCC', 'heliport', 'Clinica Las Condes Heliport', 2461, 'Santiago', , 25),
    (39379, 'SHMA', 'heliport', 'Clinica Santa Maria Heliport', 2028, 'Santiago', , 25),
    (39390, 'SHPT', 'heliport', 'Portillo Heliport', 9000, 'Los Andes', , 25)
]
cursor.executemany(SQLCrear_Registro, registros)
mydb.commit()
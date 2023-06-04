import mysql.connector as db
import mysql

mydb = db.connect(
    host = "localhost",
    user = "root",
    passwd = "mysql123",
    database = "InfoAeropuertos"
)

def insertar_registro_DB():
    cursor = mydb.cursor()
    SQLCrear_Registro = 'INSERT INTO aeropuertos (id, ident, type, name, elevation_ft, municipality, iata_code, score) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)'

    registros = [ 
        (39340, 'SHCC', 'heliport', 'Clinica Las Condes Heliport', 2461, 'Santiago','',25),
        (39379, 'SHMA', 'heliport', 'Clinica Santa Maria Heliport', 2028, 'Santiago','',25),
        (39390, 'SHPT', 'heliport', 'Portillo Heliport', 9000, 'Los Andes','',25)
    ]
    cursor.executemany(SQLCrear_Registro, registros)
    mydb.commit()
    print("\n=> Registro ingresado correctamente en la Base de Datos.\n")

def consultarDB():
    print("\nLos Aeropuertos situados a más de 5000 pies de altura son:\n")
    print("  ---------------------------------------------------------------------------------------------")
    cursor = mydb.cursor()
    SQL_Consulta = 'SELECT name, type, municipality, elevation_ft FROM aeropuertos WHERE elevation_ft > 5000'
    cursor.execute(SQL_Consulta)
    rows = cursor.fetchall()
    print("  | {:<32} | {:<18} | {:<22} | {:<8} |".format('Nombre','Tipo','Municipalidad','Altura'))
    print("  ---------------------------------------------------------------------------------------------")
    for row in rows:
        print("  | {:<32} | {:<18} | {:<22} | {:<8} |".format( row[0], row[1], row[2], row[3]))
    
    print("  ---------------------------------------------------------------------------------------------")


def solicitar_accion():
    print("Ingrese una opcion:\n") 
    print("=> [1] Agrega los tres aeropuertos")
    print("    ------------------------------------------------------------------------------------")
    print("    | 39340 | SHCC | heliport | Clinica Las Condes Heliport  | 2461 | Santiago  | | 25 |")
    print("    | 39379 | SHMA | heliport | Clinica Santa Maria Heliport | 2028 | Santiago  | | 25 |")
    print("    | 39390 | SHPT | heliport | Portillo Heliport            | 9000 | Los Andes | | 25 |")
    print("    ------------------------------------------------------------------------------------")
    print("\n=> [2] Consultar Aeropuertos situados a más de 5000 pies de altura")
    print("\n=> [0] Salir")
    
    seleccion = input("\nIndique su elección (0, 1, 2): ")
    while seleccion not in "012":
        seleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2): ")
    seleccion = int(seleccion)
    return seleccion

def main():
    
    try:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()
            if accion == 1:
                insertar_registro_DB()
                salir = True
            elif accion == 2:
                consultarDB()
                salir = True
            else:
                salir = True
                print("\n********** ¡Adiós! **********\n")

    except mysql.connector.IntegrityError as error:
            print("\n=> ID ya existe en DB, favor revisar datos a ingresar!\n")
    
        

if __name__ == "__main__":
    main()
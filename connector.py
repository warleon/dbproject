import psycopg2, generator as gen

DATABASE = "db1project"
SCHEMA1 = "db_project10_3"
SCHEMA2 = "db_project10_4"
SCHEMA3 = "db_project10_5"
SCHEMA4 = "db_project10_6"
# Query templates
INSERT = "insert into {} values ({})"
SELECT = "select {} from {} where {}"

def main():
    insertData(1000, SCHEMA1)
    # insertData(10000, SCHEMA2)
    # insertData(100000, SCHEMA3)
    # insertData(1000000, SCHEMA4)

def insertData(n , schema):
    # Connect to database
    conn = psycopg2.connect(database=DATABASE, options="-c search_path={}".format(schema))
    curr = conn.cursor()
    # Insert data
    insertUsuario(curr, n)
    insertServidor(curr, n)
    
    # Commit and close session
    conn.commit()
    curr.close()
    conn.close()

# Returns a string to format with n values
def valuesFormat(n):
    values = "'{}'"
    for i in range(n-1):
        values += ",'{}'"
    return values

def insertUsuario(curr, n):
    table = "usuario(nombre, is_jugador, is_comerciante, is_server_owner)"
    values = valuesFormat(4)
    for x in range(n):
        query = INSERT.format(table, values.format(gen.get_usuario(), gen.rand_bool(),
        gen.rand_bool(), gen.rand_bool()))
        curr.execute(query)

def insertServidor(curr, n):
    table = "servidor(nombre, usuario_nombre, ip, activo, idioma, locacion)"
    values = valuesFormat(6)
    curr.execute(SELECT.format('nombre', 'usuario', "is_server_owner='true'"))
    queryResult = curr.fetchall()
    # Add 0 to 5 servidores for each user that is a server-owner
    for row in queryResult:
        usuario = row[0]
        for i in range(gen.rand_num(n / 100)):
            curr.execute(INSERT.format(table, values.format(gen.get_nombre(),
            usuario, gen.get_ip(), gen.rand_bool(), gen.get_idioma(), gen.get_locacion())))

def insertSala(curr):
    table = "sala(servidor_nombre, codigo, enjuego)"
    values = valuesFormat(3)
    curr.execute(SELECT.format('nombre', 'servidor'))
    queryResult = curr.fetchall()
    # Add 0 to 10 salas for each servidor
    codigo = 1
    for row in queryResult:
        servidornombre = queryResult[0]
        for i in range(gen.rand_num(10)):
            # TODO remove jugadores from sala
            curr.execute(INSERT.format(table, values.format(servidornombre, codigo, gen.rand_bool())))
            codigo += 1


main()
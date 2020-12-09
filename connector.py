import psycopg2, generator as gen

DATABASE = "db1project"
SCHEMA = "db_project10_3"
# Query templates
INSERT = "insert into {} values ({})"
SELECT = "select {} from {} where {}"

def main():
    # Connect to database
    conn = psycopg2.connect(database=DATABASE, options="-c search_path={}".format(SCHEMA))
    curr = conn.cursor()
    n = 10

    # insertUsuario(curr, n)
    insertServidor(curr)
    
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

def insertServidor(curr):
    table = "servidor(nombre, usuario_nombre, ip, activo, idioma, locacion)"
    values = valuesFormat(6)
    curr.execute(SELECT.format('nombre', 'usuario', "is_server_owner='true'"))
    queryResult = curr.fetchall()
    # Add 0 to 5 servidores for each user that is a server-owner
    for row in queryResult:
        usuario = row[0]
        for i in range(gen.rand_num(5)):
            curr.execute(INSERT.format(table, values.format(gen.get_nombre(),
            usuario, gen.get_ip(), gen.rand_bool(), gen.get_idioma(), gen.get_locacion())))

def insertSala(curr):
    table = "sala(servidornombre, codigo, enjuego)"
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
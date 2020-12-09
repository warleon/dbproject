import psycopg2, generator as gen

DATABASE = "db1project"
SCHEMA = "db_project100"
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
    table = "usuario(nombre, tipo)"
    values = valuesFormat(2)
    for x in range(n):
        query = INSERT.format(table, values.format(gen.get_usuario(), gen.get_usuario_tipo()))
        curr.execute(query)

def insertServidor(curr):
    table = "servidor(nombre, usuarionombre, ip, activo, jugadores, flujo, idioma, locacion)"
    values = valuesFormat(8)
    # TODO get usuarios that are also hosts
    curr.execute(SELECT.format('*', 'usuario', "tipo='s'"))
    queryResult = curr.fetchall()
    for row in queryResult:
        usuario = row[0]
        for i in range(gen.rand_num(5)):
            curr.execute(INSERT.format(table, values.format(gen.get_nombre(),
            usuario, gen.get_ip(), gen.rand_bool(), gen.rand_num(10), gen.rand_num(10),
            gen.get_idioma(), gen.get_locacion())))


main()
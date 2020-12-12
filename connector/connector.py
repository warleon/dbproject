import psycopg2, generator as gen

DATABASE = "db1project"
SCHEMA1 = "db_project10_3"
SCHEMA2 = "db_project10_4"
SCHEMA3 = "db_project10_5"
SCHEMA4 = "db_project10_6"
# Query templates
INSERT = "insert into {} values ({})"
SELECT = "select {} from {} where {}"
SELECT2 = "select {} from {}"

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
    insertItem(curr, n)
    insertServidor(curr, n)
    insertSala(curr, n)
    insertPartida(curr, n)
    insertJuega(curr)
    insertPosee(curr)
    
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
    for x in range(n // 1000 * 2):
        curr.execute(INSERT.format(table, values.format(gen.get_nombre(30), gen.rand_bool(),
        gen.rand_bool(), 'true')))
    for x in range(n - (n // 1000 * 2)):
        curr.execute(INSERT.format(table, values.format(gen.get_nombre(30), gen.rand_bool(),
        gen.rand_bool(), 'false')))

def insertServidor(curr, n):
    table = "servidor(nombre, usuario_nombre, ip, activo, idioma, locacion)"
    values = valuesFormat(6)
    curr.execute(SELECT.format('nombre', 'usuario', "is_server_owner=true"))
    queryResult = curr.fetchall()
    # Add 2 servidores for each user that is a server-owner
    for row in queryResult:
        usuario = row[0]
        for i in range(gen.rand_num(4)): # avg 2
            curr.execute(INSERT.format(table, values.format(gen.get_nombre(35),
            usuario, gen.get_ip(), gen.rand_bool(), gen.get_idioma(), gen.get_locacion())))

def insertSala(curr, n):
    table = "sala(servidor_nombre, codigo, en_juego)"
    values = valuesFormat(3)
    curr.execute(SELECT2.format('nombre', 'servidor'))
    queryResult = curr.fetchall()
    # Add 0 to 20 salas for each servidor
    codigo = 1
    for row in queryResult:
        servidor_nombre = row[0]
        for i in range(gen.rand_num(20)): # avg 10
            curr.execute(INSERT.format(table, values.format(servidor_nombre, codigo, gen.rand_bool())))
            codigo += 1

def insertPartida(curr, n):
    table = "partida(codigo, servidor_nombre, sala_codigo, fecha, duracion, escenario_nombre)"
    values = valuesFormat(6)
    curr.execute(SELECT2.format('servidor_nombre, codigo', 'sala'))
    salas = curr.fetchall()
    curr.execute(SELECT.format('nombre', 'item', "tipo = 'Escenario'"))
    escenarios = [x[0] for x in curr.fetchall()]
    codigo = 1
    for row in salas:
        servidor_nombre = row[0]
        sala_codigo = row[1]
        for i in range(gen.rand_num(100)): # avg 50
            curr.execute(INSERT.format(table, values.format(codigo, servidor_nombre, sala_codigo, 
            gen.get_date(14), gen.get_time(), escenarios[gen.rand_num(len(escenarios) - 1)])))
            codigo += 1

def insertJuega(curr):
    table = "juega(usuario_nombre, partida_codigo)"
    values = valuesFormat(2)
    curr.execute(SELECT.format('nombre', 'usuario', "is_jugador=true"))
    usuarios = [x[0] for x in curr.fetchall()]
    curr.execute(SELECT2.format('codigo', 'partida'))
    partidas = [x[0] for x in curr.fetchall()]
    for usuario_nombre in usuarios:
        temp = partidas
        for x in range(gen.rand_num(len(partidas) // 100)):
            index = gen.rand_num(len(temp) - 1)
            curr.execute(INSERT.format(table, values.format(usuario_nombre, temp[index])))
            del temp[index]

def insertItem(curr, n):
    table = "item(nombre, limite_usos, descripcion, contrato, tipo, precio)"
    values = valuesFormat(6)
    for i in range(n // 10):
        curr.execute(INSERT.format(table, values.format(gen.get_nombre(40), gen.rand_num(100), gen.get_nombre(120), 
        gen.get_contract(), gen.get_item(), gen.rand_num(100))))

def insertPosee(curr):
    table = "posee(usuario_nombre, item_nombre)"
    values = valuesFormat(2)
    curr.execute(SELECT2.format('nombre', 'usuario'))
    usuarios = [x[0] for x in curr.fetchall()]
    curr.execute(SELECT2.format('nombre', 'item'))
    items = [x[0] for x in curr.fetchall()]
    for usuario_nombre in usuarios:
        for x in range(gen.rand_num(len(items) // 100)):
            temp = items
            # TODO check for item.limite_usos
            index = gen.rand_num(len(temp) - 1)
            curr.execute(INSERT.format(table, values.format(usuario_nombre, temp[index])))
            del temp[index]
    
main()
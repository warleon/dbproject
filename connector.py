import psycopg2, generator as gen, string

DATABASE = "bd1"
SCHEMA = "dbproject"
# Query templates
INSERT = "insert into {} values ({})"

# Sample dictionaries
usuario_tipos = ['j', 'c', 's']

def main():
    conn = psycopg2.connect(database=DATABASE, options="-c search_path={}".format(SCHEMA))
    curr = conn.cursor()

    insertUsuario(curr, 10)
    
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
        query = INSERT.format(table, values.format(gen.rand_str(string.ascii_letters, 30), gen.rand_str(usuario_tipos, 1)))
        curr.execute(query)


main()
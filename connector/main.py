from connector import insertData
from queries import queries
import time, psycopg2

DATABASE = "db1project"
SCHEMA1 = "db_project10_3"
SCHEMA2 = "db_project10_4"
SCHEMA3 = "db_project10_5"
SCHEMA4 = "db_project10_6"

def main():
    # generateData()
    testSchema(SCHEMA1)
    testSchema(SCHEMA2)
    testSchema(SCHEMA3)
    testSchema(SCHEMA4)

def generateData():
    insertData(1000, SCHEMA1)
    insertData(10000, SCHEMA2)
    insertData(100000, SCHEMA3)
    insertData(1000000, SCHEMA4)

def testSchema(schema):
    conn = psycopg2.connect(database=DATABASE, options="-c search_path={}".format(schema))
    curr = conn.cursor()
    print("Testing schema", schema)
    for i in range(len(queries)):
        print("Query", i+1, ':', testQuery(queries[i], curr), "ms")
    
    curr.close()
    conn.close()

def testQuery(query, curr):
    start = time.time()
    curr.execute(query)
    curr.fetchall()
    return round((time.time() - start) * 1000, 2)

main()
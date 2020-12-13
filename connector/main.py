from connector import insertData
from queries import queries
import time, psycopg2

DATABASE = "db1project"
SCHEMA1 = "db_project10_3_yes"
SCHEMA2 = "db_project10_4_yes"
SCHEMA3 = "db_project10_5_yes"
SCHEMA4 = "db_project10_6_yes"
SCHEMA5 = "db_project10_3_no"
SCHEMA6 = "db_project10_4_no"
SCHEMA7 = "db_project10_5_no"
SCHEMA8 = "db_project10_6_no"

schemas = [SCHEMA1,SCHEMA2,SCHEMA3,SCHEMA4,SCHEMA5,SCHEMA6,SCHEMA7,SCHEMA8]

def main():
    #generateData()
    for i in range(2,10):
        for schema in schemas:
            testSchema(schema)


def generateData():
    insertData(1000, SCHEMA1)
    insertData(10000, SCHEMA2)
    insertData(100000, SCHEMA3)
    insertData(1000000, SCHEMA4)
    #insertData(1000, SCHEMA5)
    #insertData(10000, SCHEMA6)
    #insertData(100000, SCHEMA7)
    #insertData(1000000, SCHEMA8)

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
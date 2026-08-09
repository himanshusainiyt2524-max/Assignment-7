import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="superengg3265",
    host="localhost",
    port="5433"
)


def table():
    cursor = conn.cursor()
    cursor.execute(""" create table employes (Name Text, ID int , Age int );""")
    print(" Table created succesfully")
    conn.commit()
    conn.close()


def data():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="superengg3265",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    cursor.execute(""" insert into employes (Name,ID,Age) values ('rudra',34,22);""")
    print(" data added succesfully")
    conn.commit()
    conn.close()


def extract():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="superengg3265",
        host="localhost",
        port="5433"
    )
    cursor = conn.cursor()
    cursor.execute(""" select * from employes;""")
    show=(cursor.fetchone())
    print(show[2])
    # print(" data added succesfully")
    conn.commit()
    conn.close()


data()
extract()

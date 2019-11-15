
import psycopg2

connection = psycopg2.connect(user = "postgres",
                                  password = "778KK@M8@",
                                  host = "127.0.0.1",
                                  port = "5433",
                                  database = "analysis")
cursor = connection.cursor()

cursor.execute("CREATE TABLE oko (id bigserial,first_name varchar(25),ty varchar(24));")

cursor.execute("SELECT * FROM oko")
import psycopg2

connection = psycopg2.connect(dbname="internshipdb", user="postgres",
                              password="mithukundu60@", host="localhost", port="5432")

print("connection established")

# creating cursor

cursor = connection.cursor()

# execution of query

# creating table

# cursor.execute("create table intern(id serial,name text,age int);")
# print("table created")

# inserting data

# query = "insert into intern(name,age) values('arnav',26);"

# cursor.execute(query)
# print("data inserted")

# fetch data

# query = "select * from intern;"
# cursor.execute(query)
# row = cursor.fetchall()
# print(row)

# cursor.execute(query)

# search a data

# query = "select * from intern where id=2;"
# cursor.execute(query)
# row = cursor.fetchall()
# print(row)

#  delete a data

query = "delete from intern where id=2"
cursor.execute(query)


connection.commit()
connection.close

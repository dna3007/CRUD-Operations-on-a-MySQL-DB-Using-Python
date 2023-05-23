import pymysql
conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password= "123456",
    db = "student"
)

myCursor = conn.cursor()

myCursor.execute("""create table names
    (
    id int primary key,
    name varchar(25),
    marks int
    )
    """)

conn.commit()
conn.close()
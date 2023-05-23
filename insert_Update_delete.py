import pymysql


conn = pymysql.connect(
    host="localhost",
    user="root",
    password="123456",
    db="student"
)

myCursor = conn.cursor()


def insert_record():
    id = int(input("Enter ID: "))
    name = input("Enter name: ")
    marks = int(input("Enter Marks: "))

    query = "insert into names (id,name,marks) values (%s,%s,%s)"
    myCursor.execute(query, (id, name, marks))
    conn.commit()
    print("Data Inserted Successfully!")


def update_record():
    id = int(input("Enter ID of the record to update: "))
    marks = int(input("Enter New Marks: "))

    query = "update names set marks = %s where id = %s"
    myCursor.execute(query, (marks, id))
    conn.commit()
    print("Data Inserted Successfully!")


def delete_record():
    id = int(input("Enter ID of the record to delete: "))

    query = "delete from names where id = %s"
    myCursor.execute(query, (id,))
    conn.commit()
    print("Data Inserted Successfully!")

def display_table():
    myCursor.execute("select * from names" )
    rows = myCursor.fetchall()
    print("\nid\tname\tmarks")

    for row in rows:
        print(f"{row[0]}\t{row[1]}\t{row[2]}")


display_table()
print("\n")

while True:
    print("1.insert record")
    print("2.update record")
    print("3.delete record")
    print("4.Display Table")
    print("5.Exit")

    choice = int(input("Enter your choice (1-4): "))
    if choice == 1:
        insert_record()
    elif choice == 2:
        update_record()
    elif choice == 3:
        delete_record()
    elif choice == 4:
        display_table()
    elif choice == 5:
        break
    else:
        print("invalid choice!")

myCursor.close()
conn.close()

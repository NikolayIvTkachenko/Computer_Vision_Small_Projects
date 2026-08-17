print("БАЗЫ ДАННЫХ ==========")
print("1 => =================")
# SELECT * FROM orders WHERE status = 'Shipped';
# SELECT * FROM orders;
# SELECT pono, date FROM orders;
# mysql -uroot
# /usr/local/mysql/bin/mysql - uroot -p
# ALTER USER 'root'@'localhost' IDENTIFIED BY 'your_new_pswd';
#
# CREATE DATABASE sampledb;
# USE sampledb;
#
# CREATE TABLE emps (empno INT NOT NULL, empname VARCHAR(50), job VARCHAR(30), PRIMARY KEY (empno));
# CREATE TABLE salary (empno INT NOT NULL, salary INT, PRIMARY KEY (empno));
# ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);
#
# CREATE TABLE orders (pono INT NOT NULL, empno INT NOT NULL, total INT, PRIMARY KEY (pono));
# ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);
# CREATE TABLE orders (pono INT NOT NULL, empno INT NOT NULL, total INT, PRIMARY KEY (pono), FOREIGN KEY (empno) REFERENCES (empno))
#
# db_science root toor
#
#
# ========================================================================================== ###
#

import mysql.connector


# Инициализируем переменные до try, чтобы они были видны в finally
cnx = None
cursor = None


try:
    cnx = mysql.connector.connect(user='root', password='toor', host='localhost', port=3316, database='db_science') #toortoor
    cursor = cnx.cursor()
    emps = [
        (9001, "Jeff Russell", "sales"),
        (9002, "Jeff Russell", "sales"),
        (9003, "Jeff Russell", "sales")
    ]
    query_add_emp = ("""INSERT INTO emps (empno, empname, job) VALUES (%s, %s, %s)""")

    for emp in emps:
        cursor.execute(query_add_emp, emp)
    salary = [
        (9001, 3000),
        (9002, 2800),
        (9003, 2500)
    ]

    query_add_salary = ("""INSERT INTO salary (empno, salary) VALUES (%s, %s)""")

    for sal in salary:
        cursor.execute(query_add_salary, sal)

    orders = [
        (2608, 9001, 35),
        (2617, 9001, 35),
        (2620, 9001, 139),
        (2621, 9002, 95),
        (2626, 9002, 218),
    ]

    query_add_order = ("""INSERT INTO orders(pono, empno, total) VALUES (%s, %s, %s)""")

    for order in orders:
        cursor.execute(query_add_order, order)

    cnx.commit()


except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
    # Если транзакция начала записываться, но упала на середине — откатываем
    if cnx and cnx.is_connected():
        cnx.rollback()

    print(f"Ошибка MySQL [{err.errno}]: {err.msg}")
finally:
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()
        print("Соединение с БД закрыто.")

#    cursor.close()
# NameError: name
# 'cursor' is not defined
# ==============================================================================================
# USE db_science;
# CREATE TABLE emps (empno INT NOT NULL, empname VARCHAR(50), job VARCHAR(30), PRIMARY KEY (empno));
# CREATE TABLE salary (empno INT NOT NULL, salary INT, PRIMARY KEY (empno));
# ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);
# CREATE TABLE orders (pono INT NOT NULL, empno INT NOT NULL, total INT, PRIMARY KEY (pono));
# ALTER TABLE salary ADD FOREIGN KEY (empno) REFERENCES emps (empno);


try:
    cnx = mysql.connector.connect(user='root', password='toor', host='localhost', port=3316, database='db_science')  # toortoor
    cursor = cnx.cursor()

    query = ("SELECT * FROM emps WHERE empno > %s")
    empno = 9001

    cursor.execute(query, (empno,))

    for (empno, empname, job) in cursor:
        print("{} {} {}".format(empno, empname, job))


except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
    # Если транзакция начала записываться, но упала на середине — откатываем
    if cnx and cnx.is_connected():
        cnx.rollback()

    print(f"Ошибка MySQL [{err.errno}]: {err.msg}")
finally:
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()
        print("Соединение с БД закрыто.")

try:
    cnx = mysql.connector.connect(user='root', password='toor', host='localhost', port=3316,
                                  database='db_science')  # toortoor
    cursor = cnx.cursor()

    query = ("""SELECT e.empno, e.empname, e.job, s.salary FROM emps e JOIN salary s ON e.empno = s.empno WHERE e.empno > %s""")
    empno = 9001

    cursor.execute(query, (empno,))

    for (empno, empname, job, salary) in cursor:
        print("{} {} {} {}".format(empno, empname, job, salary))


except mysql.connector.Error as err:
    print("Error-Code:", err.errno)
    print("Error-Message: {}".format(err.msg))
    # Если транзакция начала записываться, но упала на середине — откатываем
    if cnx and cnx.is_connected():
        cnx.rollback()

    print(f"Ошибка MySQL [{err.errno}]: {err.msg}")
finally:
    if cursor:
        cursor.close()
    if cnx and cnx.is_connected():
        cnx.close()
        print("Соединение с БД закрыто.")
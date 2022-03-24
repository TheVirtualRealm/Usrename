
from logging import getLogRecordFactory
from re import I
import sqlite3
from unittest import result
import sys
sqlite3.connect('login_information.db')
conn = sqlite3.connect('login_information.db')
cursor = conn.cursor()


print("Connected")

cursor.execute("""
CREATE TABLE IF NOT EXISTS userinfo (
    ID INTEGER PRIMARY KEY,
    "password" TEXT,
    "first_name" TEXT,
    "last_name" TEXT,
    "phone_number" TEXT,
    "user_name" TEXT
)""")

# print("Table Created")
# password = input('Password: \n')
# firstname = input('First Name: \n')
# lastname = input('Last Name: \n')
# phone = input('Phone Number: \n')
# username = input('Enter a username: \n')

cursor.execute("SELECT * FROM userinfo")
while True:
        row = cursor.fetchone()
        if row == None:
            break
        # print (row[5])

        userdata = str(row[5])

        print(userdata[0])

        

# password = 2
# firstname = ('george')
# lastname = ('george')
# phone = ('george')
# username = ('MrBean')

# cursor.execute("SELECT * FROM userinfo")
# cur_fetchall = cursor.fetchall()
# db_length = len(cur_fetchall)
# i = 0
# r = cursor.fetchone()
# print(r)
# print(db_length)
# while i < db_length:
#         r = cursor.fetchone()

#         print(r)

#         if r == username:
#                 print('Username already exists, please select a different username.')
#                 username = input('Please enter a new username: ') 
#                 break
#         else:
#             cursor.execute("""INSERT INTO userinfo(password, first_name, last_name, phone_number, user_name)
#             VALUES(?,?,?,?,?) 
#             """, (password, firstname, lastname, phone, username))
#         i+=1

# r = cursor.fetchone()
# print(r)

# r = cursor.fetchall()
# db_length = len(r)
# # print(r[2])
# # db_length = cursor.rowcount
# print(db_length)
# i = 0
# for item in r:
#     print(r[i])
#     i+=1

    

conn.commit()
conn.close()


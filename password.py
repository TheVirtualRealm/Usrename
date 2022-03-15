import sqlite3


sqlite3.connect('login_information.db')
conn = sqlite3.connect('login_information.db')
cursor = conn.cursor()

print("Connected")

cursor.execute("""
CREATE TABLE IF NOT EXISTS userinfo (
    "first_name" TEXT,
    "last_name" TEXT,
    "phone_number" TEXT,
    "user_name" TEXT
)""")

print("Table Created")

firstname = input('First Name: \n')
lastname = input('Last Name: \n')
phone = input('Phone Number: \n')
username = input('Enter a username:')

for name in (username):
    cursor.execute("SELECT FROM user_name WHERE name = ?", (name,))
    data=cursor.fetchall()
    if len(data)==0:
        print('')
    else: print('Username already taken. Please select a different username')


# cursor.execute("""INSERT INTO userinfo(first_name, last_name, phone_number, user_name)
# VALUES(?,?,?,?)
# """, (firstname, lastname, phone, username))


conn.commit()
conn.close()

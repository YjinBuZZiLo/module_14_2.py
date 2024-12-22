import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

# for i in range(1, 11):
#     cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',
#                    (f'User{i}', f'example{i}@gmail.com', i * 10, '1000'))

# for j in range(1, 11, 2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?', (500, j))

# for k in range(1, 11, 3):
#     cursor.execute('DELETE FROM Users WHERE id = ?', (k,))

cursor.execute('SELECT username, email, age, balance FROM Users WHERE age !=60')
Users = cursor.fetchall()
#for User in Users:
    #print(f'Имя: {User[0]} | Почта: {User[1]} | Возраст: {User[2]} | Баланс: {User[3]}')

# cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
#print(total_users)
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]
#print(all_balances)
print(all_balances/total_users)

connection.commit()
connection.close()
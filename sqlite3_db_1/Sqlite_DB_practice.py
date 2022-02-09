import sqlite3

# Creating a DB with sqlite3
# ###########################

# conn = sqlite3.connect("spam00.db")
# try:
# 	conn.execute('''CREATE TABLE COMPANY_1 (
# 					ID INT PRIMARY KEY			NOT NULL,
# 					NAME 		MESSAGE_TEXT 	NOT NULL,
# 					CONTACT 	INT 			NOT NULL,
# 					ADDRESS 	CHAR(50),
# 					SALARY 		REAL
# 					);''')
#
# 	print('\nTable Creation Success!')
#
# except Exception:
# 	print('\nTable Creation Failed!')
#
# conn.close()


# Creating/Inserting Data into table
# ###################################
#
# print('\n')
# try:
# 	conn = sqlite3.connect('spam00.db')
# 	print('DB Connection Successful!')
# except Exception:
# 	print('DB Connection Failed!')
# 	conn.close()
#
# try:
# 	conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
# 	VALUES (2, 'JOHN SNOW', 35, 'ACCRA', 25000)")
#
# 	print('Insert Success!')
#
#
# except Exception:
# 	print('Insert Failed!')
# 	conn.close()
#
# try:
# 	conn.commit()
# 	print('Commit Successful!')
#
# except Exception:
# 	print('Commit Failed!')
# 	conn.close()
#
# conn.close()


# Display from DB (Read Records)
# ################
#
# try:
# 	conn = sqlite3.connect('spam00.db')
# 	print('Connection Successful!')
# except Exception:
# 	print('Connection Unsuccessful!')
# 	conn.close()
#
# try:
# 	data = conn.execute("SELECT id, name, contact, address, salary from COMPANY_1")
# 	print('Fetch Success!')
# except Exception:
# 	print('Error! Data could not be read.')
# 	conn.close()
#
# print('\n', ''.center(82, '='))
# print('ID'.rjust(5), '| Name'.ljust(20), '| contact'.rjust(15), '| Address'.ljust(20), '| Salary'.rjust(10))
# print(''.center(82, '='))
#
# for i in data:
# 	print(str(i[0]).rjust(6), str(i[1]).ljust(20), str(i[2]).rjust(15), str(i[3]).ljust(20), str(i[4]).rjust(10))
# print(''.center(82, '='))
#
# print('\nOperation Complete!')
# conn.close()


# Update Records
###############
# try:
# 	conn = sqlite3.connect('spam00.db')
# 	print('Connection Successful!')
# except Exception:
# 	print('Error; Cannot connect to Database!')
# 	conn.close()
#
# try:
# 	conn.execute("UPDATE COMPANY_1 set SALARY = 30000 WHERE id = 3")
# 	conn.commit()
# 	print('Update Operation Successful!')
# except Exception:
# 	print('Update Operation Failed!')
# 	conn.close()
#
# try:
# 	data = conn.execute("SELECT id, name, contact, address, salary FROM COMPANY_1")
# 	print('Data Retrieval Success!')
# except Exception:
# 	print('Data Retrieval Failed!')
#
# print('\n', ''.center(82, '='))
# print('ID'.rjust(5), '| Name'.ljust(20), '| contact'.rjust(15), '| Address'.ljust(20), '| Salary'.rjust(10))
# print(''.center(82, '='))
#
# for i in data:
# 	print(str(i[0]).rjust(6), str(i[1]).ljust(20), str(i[2]).rjust(15), str(i[3]).ljust(20), str(i[4]).rjust(10))
# print(''.center(82, '='))
#
# conn.close()


# Delete Records
# ##############
#
# try:
# 	conn = sqlite3.connect('spam00.db')
# 	print('DB connection established!')
# except Exception:
# 	print('DB connection unsuccessful!')
# 	conn.close()
#
# try:
# 	conn.execute("DELETE FROM COMPANY_1 where ID = 3")
# 	conn.commit()
# 	print('Delete Operation Successful')
# except Exception:
# 	print('Delete Operation Failed!')
# 	conn.close()
#
# data = conn.execute('SELECT ID, NAME, CONTACT, ADDRESS, SALARY FROM COMPANY_1')
#
# print('\n', ''.center(82, '='))
# print(''
# 	  ' ID'.rjust(5), '| Name'.ljust(20), '| contact'.rjust(15), '| Address'.ljust(20), '| Salary'.rjust(10))
# print(''.center(82, '='))
#
# for i in data:
# 	print(str(i[0]).rjust(6), str(i[1]).ljust(20), str(i[2]).rjust(15), str(i[3]).ljust(20), str(i[4]).rjust(10))
# print(''.center(82, '='))
#
# conn.close()

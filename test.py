import pyodbc
name = 'Bob'
server = 'donghe.database.windows.net'
database = 'db-quiz0'
username = 'donghe'
password = 'D20175242.'
driver= '{ODBC Driver 18 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()
cursor.execute("select * from data where Name='Bob'")
row = cursor.fetchone()
print(row)
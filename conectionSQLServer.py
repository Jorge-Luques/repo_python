import pyodbc
conex = pyodbc.connect(
    "Driver={SQL Server};Server=localhost;Database=test;"
    "Uid=sa;Pwd=miPass;Integrated Security=SSPI;")
cursor = conex.cursor()
cursor.execute("SELECT * FROM dbo.TestTable")

for row in cursor:
    print(row)

import cdata.sql as mod

conn = mod.connect("User=user@domain.com; Password=password;")

# Create cursor and iterate over results
cur = conn.cursor()
cur.execute("SELECT * FROM SQLTable")

rs = cur.fetchall()

for row in rs:
    print(row)


# import pyodbc
# from datetime import datetime
#
# class Sql:
#     def __init__(self, database, server="GMSSTEPANENKO,1433"):
#         self.cnxn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
#                                    "Server="+server+";"
#                                    "Database="+database+";"
#                                    "Trusted_Connection=yes;")
#         self.query = "-- {}\n\n-- Made in Python".format(datetime.now()
#                                                          .strftime("%d/%m/%Y"))
# Task 1
# Press the 'Run File' menu button to execute

import sqlite3 as db
con = db.connect('test.db')
with con:
    cur = con.cursor()
    
    #delete table if exists
    cur.execute("DROP TABLE IF EXISTS Pets")
    #create a table for Pets
    cur.execute("CREATE TABLE Pets(Id INT, Name TEXT, Price INT, SalesId INT)")
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Sparky',642,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (2,'Dragon',442,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (3,'Polly',123,2))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Martha',55,3))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Norwegian blue',157,0))
    #show results
    cur.execute("SELECT * FROM Pets")
    rows = cur.fetchall() #rows is s a list/multidimensional array
    print(">>>>>>> With the new arrival of Norwegian Blue...")
    for row in rows:
        print (row)
    cur.execute("DELETE FROM Pets WHERE Name = 'Norwegian blue'")
    #show results
    cur.execute("SELECT * FROM Pets")
    rows = cur.fetchall() #rows is s a list/multidimensional array
    print(">>>>>>> Without the new arrival of Norwegian Blue...")
    for row in rows:
        print (row)
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
    #delete a table for sales people if already there
    cur.execute("DROP TABLE IF EXISTS Sales")
    #create salespeople table
    cur.execute("CREATE TABLE Sales(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Sales VALUES(?,?)",(1,'John'))
    cur.execute("INSERT INTO Sales VALUES(?,?)",(2,'Lola'))
    cur.execute("INSERT INTO Sales VALUES(?,?)",(3,'Sean'))
    a=2
    b="Tomcat"
    c=34
    cur.execute("UPDATE Pets SET Name=?, Price=? WHERE ID=?", (b, c, a))
    con.commit() #strictly unnecessary in “with” block
    cur.execute("SELECT * FROM Pets")
    rows = cur.fetchall() #rows is s a list/multidimensional array
    for row in rows:
        print (row)
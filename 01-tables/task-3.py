# Task 3
# Press the 'Run File' menu button to execute

import sqlite3 as db #import the module
con = db.connect('test.db') #connect to a local file test.db

with con: #with is used to avoid typing con.cur all the time
    cur = con.cursor()	#”with con” opens a level of indentation
    
    #delete table if exists
    cur.execute("DROP TABLE IF EXISTS Pets")
    #create a table for Pets
    cur.execute("CREATE TABLE Pets(Id INT, Name TEXT, Price INT, SalesId INT)")
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Sparky',642,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (2,'Dragon',442,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (3,'Polly',123,2))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Martha',55,3))
    #read the entries now
    cur.execute("SELECT * FROM Pets")

    rows = cur.fetchall() #rows is s a list/multidimensional array

    for row in rows:
        print (row)
#as soon as the indentation is over, the changes will be saved in the database.
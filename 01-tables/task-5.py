# Task 5
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
    cur.execute("SELECT * FROM Pets WHERE Price>350; ")
    rs=cur.fetchall()
    print("print only those pets that are more than £350")
    for row in rs:
        print(row[1], "costs", row[2], "pounds")
#as soon as the indentation is over, the changes will be saved in the database.
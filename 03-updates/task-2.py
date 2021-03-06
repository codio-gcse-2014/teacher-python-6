# Task 2
# Press the 'Run File' menu button to execute

import sqlite3 as db #import the module
con = db.connect('test.db') #connect to a local file test.db

with con: #with is used to avoid typing con.cur all the time
    cur = con.cursor()	#”with con” opens a level of indentation
    
    #delete a table for sales people if already there
    cur.execute("DROP TABLE IF EXISTS Sales")
    #create salespeople table
    cur.execute("CREATE TABLE Sales(Id INT, Name TEXT)")
    cur.execute("INSERT INTO Sales VALUES(?,?)",(1,'John'))
    cur.execute("INSERT INTO Sales VALUES(?,?)",(2,'Lola'))
    cur.execute("INSERT INTO Sales VALUES(?,?)",(3,'Sean'))
    cur.execute("SELECT Sales.Name, COUNT(Pets.ID), GROUP_CONCAT(Pets.Name), "\
                 +"SUM(Pets.Price) FROM Pets INNER JOIN Sales ON Pets.SalesID=Sales.ID GROUP BY Sales.Name; ")
    rs=cur.fetchall()
    print("join 2 tables to lookup salesperson\'s name into the Pets table, grouped by salesperson\n")
    for row in rs:
        print(row[0],"sold",row[1],"Pets, such as:",row[2],"for the total of ",row[3],"pounds")
#as soon as the indentation is over, the changes will be saved in the database.
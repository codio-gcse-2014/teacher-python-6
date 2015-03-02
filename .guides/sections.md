---
title: Database access with SQL
files:
  - action: close
    path: "#tabs"
layout: 3-cell-tree
step: 01-tables

---
## Table create and select queries

Python comes with SQLLITE3 built-in and allows creation of binary database files. The syntax is industry-standard SQL, so can be cross-taught with Access or PHP.

## Task 1
### Pet shop database
A relational database with two tables: 
- Pets(ID,Name,Price,SalesID) 
- Sales(SalesID,SalespersonName)  

joined through a common SalesID field.

Click to open task file : [task-1.py](open_file "01-tables/task-1.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
(1, 'Sparky', 642, 1)
```

## Task 2

Insert more entries into the Pets database. Remember, this goes after  the “with” statement, so  must be indented like the preceding statements.
```sql
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Sparky',642,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (2,'Dragon',442,1))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (3,'Polly',123,2))
    cur.execute("INSERT INTO Pets VALUES(?,?,?,?)", (1,'Martha',55,3))
```

Click to open task file : [task-2.py](open_file "01-tables/task-2.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
(1, 'Sparky', 642, 1)
(2, 'Dragon', 442, 1)
(3, 'Polly', 123, 2)
(1, 'Martha', 55, 3)

```
## Task 3
Limiting output to a few first records, add this code:
```sql
    cur.execute("SELECT * FROM Pets LIMIT 2")
    rs=cur.fetchall()
    print("print first two records only")
    for row in rs:
        print(row)
```
Click to open task file : [task-3.py](open_file "01-tables/task-3.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
print first two records only
(1, 'Sparky', 642, 1)
(2, 'Dragon', 442, 1)
```
## Task 4
Filtering output by criteria, formatting the output:
```sql
    cur.execute("SELECT * FROM Pets WHERE Price>350; ")
    rs=cur.fetchall()
    print("print only those pets that are more than £350")
    for row in rs:
        print(row[1], "costs", row[2], "pounds")
```
Click to open task file : [task-4.py](open_file "01-tables/task-4.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
print only those pets that are more than £350
Sparky costs 642 pounds
Dragon costs 442 pounds
```
## Task 5
Displaying only certain columns:
```sql
    cur.execute("SELECT ID,Name FROM Pets WHERE Price>350; ")
    rs=cur.fetchall()
    print("print only the ID and a Name for pets that are more than £350")
    for row in rs:
        print(row)
```
Click to open task file : [task-5.py](open_file "01-tables/task-5.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
print only the ID and a Name for pets that are more than £350
(1, 'Sparky')
(2, 'Dragon')
```
## Task 6
Now, we will create the other table and populate it.

Click to open task file : [task-6.py](open_file "01-tables/task-6.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
print ID and Name for Salespeople
(1, 'John')
(2, 'Lola')
(3, 'Sean')
```

## Task 7
Note, rather than using parameter queries (the ones with question marks), we used a very unsafe direct injection method – just look up “SQL injection” for more info. This is not safe and is to be avoided. 

Click to open task file : [task-7.py](open_file "01-tables/task-7.py").

Modify the SQL, so that no SQL injection can take place.


















---
title: Database joins (similar to Access lookup)
files:
  - action: close
    path: "#tabs"
layout: ""
step: 02-joins

---
## Task 1
Output the records in the two tables as if there were in one – this is called a “join”:

Click to open task file : [task-1.py](open_file "02-joins/task-1.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
join 2 tables to lookup salesperson's name into the Pets table
(1, 'Sparky', 642, 'John')
(2, 'Dragon', 442, 'John')
(3, 'Polly', 123, 'Lola')
(1, 'Martha', 55, 'Sean')
```

## Task 2
Have the records sorted by price:

Click to open task file : [task-2.py](open_file "02-joins/task-2.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
join 2 tables to lookup salesperson's name into the Pets table, sorted by price
(1, 'Martha', 55, 'Sean')
(3, 'Polly', 123, 'Lola')
(2, 'Dragon', 442, 'John')
(1, 'Sparky', 642, 'John')
```
## Task 3
Have the records grouped by a salesperson:

Click to open task file : [task-3.py](open_file "02-joins/task-3.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
join 2 tables to lookup salesperson's name into the Pets table, grouped by salesperson
John sold 2 Pets, such as: Sparky,Dragon for the total of  1084 pounds
Lola sold 1 Pets, such as: Polly for the total of  123 pounds
Sean sold 1 Pets, such as: Martha for the total of  55 pounds
```
---
title: Update queries
files:
  - action: close
    path: "#tabs"
layout: ""
step: 03-updates

---
The Pet Store realised there was a mistake and instead of a Dragon they have a Tomcat at a much lower price, as well. 

We are also introducing the use of variables (a, b, c) that can be inserted into SQL queries. 

These variables can come from the rest of your Python program, from the user input, or from a file.

## Task 1
Click to open task file : [task-1.py](open_file "03-updates/task-1.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
(1, 'Sparky', 642, 1)
(2, 'Tomcat', 34, 1)
(3, 'Polly', 123, 2)
(1, 'Martha', 55, 3)
```
## Task 2
Rerun your join queries on this new data.

Click to open task file : [task-2.py](open_file "03-updates/task-2.py").

Modify the code and then run the program by pressing the 'Run File' button in the top menu and you should see:
```
join 2 tables to lookup salesperson's name into the Pets table, grouped by salesperson
John sold 2 Pets, such as: Sparky,Tomcat for the total of  1084 pounds
Lola sold 1 Pets, such as: Polly for the total of  123 pounds
Sean sold 1 Pets, such as: Martha for the total of  55 pounds

---
title: Delete Queries
files:
  - action: close
    path: "#tabs"
layout: ""
step: 04-deletes

---
The Pet Store received a delivery of the famous Norwegian Blue Parrot (see Monty Python sketch on this topic) but the unfortunate creature “ceased to be”. 

Our code adds the record, shows all entries with it included, then deletes the record and shows the records without it.


## Task 1
Click to open task file : [task-1.py](open_file "04-deletes/task-1.py").

Run the program by pressing the 'Run File' button in the top menu and you should see:
```
>>>>>>> With the new arrival of Norwegian Blue...
(1, 'Sparky', 642, 1)
(2, 'Dragon', 442, 1)
(3, 'Polly', 123, 2)
(1, 'Martha', 55, 3)
(1, 'Norwegian blue', 157, 0)
>>>>>>> Without the new arrival of Norwegian Blue...
(1, 'Sparky', 642, 1)
(2, 'Dragon', 442, 1)
(3, 'Polly', 123, 2)
(1, 'Martha', 55, 3)
```
## Task 2
Click to open task file : [task-2.py](open_file "04-deletes/task-2.py").

Modify other records and rerun select queries.

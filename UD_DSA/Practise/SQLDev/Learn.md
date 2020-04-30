1. Databases and Spreadsheet: Databases are more efficient at storing data and most importantly changing data. Spreadsheets are good for ledger type activities but doesn't really come handy when we talk about updating data, Databases separate the data from how it is displayed.

2. Relational Databases: Relational databases have relations between various tables. A databse will separate the fields for us, as we want only certain type of data. Relational databases try to highlight how one data relates to other data.

3. Database Normalization is the process of organizing the fields and tables of a relational database to minimize redundancy and dependency.

    Why Normalization ? 
        Basically, when the question comes as to why we do normalization, the basic thing that comes to our minds is the following:
            i) Insert anomaly
            ii) Update Anomaly
            iii) Delete Anomaly

    Normal Forms:
        1. 1NF(1st Normal Form): In accordance with the 1NF, an attribuute of a table cannot hold multiple values. It should hold only atomic values.

        2. 2NF(2nd Normal Form): A table is said to be in 2nd normal form if the following conditions hold:
            i) Tables are in 1NF
            ii) No non -prime attribute is dependent on the proper subset of any candidate key in the table.

            An atttribute that is not a part of the candidate key is known as a non prime attribute.
            If a non prime attribute just depends on the proper subset of the candidate key, then we can simplyy break the data into two tables with the new table being the candidate key and the non prime attribut.

        3. 3NF (3rd Normal Form): 
            i) Transitive dependency - X->Z is a transitive dependency if the following three functional dependencies hold true. 
                i) X->Y
                ii) Y does not belongs to X
                iii)Y->Z
            
            So, for a table to be in 3rd Normal Form, It should already be in 2nd Normal Form and Transitive functional dependency of non prime attribute on any super key should be removed.
            In other simple words, 3NF can be explained like this, A table is in 3NF if it is in 2NF and for each functional dependency X->Y, at least one of the following conditions hold true. 
                X->Y , X is a super key
                Y is a prime attribute of table.
            When we have a transitive functional dependency, we remove that by splitting up the data simply into two columns.

        4. BCNF(Boyce code normal form):
            With the properties of 3NF, What we simply do in this is that we can have candidate key comprising of only one attribute, for every relation X-Y, X should be a super key of the table.

    Sometimes, Denormaliztion, is required to improve performance operation.

4.  OLAP - Online Analytical Processing, 
    OLTP - Online Transaction Processing.
    CRUD - Create/Read/Update/Delete - Basic level to interact with the database.

5. SELECT Statement
6. Create Statement
7. CHECK inside CREATE statement
8. DISCTINCT keyword is used to sleect distinct rows only!
9. set @a1 := (select count(*) from table)
    This is how we store variables in sql
10. select @a1-@a2 as diff ==> Addition or subtraction operations
11. When you have to check for a particular character in a string
    substring() method of SQL, basically comes very handy.
    substring(col_name,-1,1) => 2nd argument probably is from the back or the start and then same like python not in ('a','e'..)

12. select city,length(city) from station order by length(city) ASC,city limit 1
                                                    => Telling that we want to order by length
                                                    => ASC, city (Ascending wrt city)
                                                    => We want one result

13. select name from students where marks > 75 order by RIGHT(name,3), id ASC;
                                                => This tells how i am ordering my o/p
                                                => and how do i want it to be
                                                => We just specify the sorting parameters one by one and so on.

14. Case statment in MySQL
<!-- https://www.hackerrank.com/challenges/what-type-of-triangle/problem?isFullScreen=true -->
A case starts with case symbol and ends with the END statement.
We can have nested cases as well, inside which we have various things separated by when
and we end using the END statemment

select case when a+b >c then
        case when a=b and b=c and c=a then "Equilateral"
        when a=b or b=c or c=a then "Isosceles"
        when a!=b and b!=c and c!=a then "Scalene"
        end
        else "Not A Triangle" 
        end 
        from triangles;
        
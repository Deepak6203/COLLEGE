import sqlite3
connection = sqlite3.connect("Sqlite3-Database.db")
cursor = connection.cursor()


# SQL queries to create multiple tables
create_table1 = '''
CREATE TABLE Cameras (
    ID TEXT,
    Name TEXT
);
'''

create_table2 = '''
CREATE TABLE Rules (
    Rule_ID TEXT,
    Camera_ID TEXT,
    Type TEXT
);
'''

create_table3 = '''
CREATE TABLE Density_Rule (
    Rule_ID TEXT,
    Count INTEGER,
    Fence TEXT,
    Zone TEXT
);
'''

create_table4 = '''
CREATE TABLE Time_Rule (
    Rule_ID TEXT,
    Time_From TEXT,
    Time_To TEXT,
    Fence TEXT,
    Zone TEXT
);
'''

create_table5 = '''
CREATE TABLE Hybrid_Rule (
    Rule_ID TEXT,
    Time_From TEXT,
    Time_To TEXT,
    Count INTEGER,
    Fence TEXT,
    Zone TEXT
);
'''

create_table6 = '''
CREATE TABLE Recording (
    Recording_ID TEXT,
    Recorded_Time_From TEXT,
    Recorded_Time_To TEXT,
    Recording_Location TEXT,
    Camera_ID TEXT
);
'''

create_table7 = '''
CREATE TABLE Incident_Rule (
    Incident_ID TEXT,
    Incident_Time TEXT,
    Incident_TimeStamp TEXT,
    Recording_ID TEXT,
    Rule_ID TEXT,
    Camera_ID TEXT
);  
'''



# Execute each CREATE TABLE statement
cursor.execute(create_table1)
cursor.execute(create_table2)
cursor.execute(create_table3)
cursor.execute(create_table4)
cursor.execute(create_table5)
cursor.execute(create_table6)
cursor.execute(create_table7)



## Commit the changes to the database
connection.commit()

## Close the database connection
connection.close()
import mysql.connector

#this s=is used to connect python with the mysql database 
mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"

)


#we can directly run the sql commands in the mysql workbench and it will run the commands and create the database and tables in the server
#or we can aslo coonect the mysql with python and give the sql commands and it will also connects with the mysql server and creates the database and tables
#we will write all the commands in the variable we wanted to execute and auto increment is used for incrementing the numbers and unique is used to check for no duplicates
#current_timestamp gives the prsent time when it is created and foreign key is used to link user_id to users and on delete cascade is used when user is deleted then their responses will be deleted
sql="""
CREATE DATABASE IF NOT EXISTS social_engineering_simulator;
USE social_engineering_simulator;

CREATE TABLE users(
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    department VARCHAR(100),
    status ENUM('trained','not_trained') DEFAULT 'not_trained'
    );

CREATE TABLE scenarios(
    scenario_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    email_subject VARCHAR(255) NOT NULL,
    email_body TEXT NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );

CREATE TABLE responses(
    response_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    scenario_id INT NOT NULL,
    clicked BOOLEAN DEFAULT FAlSE,
    submitted_data BOOLEAN DEFAULT FALSE,
    response_time DATETIME NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    FOREIGN KEY (scenario_id) REFERENCES scenarios(scenario_id) ON DELETE CASCADE
    );
"""

try:
    mycursor=mydb.cursor()#creates the mycursor object to execute sql statements

    for statement in sql.split(";"):#splits the sql statements into individual commands
        if statement.strip():#strips the white spaces and executes the statements
            mycursor.execute(statement)#this executes each statement
            print(f"executed: {statement.strip()}")
    
    print("Database and tables created sucessfully!")
#finds if any error and prints it
except mysql.connector.Error as err:
    print(f"error:{err}")
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()
#this is used to make the database and curosor connections are closed for freeing the resources
import mysql.connector

mydb=mysql.connector.connect(
    host="your_hostname",
    user="your_username",
    password="your_passowrd"

)

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
    mycursor=mydb.cursor()

    for statement in sql.split(";"):
        if statement.strip():
            mycursor.execute(statement)
            print(f"executed: {statement.strip()}")
    
    print("Database and tables created sucessfully!")
    
except mysql.connector.Error as err:
    print(f"error:{err}")
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()

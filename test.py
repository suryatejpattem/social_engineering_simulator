import mysql.connector

#connect to the database to add values into the table and also mention the database to use
mydb=mysql.connector.connect(
    host="localhost",
    user="root",      
    password="password",  
    database="social_engineering_simulator" 
)


# this is list of tuples where each tuple is record for each user and same as the scenarios values with title ans subject
sample_users = [
    ("Alice Johnson", "suryatej2601@gmail.com", "IT", "not_trained"),
    ("Bob Smith", "suryatej276@gmail.com", "HR", "not_trained"),
    ("Charlie Brown", "suryatejpattem@gmail.com", "Finance", "not_trained"),
]

sample_scenarios = [
    ("Phishing - Fake Login Page", "Important: Update Your Account Info",
     "Dear User, your account is at risk! Click the link to update your details immediately."),
    ("Phishing - Prize Scam", "Congratulations! You've Won!",
     "Hello, you’ve won a free gift card! Click the link to claim your prize."),
]

# Connect to the database
try:
    mycursor = mydb.cursor()

    # Insert sample users by looping  through each tuple
    for user in sample_users:
        try:
            print(f"Inserting user: {user}")#this try block is for debugging purpose 
            mycursor.execute("""
            INSERT INTO users (name, email, department, status)
            VALUES (%s, %s, %s, %s)
            """, user)
        except mysql.connector.Error as err:
            print(f"error inserting user {user[0]}:{err}")

    # Insert sample scenarios
    for scenario in sample_scenarios:
        try:
            print(f"Inserting scenario: {scenario}")
            mycursor.execute("""
            INSERT INTO scenarios (title, email_subject, email_body)
            VALUES (%s, %s, %s)
            """, scenario)
        except mysql.connector.Error as err:
            print(f"error inserting scenarrio {scenario[0]}:{err}")

    # Commit changes after inserting and deleting for making changes in the database
    mydb.commit()

    print(f"{len(sample_users)} users and {len(sample_scenarios)} scenarios added successfully!")

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # Close the connection
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()

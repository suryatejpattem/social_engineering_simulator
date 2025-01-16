import smtplib
import mysql.connector
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart 

mydb=mysql.connector.connect(
    host="your_hostname",
    user="your_username",
    password="your_password",
    database="social_engineering_simulator"
)

#we can use variables to save these or can use the dictionary for this
email_config={
    "smtp_server":"smtp.gmail.com",
    "smtp_port":587,
    "sender_email":"your_sender_email",
    "sender_password":"your_password"
}

try:
    mycursor=mydb.cursor()

    mycursor.execute("SELECT user_id, name, email FROM users WHERE status = 'not_trained'")
    users=mycursor.fetchall()

    mycursor.execute("SELECT scenario_id, email_subject, email_body FROM scenarios")
    scenarios=mycursor.fetchall()

    tracking_base_url = "https://xxxxxxxxxxxxxxx.ngrok-free.app/track_click"

    for user in users:
        user_id,name,user_email=user
        for scenario in scenarios:
            scenario_id,subject,body=scenario

            mycursor.execute("""
                SELECT * FROM responses 
                WHERE user_id = %s AND scenario_id = %s
            """, (user_id, scenario_id))

            if mycursor.fetchone():
                print(f"Email already sent to {name} ({user_email}) for scenario: {subject}")
                continue 
            
            tracking_link = f"{tracking_base_url}?user_id={user_id}&scenario_id={scenario_id}"

            
            full_body = f"{body}\n\nClick here to respond: {tracking_link}"

            #create email message
            message=MIMEMultipart()
            message["from"]=email_config["sender_email"]
            message["to"]=user_email
            message["subject"]=subject

            message.attach(MIMEText(full_body,"plain"))

            
            try:
                with smtplib.SMTP(email_config["smtp_server"],email_config["smtp_port"]) as server:
                    server.starttls()
                    server.login(email_config["sender_email"],email_config["sender_password"])
                    text=message.as_string()
                    server.sendmail(email_config["sender_email"],user_email,text)
                    print(f"phishing email sent to {name} ({user_email}) for scenario: {object}")

                    
                mycursor.execute("""
                    INSERT INTO responses (user_id, scenario_id, clicked)
                    VALUES (%s, %s, FALSE)
                """, (user_id, scenario_id))
                mydb.commit()
            
            except Exception as e:
                print("failed to send phishing email")

except mysql.connector.Error as err:
    print("database error")
finally:
    if mycursor:
        mycursor.close()
    if mydb:
        mydb.close()

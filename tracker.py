from flask import Flask,request,render_template,url_for
import mysql.connector
import hashlib

app=Flask(__name__)#creates instance of the flask application

#connect the mysql database server
mydb=mysql.connector.connect(
    host="your_localhost",
    user="your_username",
    password="your_password",
    database="social_engineering_simulator"

)

@app.route('/dashboard')
def dashboard():
    mycursor=None
    try:
        mycursor=mydb.cursor()

        mycursor.execute("""
            SELECT u.name, u.email, s.title, r.clicked, r.response_time
            FROM responses r
            JOIN users u ON r.user_id = u.user_id
            JOIN scenarios s ON r.scenario_id = s.scenario_id
        """)
        responses = mycursor.fetchall()

        # Render the HTML template with data
        return render_template('dashboard.html', responses=responses)

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return "An error occurred while fetching data."

@app.route('/track_click')
def track_click():
    user_id = request.args.get('user_id')
    scenario_id = request.args.get('scenario_id')

    if not user_id or not scenario_id:
        return "Invalid tracking link."

    mycursor = None
    try:
        mycursor = mydb.cursor()

        # Update the 'clicked' status in the responses table
        mycursor.execute("""
            UPDATE responses
            SET clicked = TRUE, response_time=NOW()
            WHERE user_id = %s AND scenario_id = %s
        """, (user_id, scenario_id))
        mydb.commit()

        #update the user table after clicking the link
        mycursor.execute("""
            UPDATE users
            SET status = 'trained'
            WHERE user_id = %s
        """, (user_id,))
        mydb.commit()

        # Display a thank-you message
        return render_template("response.html")

    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return "An error occurred while tracking your response."
    finally:
        if mycursor:
            mycursor.close()

if __name__ == '__main__':
    app.run(debug=True)

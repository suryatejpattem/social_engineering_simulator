# Social Engineering Simulator

A phishing simulation tool designed to help organizations train their employees on how to recognize and respond to phishing emails. The tool sends simulated phishing emails to users, tracks their responses, and provides a dashboard for monitoring.

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Configure Email Settings](#configure-email-settings)
6. [Run the Web Application](#run-the-web-application)
7. [Use ngrok for External Access](#use-ngrok-for-external-access)
8. [License](#license)

## Overview

The Social Engineering Simulator provides a platform for simulating phishing attacks and tracking user responses. It connects to a MySQL database to store user and scenario data, sends phishing emails using Gmail's SMTP server, and provides a Flask-based web dashboard to display the results.

## Features

- Simulate phishing emails with custom scenarios.
- Track whether users click on the phishing links.
- Dashboard to monitor user responses.
- MySQL database integration for managing users, scenarios, and responses.
- SMTP email sending with Gmail.
- Expose your local Flask server to the internet using **ngrok**.

## Installation

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone https://github.com/yourusername/social-engineering-simulator.git
cd social-engineering-simulator
```
2. Install Dependencies
Install the required Python dependencies by running:

bash
Copy code
pip install -r requirements.txt
This will install Flask, MySQL connector, and other necessary libraries.

3. Configure the Database
Create a MySQL database named social_engineering_simulator using the following SQL query:
sql
Copy code
CREATE DATABASE social_engineering_simulator;
Update the database connection details in database.py, email_send.py, and tracker.py to match your local MySQL configuration.
4. Initialize the Database
Run the database.py script to set up the required database schema:

bash
Copy code
python database.py
This will create the necessary tables in the database.

5. Populate the Database
To insert sample data into the database (e.g., users, scenarios), run the test.py script:

bash
Copy code
python test.py
This will populate the users and scenarios tables with mock data.

6. Configure Email Settings
Update the email_config dictionary in email_send.py with your SMTP server details and email credentials:

python
Copy code
email_config = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "your-email@gmail.com",
    "sender_password": "your-email-password"
}
If using Gmail, you may need to enable "Less Secure Apps" or create an App Password for security.

7. Run the Web Application
Start the Flask server to access the dashboard and track user responses:

bash
Copy code
python tracker.py
This will start the application at http://127.0.0.1:5000. You can open this URL in your browser to access the dashboard and track clicks.

Use ngrok for External Access
If you want to make your local Flask application publicly accessible (for example, to send phishing emails with links that need to be clicked externally), you can use ngrok.

Download ngrok from https://ngrok.com/download and install it.

Expose your local Flask server to the internet by running the following command:

bash
Copy code
ngrok http 5000
This will generate a public URL (e.g., https://xxxxxxxx.ngrok.io) that you can use in your phishing emails.

Update the tracking URL in the phishing email to use the ngrok URL:
python
Copy code
tracking_base_url = "https://xxxxxxxx.ngrok.io/track_click"
Now, any clicks on the phishing link will be tracked via the publicly accessible URL provided by ngrok.

License
This project is licensed under the MIT License - see the LICENSE file for details.

vbnet
Copy code

### Key Additions:
- **Use ngrok for External Access**: This section explains how to set up ngrok to expose your local server to the internet and update the tracking URL in the phishing email.
- **Instructions to update phishing email links**: The ngrok-generated URL is used to replace the local server URL in the email tracking link.

This should now provide full instructions on using ngrok for external access during testing.

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
### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure the Database

```sql
CREATE DATABASE social_engineering_simulator;
```
Update the database connection details in database.py, email_send.py, and tracker.py to match your local MySQL configuration.

### 4. Initialize the Database

```bash
python database.py
```

### 5. Populate the Database

```bash
python test.py
```

### 6. Configure Email Settings
Update the email_config dictionary in email_send.py with your SMTP server details and email credentials:

```python

email_config = {
    "smtp_server": "smtp.gmail.com",
    "smtp_port": 587,
    "sender_email": "your-email@gmail.com",
    "sender_password": "your-email-password"
}
```

### 7. Run the Web Application

```bash
python tracker.py
```

### Use ngrok for External Access

Expose your local Flask server to the internet by running the following command:

```bash
ngrok http 5000
```
This will generate a public URL (e.g., https://xxxxxxxx.ngrok.io) that you can use in your phishing emails.
Update the tracking URL in the phishing email to use the ngrok URL:

```python
tracking_base_url = "https://xxxxxxxx.ngrok.io/track_click"
```

### License
This project is licensed under the MIT License - see the LICENSE file for details.


### Key Additions:
- **Use ngrok for External Access**: This section explains how to set up ngrok to expose your local server to the internet and update the tracking URL in the phishing email.
- **Instructions to update phishing email links**: The ngrok-generated URL is used to replace the local server URL in the email tracking link.

```css
This should now provide full instructions on using ngrok for external access during testing.
```

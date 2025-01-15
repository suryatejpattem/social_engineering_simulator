# Social Engineering Simulator

A cybersecurity tool designed to simulate phishing attacks and raise awareness about human-centric cybersecurity threats. The application sends phishing emails to users, tracks their interactions, and provides insights through a dashboard.

---

## Features

- **User Management**: Add and manage users targeted in phishing simulations.
- **Phishing Scenarios**: Create realistic phishing email scenarios.
- **Email Automation**: Send phishing emails with embedded tracking links.
- **Tracking and Analysis**: Track if users clicked on phishing links and log their response time.
- **Dashboard**: Display user interactions with phishing emails in an intuitive web interface.

---

## Technologies Used

- **Backend**: Python with Flask
- **Database**: MySQL
- **Frontend**: HTML/CSS (Jinja templating engine)
- **Email Service**: SMTP with Python's `smtplib`

---

## Prerequisites

Ensure you have the following installed on your system:

1. Python 3.8+  
2. MySQL Server  
3. A valid SMTP server (e.g., Gmail) and email credentials.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/social-engineering-simulator.git
cd social-engineering-simulator


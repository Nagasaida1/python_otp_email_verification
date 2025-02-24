# python_otp_email_verification


# OTP Verification System

This is a Python-based OTP (One-Time Password) Verification System. It generates a 6-digit OTP and sends it to the user's email address for verification. The project uses the `smtplib` library to send emails and `tkinter` for the graphical user interface (GUI).

## Features
- Generates a 6-digit random OTP.
- Sends the OTP to the user's email address.
- Provides a simple GUI for email input, OTP sending, and verification.
- Verifies the OTP entered by the user.

## Prerequisites
Before running the project, ensure you have the following:
1. **Python 3.x** installed on your system.
2. Required Python libraries: `smtplib`, `email`, `tkinter`, and `random`. These are part of Python's standard library, so no additional installation is needed.

## Setup Instructions

### 1. Clone the Repository
Clone this repository to your local machine using the following command:
```bash
git clone https://github.com/Nagasaida1/python_otp_email_verification.git


## 2. Configure Email Settings
To send OTPs via email, you need to configure the sender's email and password in the `send_otp` function in the code.

1. Open the `otp_verification.py` file.
2. Replace the following placeholders with your email credentials:
   ```python
   sender_email = "your-email@gmail.com"  # Replace with your email
   sender_password = "your-app-specific-password"  # Replace with your app-specific password

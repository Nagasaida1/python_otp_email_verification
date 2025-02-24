import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import tkinter as tk
from tkinter import messagebox

# Generate a 6-digit random OTP 
def generate_otp():
    return f"{random.randint(100000, 999999)}"

# Send the OTP to the receiver's email
def send_otp(receiver_email, otp):
    try:
        sender_email = " "  # Replace with your email
        sender_password = " "  # 16 digits pasword Replace with your app-specific password

        smtp_server = "smtp.gmail.com"
        smtp_port = 587

        subject = "Your OTP Code"
        body = f"Your OTP is: {otp}\n\nPlease do not share it with anyone."

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = subject
        message.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.send_message(message)
        
        return True
    except Exception as e:
        print(f"Error sending OTP: {e}")
        return False

# Define GUI using (tkinter)
class OTPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification System")
        self.root.geometry("400x300")

        self.otp = ""  # OTP will be stored here

        # Email input
        self.email_label = tk.Label(root, text="Enter your email:")
        self.email_label.pack(pady=5)

        self.email_entry = tk.Entry(root, width=30)
        self.email_entry.pack(pady=5)

        # Send OTP button
        self.send_otp_button = tk.Button(root, text="Send OTP", command=self.send_otp)
        self.send_otp_button.pack(pady=10)

        # OTP input
        self.otp_label = tk.Label(root, text="Enter the OTP:")
        self.otp_label.pack(pady=5)

        self.otp_entry = tk.Entry(root, width=15)
        self.otp_entry.pack(pady=5)   

        # Verify OTP button
        self.verify_otp_button = tk.Button(root, text="Verify OTP", command=self.verify_otp)
        self.verify_otp_button.pack(pady=10)

    def send_otp(self):
        email = self.email_entry.get()
        if not email:
            messagebox.showerror("Error", "Please enter an email address.")
            return
        
        self.otp = generate_otp()
        if send_otp(email, self.otp):
            messagebox.showinfo("Success", "OTP sent successfully!")
        else:
            messagebox.showerror("Error", "Failed to send OTP. Please try again.")

    def verify_otp(self):
        user_otp = self.otp_entry.get()
        if user_otp == self.otp:
            messagebox.showinfo("Success", "OTP verified. Access granted.")
            self.otp_entry.delete(0, tk.END)  # Clear the OTP input field
        else:
            messagebox.showerror("Error", "Invalid OTP. Access denied.")

# Main
if __name__ == "__main__":
    root = tk.Tk()
    app = OTPApp(root)
    root.mainloop()

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
import re
from config import EMAIL_SENDER, EMAIL_PASSWORD

class EmailService:
    def __init__(self):
        self.sender_email = EMAIL_SENDER
        self.sender_password = EMAIL_PASSWORD
        if not self.sender_email or not self.sender_password:
            raise Exception("Email sender and password must be configured in config.py")
        self.smtp_server = "smtp.gmail.com"
        self.smtp_port = 587

    def validate_email(self, email):
        """Validate email format"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(pattern, email):
            raise Exception("Invalid email format")

    def send_weather_update(self, recipient_email, location, temperature, description):
        self.validate_email(recipient_email)
        try:
            message = MIMEMultipart()
            message["From"] = self.sender_email
            message["To"] = recipient_email
            message["Subject"] = f"Weather Update for {location}"

            body = f"""
            Here's your weather update for {location}:
            Temperature: {temperature}°C
            Conditions: {description}
            """
            
            message.attach(MIMEText(body, "plain"))

            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.send_message(message)
            
            return True
        except Exception as e:
            raise Exception(f"Failed to send email: {str(e)}")

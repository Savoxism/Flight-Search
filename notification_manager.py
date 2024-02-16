import smtplib

MY_EMAIL = "YOUR EMAIL"
MY_PASSWORD = "YOUR PASSWORD"

class NotificationManager: 
    
    def __init__(self):
        self.email = MY_EMAIL
        
    def send_sms(self, message):
        pass
    
    def send_email(self, emails, message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user = MY_EMAIL, password = MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr = MY_EMAIL,
                    to_addrs= email,
                    msg = f"Subject:Low price alert!\n\n{message}".encode('utf-8')
                )
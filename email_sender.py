import smtplib

def send_email(sender, password, receiver, message):
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender, password)
        server.sendmail(sender, receiver, message)
        print("Email sent!")
        server.quit()
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    send_email("your_email@gmail.com", "your_password", "to@gmail.com", "Hello from Python!")

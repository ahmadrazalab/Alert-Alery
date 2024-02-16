import psutil
import smtplib
from email.mime.text import MIMEText

# Function to check CPU usage
def check_cpu_usage():
    cpu_percent = psutil.cpu_percent(interval=1)
    return cpu_percent

# Function to send email alert
def send_email_alert(subject, body):
    sender_email = 'test@gmail.com'    # Your email address of SMTP Server 
    receiver_email = 'dev@alery.in'      # Your email address of receiver alery 
    password = 'abcd xyz'  # Use App Password if 2FA is enabled

    message = MIMEText(body)
    message['Subject'] = subject
    message['From'] = sender_email
    message['To'] = receiver_email

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email alert sent successfully!")
    except Exception as e:
        print("Failed to send email alert:", e)

# Main function
def main():
    threshold = 60  # CPU usage threshold in percentage

    cpu_usage = check_cpu_usage()
    if cpu_usage > threshold:
        subject = "High CPU Usage Alert!"
        body = f"CPU usage is {cpu_usage}% which exceeds the threshold of {threshold}%"
        send_email_alert(subject, body)

if __name__ == "__main__":
    main()

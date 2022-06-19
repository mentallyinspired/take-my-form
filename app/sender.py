import smtplib, ssl, os
from email.message import EmailMessage
import configparser

class Sender():
    def __init__(self) -> None:
        config = configparser.ConfigParser()
        config_file = os.path.join(os.path.dirname(__file__), "config", "config.ini")
        config.read(config_file)

        self.MAIL_SERVER = config['SMTP']['MAIL_SERVER']
        self.FROM_ADDRESS = config['SMTP']['FROM_ADDRESS']
        self.PORT = config['SMTP']['PORT']
        self.PASSWORD = config['SMTP']['PASSWORD']

    def validate_config(self):
        pass

    def send_mail(self, to_email, name, email, message, subject):
        
        context = ssl.create_default_context()

        # Create the base text message.
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = self.FROM_ADDRESS

        msg['To'] = to_email
        msg.set_content(f"""\
        {message}

        --{name}
        """)

        msg.add_header('reply-to', email)

        # Send the message via local SMTP server.
        with smtplib.SMTP_SSL(self.MAIL_SERVER, self.PORT, context=context) as s:
            s.login(self.FROM_ADDRESS, self.PASSWORD)
            s.send_message(msg)
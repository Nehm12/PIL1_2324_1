# smtp_test.py

import smtplib
from email.message import EmailMessage

def test_smtp_connection():
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('exaucehga123@gmail.com', 'exaucehga123@Gmail')
        print("SMTP connection successful!")
    except Exception as e:
        print(f"SMTP connection failed: {e}")
    finally:
        server.quit()

# Appel de la fonction de test
test_smtp_connection()

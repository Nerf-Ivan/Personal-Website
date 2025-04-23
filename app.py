from flask import Flask, render_template, request, redirect, url_for, flash
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import os

app = Flask(__name__)

# Set a secret key for flash messages
app.secret_key = "your-secret-key-here"  # Replace with a secure random string in production

# Debug: Print the current working directory
print(f"Current working directory: {os.getcwd()}")

# Load environment variables from credentials.env using an absolute path
load_dotenv("/home/ivan-swanepoel/Personal-Website/credentials.env")
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# Validate environment variables at startup
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("EMAIL_ADDRESS or EMAIL_PASSWORD not set in credentials.env")

# Debug: Print credentials at startup
print(f"Startup - EMAIL_ADDRESS: {EMAIL_ADDRESS}")
print(f"Startup - EMAIL_PASSWORD: {EMAIL_PASSWORD}")

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/send-message", methods=["POST"])
def send_message():
    # Reload environment variables to ensure they're available
    load_dotenv("/home/ivan-swanepoel/Personal-Website/credentials.env")
    email_address = os.getenv("EMAIL_ADDRESS")
    email_password = os.getenv("EMAIL_PASSWORD")

    # Debug: Print credentials during the request
    print(f"Request - EMAIL_ADDRESS: {email_address}")
    print(f"Request - EMAIL_PASSWORD: {email_password}")

    # Validate credentials
    if not email_address or not email_password:
        flash("Error: Could not load email credentials", "error")
        return redirect(url_for("home") + "#contact")

    # Get form data
    visitor_email = request.form.get("email")
    visitor_message = request.form.get("message")

    # Validate form data
    if not visitor_email or not visitor_message:
        flash("Error: Email and message are required", "error")
        return redirect(url_for("home") + "#contact")

    # Set up the email
    msg = MIMEMultipart()
    msg["From"] = email_address
    msg["To"] = "ivan.swanepoel.dev@gmail.com"
    msg["Subject"] = "New Message from Your Website"
    body = f"From: {visitor_email}\n\nMessage:\n{visitor_message}"
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to Gmail's SMTP server
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email_address, email_password)
        server.sendmail(email_address, "ivan.swanepoel.dev@gmail.com", msg.as_string())
        server.quit()
        flash("Your message was sent successfully! I'll get back to you soon.", "success")
        return redirect(url_for("home") + "#contact")
    except smtplib.SMTPAuthenticationError as auth_error:
        flash("Error: Invalid email credentials. Please check EMAIL_ADDRESS and EMAIL_PASSWORD.", "error")
        return redirect(url_for("home") + "#contact")
    except Exception as e:
        flash(f"Error sending email: {str(e)}", "error")
        return redirect(url_for("home") + "#contact")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
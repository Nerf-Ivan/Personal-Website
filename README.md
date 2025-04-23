# Personal-Website

Welcome to my personal website! This is a Flask-based web application where I showcase my skills, education, and projects as an aspiring software engineer. The site includes a contact form that allows visitors to send me messages via email.You will find all sorts of info about me. This page will be updated and improved as I learn new cool skills. Feel free to leave feedback in my form

# Features

Responsive Sidebar Navigation: Navigate through sections like Home, Skills, Education, and Contact, with a toggleable sidebar.
Social Links: Links to my email, phone, Instagram, Facebook, and GitHub in the sidebar, styled with Boxicons.
Contact Form: Visitors can send messages directly to my email using a form powered by Flask and Gmail SMTP.
Flash Messages: User-friendly success/error messages for form submissions, styled to match the site’s design.
Modern Design: A dark theme with blue accents, custom CSS, rounded corners, shadows, and hover effects for interactivity.

# Prerequisites

Python 3.8 or higher
A Gmail account with an App Password for SMTP (requires 2-Step Verification enabled on your Google Account)
A virtual environment (recommended)

# Installation
1. Clone the Repository
If this project is hosted in a Git repository, clone it:
git clone <https://github.com/Nerf-Ivan/Personal-Website.git>
cd Personal-Website

2. Set Up a Virtual Environment
Create and activate a virtual environment to manage dependencies:
python -m venv venv


On Windows: venv\Scripts\activate
On macOS/Linux: source venv/bin/activate

3. Install Dependencies
Install the required packages listed in requirements.txt:
pip install -r requirements.txt

The requirements.txt file includes:
Flask==3.0.3
python-dotenv==1.0.1
gunicorn==23.0.0

4. Configure Environment Variables
Create a file named credentials.env in the project root with the following:
EMAIL_ADDRESS=your-email@gmail.com
EMAIL_PASSWORD=your-app-password


Replace your-email@gmail.com with your Gmail address (e.g., ivan.swanepoel.dev@gmail.com).
Replace your-app-password with a Gmail App Password. To generate one:
Enable 2-Step Verification in your Google Account settings.
Go to Security > App Passwords, select "Mail" as the app, and generate a 16-character password (e.g., agokqawqtkcjcohs).
Copy the password without spaces into credentials.env.



5. Run the Application
Start the Flask development server:
python app.py

The app will be available at http://127.0.0.1:5000/.
Project Structure
Personal-Website/
│
├── app.py               # Main Flask application
├── credentials.env      # Environment variables (not tracked in Git)
├── requirements.txt     # Project dependencies
├── static/              # Static files (CSS, images)
│   ├── style.css        # Custom styles for the website
│   └── ivanfotowebsite.jpg  # Profile image for the sidebar
└── templates/           # HTML templates
    └── index.html       # Main template with sidebar and content sections

# Usage

Open http://127.0.0.1:5000/ in your browser to view the website.
Use the sidebar to navigate between sections (Home, Skills, Education, Contact).
Click the menu icon in the sidebar to expand/collapse it.
In the Contact section, fill out the form with your email and message to send me a message. You’ll see a styled success or error message upon submission.
Click the social links in the sidebar to visit my profiles or contact me directly.

# Deployment
To deploy this app (e.g., on Heroku):

Ensure gunicorn is in requirements.txt.

Create a Procfile with:
web: gunicorn app:app


Set environment variables on the hosting platform:

EMAIL_ADDRESS
EMAIL_PASSWORD


Deploy using the platform’s instructions (e.g., heroku create, git push heroku main).


Note: Some hosting platforms may block SMTP ports. In production, consider using a service like SendGrid or Mailgun for email sending instead of Gmail SMTP.
Contributing
This is a personal project, but I’m open to feedback! If you have suggestions or improvements, feel free to reach out.
# Contact

Email: ivan.swanepoel.dev@gmail.com
GitHub: https://www.github.com/Nerf-Ivan
Instagram: https://www.instagram.com/ivan._.swanepoel
Facebook: https://www.facebook.com/ivan._.swanepoel
# License
This project is for personal use and not currently licensed for public distribution.

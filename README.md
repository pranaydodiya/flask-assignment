Flask Assignment - Student Registration and Login System
=======================================================

Project Overview
----------------
This is a simple Flask-based web application for student registration and login. 
It demonstrates user authentication and session management using Flask.

The project contains:
- Registration Page
- Login Page
- Welcome Page (after successful login)
- Session-based authentication

Features
--------
1. Register a new user with username and password
2. Secure password storage using hashing
3. User login with validation
4. Session handling to keep users logged in
5. Logout functionality

Technologies Used
-----------------
- Python (Flask framework)
- HTML (Frontend)
- CSS (Styling)
- Jinja2 Templating
- Git & GitHub for version control

Project Structure
-----------------
flask-assignment/
│
├── app.py              # Main Flask application
├── templates/          # HTML templates
│   ├── register.html   # Registration page
│   ├── login.html      # Login page
│   ├── welcome.html    # Welcome page after login
│
├── static/             # CSS or images if needed
│   └── style.css
│
└── README.txt          # Project documentation

Installation and Setup
----------------------
1. Clone the repository:
   git clone https://github.com/pranaydodiya/flask-assignment.git

2. Navigate to the project folder:
   cd flask-assignment

3. Create a virtual environment:
   python -m venv venv

4. Activate the environment:
   - Windows: venv\Scripts\activate
   - Linux/Mac: source venv/bin/activate

5. Install required packages:
   pip install flask

6. Run the application:
   python app.py

7. Open in browser:
   http://127.0.0.1:5000/

Git Commands Used
-----------------
echo "# flask-assignment" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/pranaydodiya/flask-assignment.git
git push -u origin main

Future Improvements
-------------------
- Database integration (SQLite/MySQL)
- Email verification for signup
- Password reset functionality
- Deployment on cloud (Heroku/AWS)

Author
------
Pranay Dodiya


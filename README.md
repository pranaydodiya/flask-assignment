📌 Flask + MongoDB Assignment

This is a simple Flask application connected with MongoDB Atlas that demonstrates:

Collecting user input via a form

Saving the input to MongoDB

Displaying stored records on another page

🚀 Features

Home page with a form to enter Name and Role

Stores the submitted data into MongoDB Atlas

Redirects to a second page (/users) that lists all users

Clean and minimal Flask project structure

🛠️ Tech Stack

Flask (Python web framework)

MongoDB Atlas (Cloud database)

HTML (Frontend templates with Jinja2)

📂 Project Structure
flask-mongo-assignment/
│
├── app.py                # Main Flask app
├── templates/
│   ├── index.html        # User input form
│   └── users.html        # Display all users
├── requirements.txt      # Dependencies
└── README.md             # Project documentation

⚙️ Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/pranaydodiya/flask-assignment.git
cd flask-assignment

2️⃣ Create virtual environment
python -m venv venv
venv\Scripts\activate   # For Windows
# source venv/bin/activate  # For Linux/Mac

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Configure MongoDB Atlas

Create a free MongoDB Atlas cluster.

Whitelist your IP address.

Copy your connection string and update it inside app.py:

client = MongoClient("your_mongo_connection_string")

5️⃣ Run the application
py app.py


App will be running on:
👉 http://127.0.0.1:5000

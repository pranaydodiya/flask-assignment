from flask import Flask, jsonify, render_template, request, redirect, url_for
from pathlib import Path
from pymongo import MongoClient
import json

app = Flask(__name__)
DATA_FILE = Path(__file__).with_name("data.json")

# --- MongoDB Atlas connection ---
# Replace <your_connection_string> with your MongoDB Atlas URI
# Example: "mongodb+srv://username:password@cluster0.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient("<your_connection_string>")
db = client["flaskDB"]         # database name
collection = db["users"]       # collection name

@app.get("/api")
def get_api():
    try:
        with DATA_FILE.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []
    return jsonify(data)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            name = request.form.get("name")
            role = request.form.get("role")

            if not name or not role:
                return render_template("index.html", error="Both fields are required!")

            # Insert into MongoDB
            collection.insert_one({"name": name, "role": role})

            return redirect(url_for("success"))
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html")

@app.get("/success")
def success():
    return render_template("success.html")

if __name__ == "__main__":
    app.run(debug=True)

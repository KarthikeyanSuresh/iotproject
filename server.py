from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('localhost', 27017)
# client = MongoClient('localhost', 27017, username='username', password='password') put authentication

db = client.flask_db
todos = db.todos

@app.route("/")
def home():
    return "Hello, World!"
    
if __name__ == "__main__":
    app.run(debug=True)

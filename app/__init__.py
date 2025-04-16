from flask import Flask

app = Flask(__name__)
app.secret_key = "super-secret-key"  # Replace with secure key later

from app import routes

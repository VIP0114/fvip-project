# Backend entry point

from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'F VIP Backend is running'
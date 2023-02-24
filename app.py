import os
import requests
from flask import Flask, flash, redirect, render_template, request, session

PREFIX = "http://localhost:8001"

# Configure application
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    # Get form information
    link = request.form.get("request")
    print(f"User input: {link}")

    # print(requests.get("http://localhost:8001/drone/drone01?data=info").text)
    print(f"Result on request: {requests.get(link).text}")
    return requests.get(link).text

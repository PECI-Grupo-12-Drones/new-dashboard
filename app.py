import requests
from flask import Flask, flash, redirect, render_template, request, session
from http.client import responses

headers = {"Accept": "application/json", "Content-Type": "application/json"}
# Configure application
app = Flask(__name__)
app.secret_key = b'wquygduihgsyfutdyugaiusufdtyg'
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "GET":
        return render_template("index.html")
    
    # Get form information
    link = request.form.get("request")
    print(f"User input: {link}")

    # print(requests.get("http://localhost:8001/drone/drone01?data=info").text)

    response_api = requests.get(link, headers=headers) # talk with api
    flash("Request sent", "success")
    code = response_api.status_code
    code = f"{code} {responses[code]}"
    return render_template("index.html", code=code, response=response_api.json())

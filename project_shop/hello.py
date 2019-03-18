from flask import Flask, render_template, url_for

app = Flask(__name__, static_folder="static")

@app.route('/')

@app.route("/template")

def home():
	return render_template('home.html', title="Home")


# def hello():
# 	return 'Hello, World!'
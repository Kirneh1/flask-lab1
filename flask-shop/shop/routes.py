from flask import render_template, url_for 
from shop import app
from shop import models
@app.route("/")
@app.route("/home")


def home():
	 
	return render_template('home.html', title='Home', paintings=models.paintings)


@app.route("/about")
def about():
	return render_template('about.html', title="About")


@app.route("/layout")
def layout():
	return render_template('layout.html', title='Navigation')


@app.route("/painting/<int:painting_id>")

def painting(painting_id):

	return render_template('painting.html', painting = str(painting_id), name= models.paintings[painting_id-1][1], price= models.paintings[painting_id-1][2], height=models.paintings[painting_id-1][3], width=models.paintings[painting_id-1][4])

# python file to run everything through all your files and the server

from flask import Flask, render_template, redirect, request
app = Flask(__name__)

@app.route('/')
def default_page():
  return render_template("index.html")

@app.route('/ninja')
def ninja():
  return render_template("ninja.html")

@app.route('/ninja/blue')
def ninja_blue():
  return render_template("ninja_blue.html")

@app.route('/ninja/red')
def ninja_red():
  return render_template("ninja_red.html")

@app.route('/ninja/purple')
def ninja_purple():
  return render_template("ninja_purple.html")

@app.route('/ninja/orange')
def ninja_orange():
  return render_template("ninja_orange.html")

@app.route('/ninja/<color>')
def ninja_other(color):
  return render_template("ninja_other.html")

app.run(debug=True)

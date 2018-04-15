# python file to run everything through all your files and the server

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def default_page():
  return render_template("index.html")

app.run(debug=True)

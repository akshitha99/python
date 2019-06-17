from flask import Flask
from flask import Markup
from flask import Flask
from flask import render_template

import datetime
app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')
@app.route('/about')
def about():
  return render_template('about.html')
	
@app.route("/date")
def hello():
   now = datetime.datetime.now()
   timeString = now.strftime("%Y-%m-%d %H:%M")
   templateData = {
      'title' : 'HELLO!',
      'time': timeString
      }
   return render_template('sample1.html', **templateData)
 
if __name__ == '__main__':
  app.run(debug=True)
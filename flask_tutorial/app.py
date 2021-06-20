
from flask import Flask, render_template, request 
from textblob import TextBlob

app = Flask(__name__)

@app.route('/') # default route
def new():
	result = ""
	return render_template('index.html', result = result) # renders template: index.html with argument result = ""

@app.route('/result', methods = ['POST', 'GET']) # /result route, allowed request methods; POST, and GET
def predict():
	if request.method == 'POST': 
		result = request.form['Name'] # fetches text from <input name = "Name"> from index.html
		blob = TextBlob(result)
		for sentence in blob.sentences:
			result = sentence.sentiment.polarity # result = polarity value
		return render_template('index.html', result = result) # renders template: index.html with argument result = polarity value calculated
	else:
		return render_template('index.html')	
		

if __name__ == '__main__':
	app.debug = True
	app.run()
# serve.py

from flask import Flask, render_template, url_for, request

# creates a Flask application, named app
app = Flask(__name__)

# a route where we will display a welcome message via an HTML template
@app.route("/topten/<topic>")
def toptentopic(topic):
	if topic == '' or topic == None:
		return render_template('NotFound.html')	
	return render_template('toptenPage.html', topic=topic)

# a route where we will display a welcome message via an HTML template
@app.route("/topten", methods=['POST'])
def topten():
	if request.method == 'POST':
		topic = request.form.get('topic')
		if topic == '' or topic == None:
			return render_template('NotFound.html')
		return toptentopic(topic)
	return render_template('NotFound.html')



# a route where we will display a welcome message via an HTML template
@app.route("/")
def landingPage():  
	return render_template('index.html')

# run the application
if __name__ == "__main__":  
	app.run(debug=True)
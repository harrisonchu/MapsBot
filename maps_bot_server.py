from flask import Flask
from flask import request
import os

app = Flask(__name__)

@app.route('/directions', methods=['GET', 'POST'])
def directions():
	#Twilio sends the SMS data via POST
	if request.method == 'POST':
		print(request.form['Body'])	

	#return this so twilio doesn't through an error
	return "<Response>"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

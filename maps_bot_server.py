from flask import Flask
from flask import request
import os
import directions_service
from twilio import twiml

app = Flask(__name__)
directions_service = directions_service.DirectionsService()

@app.route('/directions', methods=['GET', 'POST'])
def directions():
	#Twilio sends the SMS data via POST
	directions = "No directions available"
	if request.method == 'POST':
		print(request.form['Body'])	
		user_input = request.form['Body']
		directions = directions_service.get_directions(user_input)

	#return this so twilio doesn't through an error
	response = twiml.Response()
	response.message(directions)
	return response.toxml()

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

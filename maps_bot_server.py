from flask import Flask
import os

app = Flask(__name__)

@app.route('/directions', methods=['GET', 'POST'])
def directions():
	#Twilio sends the SMS data via POST
	if request.method == 'POST':
		print(request.form['Body'])	
	else:
		return "Hello World!"

if __name__ == '__main__':
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)

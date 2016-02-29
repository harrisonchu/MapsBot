class SimpleTwilioResponse:
	def __init__(self):
		self.message = ""

	def set_message(self, message):
		self.message = message

	def print_xml(self):
		response = '<?xml version=\"1.0\" encoding=\"UTF-8\"?>'
		response += "<Response>"
		response += "<Message>"
		response += self.message
		response += "</Message>"
		response += "</Response>"
		return response

import json
import re
import usaddress

def clean_html_tags(raw_html):
 	cleanr =re.compile('<.*?>')
 	cleantext = re.sub(cleanr,'', raw_html)
 	return cleantext

class DirectionQuery:
	def __init__(self, is_valid, raw_input):
		self.is_valid = is_valid
		self.destination = ""
		self.origin = ""
		#For now only bias for US users."
		self.region = "us"
		self.raw_input = raw_input

class DirectionOutput:
	def __init__(self):
		self.origin = ""
		self.destination = ""
		self.turn_by_turn_directions = ""

class DirectionParser:
	def parse_directions_query(self, input):
		input = input.lower()

		#for now assume input is 'from xxx to xxx'
		input_array = input.split("from")
		if len(input_array) != 2:
			return DirectionQuery(False, input)
		input_array = input_array[1].split(" to ")
		if len(input_array) != 2:
			return DirectionQuery(False, input)
		destination = input_array[1]
		origin = input_array[0]
		if len(destination) == 0 or len(origin) == 0:
			return DirectionQuery(False, input)	

		# Looks like everything is good.  create the direction query
		query = DirectionQuery(True, input)
		query.destination = destination
		query.origin = origin
		return query

	def parse_directions_output(self, directions_json_string):
		j = json.loads(directions_json_string)
		steps = j['routes'][0]['legs'][0]['steps']	

		full_directions = ""
		for step in steps:
			clean_step = clean_html_tags(step['html_instructions'])	
			distance_in_direction = step['distance']['text']
			full_directions += clean_step + " for " + distance_in_direction + ".  \n"
		
		output = DirectionOutput()
		output.turn_by_turn_directions = full_directions
		return output	

def get_best_guess_for_city(origin, destination):
	origin_parsed = usaddress.tag(origin)
	destination_parsed = usaddress.tag(destination)
	

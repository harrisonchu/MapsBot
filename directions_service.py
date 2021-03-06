from directions_input_parser import *
import os
import requests

class Directions:
	def __init__(self, is_success, raw_query, directions):
		self.is_success = is_success
		self.raw_query = raw_query
		self.directions = directions

class DirectionsService:
	def __init__(self):
		self.parser = DirectionParser()
		self.maps_api_endpoint = 'https://maps.googleapis.com/maps/api/directions/json'

	def get_directions(self, input):
		query = self.parser.parse_directions_query(input)	
		if not query.is_valid:
			return Directions(False, input, "")

		#got a valid query, start building http request to api
		api_query_string = {}
		api_query_string['key']= os.environ['MAPS_API_KEY']
		api_query_string['origin']= query.origin
		api_query_string['destination'] = query.destination
	
		r = requests.get(self.maps_api_endpoint, api_query_string)
		directions_output = self.parser.parse_directions_output(r.text)
		return directions_output.turn_by_turn_directions

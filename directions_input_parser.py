class DirectionQuery:
	def __init__(self, is_valid, raw_input):
		self.is_valid = is_valid
		self.destination = ""
		self.origin = ""
		self.raw_input = raw_input

class DirectionInputParser:
	def get_direction_query(self, input):
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

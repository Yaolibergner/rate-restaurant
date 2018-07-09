"""Restaurant rating lister."""


# put your code here

def rate_restaurant(file):

	"""Return restaurant rating by alphabetical order."""
	
	restaurant_dict = {}

	with open (file) as rating_file:

		for line in rating_file:
			line = line.rstrip()
			restaurant, score = line.split(":")
			restaurant_dict[restaurant] = score
	
		key_list = sorted(restaurant_dict)

		for restaurant in key_list:
			print("{} is rated at {}.".format(restaurant, restaurant_dict[restaurant]))

rate_restaurant("scores.txt")
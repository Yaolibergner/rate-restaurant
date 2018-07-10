"""Restaurant rating lister."""


# put your code here

def rate_restaurant(file):

	"""Return restaurant rating by alphabetical order."""
	
	restaurant_dict = {}

	with open(file) as rating_file:

		for line in rating_file:
			line = line.rstrip()
			restaurant, score = line.split(":")
			restaurant_dict[restaurant] = score
	
		# key_list = sorted(restaurant_dict)

		# for restaurant in key_list:
		# 	print("{} is rated at {}.".format(restaurant, restaurant_dict[restaurant]))
	return restaurant_dict


def add_ratings():

	"""Add new restaurant and rating to rate_restaurant."""

	restaurant_new_dict = rate_restaurant("scores.txt")

	new_restaurant = input("What's the restaurant name? ").capitalize()
	rating = int(input("What's the restaurant's score? "))

	restaurant_new_dict[new_restaurant] = rating

	key_list = sorted(restaurant_new_dict)

	for new_restaurant in key_list:
		print("{} is rated at {}.".format(new_restaurant, restaurant_new_dict[new_restaurant]))



add_ratings()
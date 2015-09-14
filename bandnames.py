# Band name generator
import random


titles = ["gigantic", "steamy", "gross", "stupid", "ironic", "greasy",
	"tangy", "smelly", "small", "inventive", "spherical", "spiritual", "gren",
	"blue", "pot bellied", "pickled", "prickly"]

adjs = ["tiny", "fat", "shiny", "ecclectic", "fluffy", "bright",
	"corrupt", "aggressive", "alarming", "amazing", "magical",
	"couragous", "fierce", "colorless", "red", "thoughtless",
	"smart", "delirious", "fabulous", "fergalicous", "dangerous"]

plural_nouns = ["apples", "oranges", "kiwis", "clementines", 
	"wildbeasts", "mammoths", "rabbits", "sloths", "spices",
	"eggs", "eggs", "kermits", "cowboys"]

def title():
	return random.choice(titles)

def adj():
	return random.choice(adjs)

def plural_noun():
	return random.choice(plural_nouns)

def main():
	while True:
		name = raw_input("Erik")
		if name == "q":
			break
		random.seed(name)
		print title(), name,"and the", adj(), plural_noun()

main()
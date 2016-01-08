def madlib():
	adjective1 = raw_input("type in adjective: ")
	adjective2 = raw_input("type in adective: ")
	typeofbird = raw_input("type of bird: ")
	roominhouse = raw_input("room in house: ")
	pastverb = raw_input("past tense verb: ")
	verb = raw_input("type in verb: ")
	relname = raw_input("type in relative's name: ")
	noun = raw_input("type in noun: ")
	liquid = raw_input(" a liquid: ")
	ingverb = raw_input("verb ending in -ing: ")
	bodypart = raw_input("body part: ")
	pluralnoun = raw_input(" plural noun: ")
	ingverb2 = raw_input(" ]verb ending in -ing: ")
	noun2 = raw_input(" another noun: ")

	print "it was a " + adjective1 + ", cold November day. I woke up to the " + adjective2 + \
 	" smell of " + typeofbird + " roasting in the " + roominhouse + " downstairs. I " + pastverb + \
  	" down the stairs to see if i could help " + verb + " the dinner. My mom said, 'See if " \
  	+ relname + " needs a fresh " + noun + ".' So I carried a tray of glasses full of " + liquid + \
   	" into the " + ingverb + " room. When i got there, i couldnt believe my " + bodypart + \
    	"! There were " + pluralnoun + " " + ingverb2 + " on the " + noun2 + "!" 
def main():
	while True:
		again = raw_input("Lets play a game! Enter yes/no: ")
			
		if again == "no":
			print ("Thanks for playing!")
			return
		elif again == "yes":
			print ("Lets play again!")
			madlib()
		else:
			print ("Type yes or no")

if __name__=="__main__":
	main()
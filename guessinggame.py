# high low guessing game!

def show_instructions():
	print "Pick a number between 1 and 1000 and i will try to guess it."
	print "I can do this in no more then 10 guesses."
	print "  "
	print "After each guess, enter:"
	print "0  - If i got it right"
	print "-1 - if i guessed too high"
	print "1  - if i guessed to low"

def take_guess(high, low):
	guess ==
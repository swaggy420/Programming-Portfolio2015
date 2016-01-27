#pig game
import random

def roll_dice(sides):
	x = random.randrange(1, sides+1)
	return x

def take_turn(player):
	points = 0
	flag = 1
	print "It's your turn player ",player
	raw_input( "Press enter to begin")
	while flag==1:
		r = roll_dice(6)
		print " You got a" , r
		if r == 1:
			points=0
			flag=0
		else:
			points += r
			print " Your total is" ,points
			y = raw_input("Do you want to continue? y=yes/n=no: ")
			if y == "y":
				flag=1
			else:
				flag=0
	print "Your turn is over"
	return points

def show_instructions():
	print "Welcome to the game of Pig. To win, be the"
	print "player with the most points at the end of "
	print " the game. The game ends at the end of a "
	print "round where at least one player has 100 "
	print "or more points."
	print
	print "On each turn, you may roll the die as many"
	print "times as you like to obtain more points. "
	print "However,if you roll a one, your turn is "
	print "over, and you do not obtain any points that turn."
	print

def main():
	show_instructions()
	p1 = 0
	p2 = 0
	while p1<100 and p2<100:
		print " Player points are:" +str(p1)
		print " Player points are:" +str(p2)
		x = take_turn(1)
		p1 += x
		print " Player points are:" +str(p1)
		print " Player points are:" +str(p2)
		x = take_turn(2)
		p2 += x
		print " The game is over"
		print " Player points are:" +str(p1)
		print " Player points are:" +str(p2)
		if p1>p2 and p1>=100:
			print " Player one is the winner!"
		elif p2>p1 and p2>= 100:
			print " Player two is the winner!"
		else:
			print " Tie game!"

main()
take_turn(1)
take_turn(2)



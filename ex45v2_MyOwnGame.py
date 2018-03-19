#Make your own game

#basic description - game idea
"""
Car Competition
there are 3 cars Skoda, Nissan and Audi competing in tournament consisting
of 5 races. You need to choose your car and throw dice to compete.
You can also bet each race which car wins.
For each race there are points distributed based on highest rank of dice points:
5 points for winner, 3 points for 2nd runner and 2 points for loser.
Sum of points at the end of tournament determines ranking of cars.

"""
#1 start with Design
#2 basic game concept see in version 1

#!!task: if 2 or 3 cars roll the same points of dice, adjust points distribution
from sys import exit
from random import randint

#Game Engine to play 
# class Engine (object):
	# print "**22 start engine class**"
	# def __init__(self,race_map):
		# print "**26 start engine init**"
		# self.race_map = race_map
	
	# def play (self):
		# print "**26 start playing function**"
		# self.current_race = self.race_map.opening_race()
		# self.last_race = self.race_map.next_race("results")

		# while self.current_race != self.last_race:
			# print "**31 changing race class**"
			# self.next_race_name = self.current_race.__init__()
			# self.current_race = self.race_map.next_race(self.next_race_name)
		
		# #be sure to launch the last scene:
		# self.current_race.__init__()
						
class Tournament(object):
	def __init__(self):
		#print "**43 start tour init**"
		self.cars = ["Skoda", "Nissan", "Audi"]
		
		#define score list with attributes [order,car,player,race score,tour points]
		global score
		score = [[1,"Skoda ", "Speedy G   ", 0, 0],
		[2,"Nissan", "Fast Bunny ", 0 , 0],[3,"Audi  ", "Flying Bird", 0, 0]]
		
		print "\n Get ready, game is starting..."
		#add Tournament description / rules / points etc.
		print "\n Car Competition \n This is a new car tournament consisting"
		print "of 5 races. You need to choose your car and throw dice to compete."
		print "There are 3 cars racing:\n"
		print "\n".join(self.cars)
		
		self.car_choice()
		
	def car_choice(self):
		#print "**56 start car choice**"
		self.car_spelling = [
		"Skoda","skoda","s","Nissan","nissan","n","Audi","audi","a"]
		self.correct = 0
		global player_car
		player_car = ""
		
		while self.correct < 1:
			player_choice = raw_input ("Choose your car:")
	
			if player_choice in self.car_spelling:
				self.correct = 1
			else:
				print "Misspelled. Please, type the car name correctly."
	
		if player_choice in self.car_spelling[0:3]:
			player_car = "Skoda"
			score[0][2] = "You, Racer "
		elif player_choice in self.car_spelling[3:6]:
			player_car = "Nissan"
			score[1][2] = "You, Racer "
		elif player_choice in self.car_spelling[6:9]:
			player_car = "Audi"
			score[2][2] = "You, Racer "
	
		print "\n OK. so you will race with %s. \n" % (player_car)
		print "Let`s start the game:\n"
		
		#go to the Race No. 1
		#return "race_no_1"
				
#Race class for 5 Races with description and dice rolling
class RaceNo1 (Tournament):
	def __init__(self):
		print "**Welcome to the Race No 1!**"	
		self.roll_and_race()
		pass
	
	#iter method makes an object iterable, i.e. can make next object instance
	#(needed for use of sorted function or for loop)	
	def __iter__ (self):
		return iter(self.list)
	
	def roll_and_race (self):
		#print "**122 point Race start**"		
		raw_input ("Roll the dice: (hit 'Enter' or press any key)")
		
		skoda_dice = randint(1,6)
		nissan_dice = randint(1,6)
		audi_dice = randint(1,6)
		
		if player_car == "Skoda":
			player_dice = skoda_dice
		elif player_car == "Nissan":
			player_dice = nissan_dice
		elif player_car == "Audi":
			player_dice = audi_dice
		else: print "Something went wrong?"
		
		print "\n You have got %s!\n" % player_dice
		
		#add score from dice to cars in list, 5th member reserved for points	
		global score
		score = sorted(score, key=lambda x: x[0])
		score[0][3] = skoda_dice
		score[1][3] = nissan_dice
		score[2][3] = audi_dice
					
		max_sub = max(score, key=lambda x: x[3])
		max_val = max_sub[3]
		#max_index = max_sub[0]
		#print max_sub
		#print max_val, max_index
				
		raw_input ("Who wins? (hit 'Enter' or press any key)")
		
		print "\n The winner got", max_val
		"""
		print "And the winner is...\n\n   ", max_index, "!!!"
		print "\n    Wooooow!\n"
		print "just checking:", score
		"""
		print 30*"-"
		
		raw_input ("press key to get the winner...")
		
		#call result function to sort cars and choose the winner
		self.result()
		
	def result (self):
		global score
		score = sorted(score, key=lambda x: x[3], reverse = True)
		
		#check what-if 2 or 3 cars roll the same points of dice		
		if score [0][3] > score [1][3]:
			winner = score [0][1]
		elif score [1][3] > score [2][3]:
			winner = "%s and %s" % (score [0][1],score [1][1])
		else:
			winner = "All racers won within the same time!!!"
		
		#print "\n Score: ", score
		#print "\n Result Table:", score
		print "\n\n The winner is:\t %s \n" % winner
		
		print "\n\t Race result table:\n "
		print "\t 1.", score [0][2], "  ", score[0][1], "  ", score [0][3]
		print "\t 2.", score [1][2], "  ", score[1][1], "  ", score [1][3]
		print "\t 3.", score [2][2], "  ", score[2][1], "  ", score [2][3], "\n\n"
		
		#print "check score>", score
		
		#call ranking function to add points
		self.ranking()
		
	def ranking(self):	
		global score
		
		#print "score ranking check>",score
		#reward points to cars/players based on last result
		score[0][4] += 5
		score[1][4] += 3
		score[2][4] += 2

		#print "points added check>",score
		#sort based on points achieved
		score = sorted(score, key=lambda x: x[4], reverse = True)
		print 30*"-"
		print "\n\t Tournament ranking table:\n "
		print "\t 1.", score [0][2], "  ", score[0][1], "  ", score [0][4], "points"
		print "\t 2.", score [1][2], "  ", score[1][1], "  ", score [1][4], "points"
		print "\t 3.", score [2][2], "  ", score[2][1], "  ", score [2][4], "points\n\n"
		
class RaceNo2 (RaceNo1):
	
	def __init__(self):
		print "**Welcome to the Race No 2!**"
		self.roll_and_race()		

	#check how to get points from last race into score list	instead 0
	#def result - modify
		
class RaceNo3 (RaceNo1):
	
	def __init__(self):
		print "**Welcome to the Race No 3!**"
		self.roll_and_race()	

class RaceNo4 (RaceNo1):
	
	def __init__(self):
		print "**Welcome to the Race No 4!**"
		self.roll_and_race()		

class RaceNo5 (RaceNo1):
	
	def __init__(self):
		print "\n\t**Welcome to the Race No 5, Le Grand Prix!**"
		print "\n\t(**D o u b l e  R e w a r d s**)\n"
		self.roll_and_race()		
	
	def ranking(self):	
		global score
		#print "score ranking check>",score
		#reward points to cars/players based on last result
		score[0][4] += 10
		score[1][4] += 6
		score[2][4] += 4

		#print "points added check>",score
		#sort based on points achieved
		score = sorted(score, key=lambda x: x[4], reverse = True)
		print "\n\tTa daaa!"
		print "\t...and the winner is: ***", score [0][2], "***!!! Congratulations!!!"
		print "\n\t ***Tournament final ranking table***\n "
		print "\t 1.", score [0][2], "  ", score[0][1], "  ", score [0][4], "points"
		print "\t 2.", score [1][2], "  ", score[1][1], "  ", score [1][4], "points"
		print "\t 3.", score [2][2], "  ", score[2][1], "  ", score [2][4], "points\n\n"
					
class Finish (object):
	#print "195**pass through class Finish**"
	def __init__(self):
		#print "203**start class Finish init**"
		print "\tThis is the end of game. Good bye!"
		
#Map for transfer from one race to another
class Map (object):
	#print "200**pass through class Map**"
	races = {
			"tournament" : Tournament(),
			"race_no_1"  : RaceNo1(),
			"race_no_2"  : RaceNo2(),
			"race_no_3"  : RaceNo3(),
			"race_no_4"  : RaceNo4(),
			"race_no_5"  : RaceNo5(),
			"finish"     : Finish()
	}
	
	def __init__(self, start_race):
		#print "**220 start class Map init**"
		self.start_race = start_race

	# def next_race(self, race_name):
		# val = Map.races.get(race_name)
		# return val

	# def opening_race(self):
		# return self.next_race(self.start_race)

	# print "221** before game_start**"		
game_start = Map("tournament")
#print "**217 game_start:", game_start
#game = Engine(game_start)
#print "**219 game:", game
#game.play()
#welcome = Tournament()
#welcome.__init__()
#print "227**endline touch**"


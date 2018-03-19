#Ex48 Lexicon and advanced input scanner

def convert_numbers(s):
	try:
		return int(s)
	except ValueError:
		return None	

def scan(stuff):
	words = stuff.split()
	directions = ['east','west','north','south', 'down', 'up', 'left', 'right', 'back']
	verbs = ['go', 'stop', 'kill', 'eat']
	stops = ['the', 'in', 'of', 'from', 'at', 'it']
	nouns = ['door', 'bear', 'princess', 'cabinet']
	scanned = []
	
	for i in words:
		if i in directions:
			scanned.append (('direction', i))
		elif i in verbs:
			scanned.append (('verb', i))
		elif i in stops:
			scanned.append (('stop', i))
		elif i in nouns:
			scanned.append (('noun', i))
		elif convert_numbers(i) != None:
			integer = convert_numbers(i)
			scanned.append (('number', integer))
		else:
			scanned.append (('error', i))
					
	return scanned

print "Hello pal!\nWrite me your sentence:"
stuff = raw_input ('> ')
result = scan(stuff)
print result

# def scan (stuff):
	# #stuff = raw_input ('> ')
	# stuff = "north"
	# words = stuff.split()
	# directions = ['east','west','north','south']
	# first_word = ('direction', 'north')
	# second_word = ('verb', 'go')
	# sentence = [first_word, second_word]
	# lexicon = {}
	
	

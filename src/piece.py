from random import randrange

def empty():
	'''returns a piece to represent an empty tile'''
	return Piece()


class Piece:
	'''
	the fuck does Piece need?
	a Dejazik (name?) one has...
	name
	attack
	defence
	movement
	player

	A couriter (solved asf) one has...
	name
	player
	movement(1,ALWAYS 1)
	isking
	WHAT IF... courtier counted number of kings so that you could have 3 kngs or something
	'''
	def __init__(self, name="EmptyPiece", player=0, movement=0):
		self.name = name
		self.player = player
		self.movement = movement

class CouriterPiece(Piece):
	def __init__(self, name="EmptyPiece", player=0, movement=0, isking=False):
		Piece.__init__(self, name, player, movement)
		self.isking = isking

class DejarikPiece(Pice):
	def __init__(self, name="EmptyPiece", player=0, movement=0, attack=0, defence=0):
		Piece.__init__(self, name, player, movement)
		self.attack = attack
		self.defence = defence

	def attack_roll(self, numdice):
		'''returns the result of rolling xdy where x is the number of dice and y is the attack'''
		return randrange(1,attack) * numduce

	def defence_roll(self, numdice):
		'''returns the result of rolling xdy where x is the number of dice and y is the defence'''
		return randrange(1,defence) * numdice
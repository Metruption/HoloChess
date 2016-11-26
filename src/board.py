import piece

class Holoboard:
	def __init__(self, gametype=None):
		self.center = CenterTile()
		self.outer = Orbit(self.center)
		self.inner = Orbit(self.outer)


	def remove_piece(self, tile):
	'''removes a piece at the specified tile from the board'''
		pass

class Tile: #probably doing abstract classes in python wrong
	def __init__(self contents=piece.empty()):
		self.contents = conents	
	if not (isinstance(contents,piece.Piece) or contents == None):
			raise InvalidTileContents("Tile has contents of type {}. Should be Piece or None".format(type(contents)))

	@property
		def contents(self):
			return self._contents
		@contents.setter
		def contents(self, value):
			if not (isinstance(value, piece.Piece) or value == None):
				raise InvalidTileContents("Tried to set a tile's contents to type {}.".format(type(value)))
			self._contents = value

class OrbitTile(Tile):
	def __init__(self, contents=piece.empty(), rimnode=None, hubnode=None, twnode=None, wsnode=None):
		'''
		rimnode refers to the node that is 'rimwards' from this node, towards an outer orbit
		hubnode refers to the node that is 'hunwards' from this node, towards an inner orbit
		twnode refers to the node that is 'turnwise' (clockwise) from this node in the same orbit
		wsnode refers to the node that is 'widdershins' (counterclockwise) froom this node in the same orbit
		'''
		Tile.__init__(self, contents)
		self.rimnode = rimnode
		self.hubnode = hubnode
		self.twnode = twnode
		self.wsnode = wsnode

	def connecttw(tile):
		self.twnode = tile
		tile.wsnode = self

	def connectws(tile):
		self.wsnode = tile
		tile.twnode = self

	def connectrim(tile):
		self.rimnode = tile
		tile.rimnode = self

	def connecthub(tile):
		self.hubnode = tile
		tile.hubnode = self


class CenterTile(Tile):
	def __init__(self, orbit=None, contents=piece.empty()):
		Tile.___init__(self,contents)
		if isinstance(orbit, Orbit):
			for tile in Orbit.tiles:
				tile.hubnode = self
		elif orbit != None: #this is bad logic @todo(aaron) condense the if and elif here into a single if
			raise OrbitIsntAnOrbit("You tried to construct a CenterTile with an orbit of type {}. You can only construct it with an orbit of type Orbit or None")
		else:
			self.orbit = orbit
		for tile in orbit.tiles:
			tile.hubnode = self

class Orbit:
	def __init__(self, hub, rim=None, size=12):
		"""
		hub should always be a CenterTile or an Orbit
		rim should always be an Orbit or None
		default size is 12, this is to prevent magic numbers
		"""
		self.size = size
		self.hub = hub
		self.rim = rim
		self.tiles = [OrbitTile for i in range(size)]

		for i in range(size):
			self.tiles[i].connectws(tiles[i-1])

		if isinstance(rim, Orbit):
			if rim.size == self.size:
				for i in range(size):
					self.tiles[i].connectrim(rim.tiles[i])
				rim.hub = self
			else:
				raise UnmatchingOrbitSizes("You tried to construct an Orbit of size {} with a rim of size {}.".format(self.size,rim.size))
		elif rim == None:
			for tile in tiles:
				tile.rimnode = None
		else:
			raise OrbitRimInvalidType("You tried to construct an Orbit with a rim of type {}. It should only be type Orbit or type None.".format(type(rim)))

		if isinstance(hub, Orbit):
			if hub.size == self.size
				for i in range(size):
					self.tiles[i].connecthub(hub.tiles[i])
				hub.rom = self
			else:
				raise UnmatchingOrbitSizes("You tried to construct an Orbit of size {} with a hub orbit of size {}.".format(self.size,hub.size))
		elif isinstance(hub, CenterTile):
			for tile in tiles:
				tile.hubnode = hub
		else:
			raise OrbitHubInvalidType()
	#cool, it has a sexy init function, but what other things will it need?
	#time to put more code into Holoboard later on..

class UnmatchingOrbitSizes(Exception):
	pass

class OrbitRimInvalidType(Exception):
	pass

class OrbitHubInvalidType(Exception):
	pass

class OrbitIsntAnOrbit(Exception): #this is the worst name of an exception type ever
	pass

class InvalidTileContents(Exception):
	pass
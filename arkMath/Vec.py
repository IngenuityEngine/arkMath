# standard libraries
import math
import re

# monkey patch the json encoder
# because it has no way to
# encode custom classes
# https://stackoverflow.com/questions/18478287/making-object-json-serializable-with-regular-encoder
from json import JSONEncoder

# new _default function to use
def _default(self, obj):
    return getattr(obj.__class__, '__json__', _default.default)(obj)

# save unmodified default
_default.default = JSONEncoder().default
# overwrite with it's replacement
JSONEncoder.default = _default

class Vec(object):

	def __init__(self, x=0, y=0, z=0, w=0):
		# handle string input (turn to list)
		if isinstance(x, str):
			x = self.parseString(x)

		# handle list, tupple, etc inputs
		try:
			x[:0]
		except TypeError:
			# not a list
			pass
		else:
			y = x[1]
			if len(x) > 2:
				z = x[2]
			if len(x) > 3:
				w = x[3]
			x = x[0]

		# validate input
		if not all([isinstance(x, float) or isinstance(x, int),
			isinstance(y, float) or isinstance(y, int),
			isinstance(z, float) or isinstance(z, int),
			isinstance(w, float) or isinstance(w, int)]):
			raise Exception('Invalid input')

		# set values
		self.vec = [x, y, z, w]
		self.setX(x)
		self.setY(y)
		self.setZ(z)
		self.setW(w)

	def parseString(self, vecString):
		vecString = re.sub(r'[^0-9\.\,\-]', '', vecString)
		parts = vecString.split(',')
		if len(parts) > 1:
			return [float(x) for x in parts]
		raise Exception('Invalid string: ' + vecString)

	def setFromString(self, vecString):
		numbers = self.parseString(vecString)
		self.setFromList(numbers)

	def setFromList(self, numbers):
		for i, n in enumerate(numbers):
			self[i] = n

	def equals(self, vec):
		return ((self.x == vec.x) and (self.y == vec.y) and (self.z == vec.z) and (self.w == self.w))

	def length(self):
		return math.sqrt(
			self.x * self.x +
			self.y * self.y +
			self.z * self.z +
			self.w * self.w)

	def angle(self, vec):
		# In radians, because math.
		return math.acos(self.dot(vec) / self.length() / vec.length())

	def dot(self, vec):
		self.updateVec()
		return sum(x * y for x, y in zip(self.vec, vec.vec))

	def cross(self, vec):
		# Cross product is not really defined in 4 dimensions.
		# This uses only x,y,z.
		return Vec(
			self.y * vec.z - vec.y * self.z,
			self.z * vec.x - vec.z * self.x,
			self.x * vec.y - vec.x * self.y,
			0)

	def linearCombination(self, coefficients):
		self.updateVec()
		if isinstance(coefficients, list):
			if len(coefficients) == 4:
				return Vec([x*i for x, i in zip(self.vec, coefficients)])

	def normalize(self):
		# same as divide, tiniest of optimizations
		lengthMult = 1 / self.length()
		return Vec(
			self.x * lengthMult,
			self.y * lengthMult,
			self.z * lengthMult,
			self.w * lengthMult)

	def add(self, vec):
		return Vec(
			self.x + vec.x,
			self.y + vec.y,
			self.z + vec.z,
			self.w + vec.w)

	def subtract(self, vec):
		return Vec(
			self.x - vec.x,
			self.y - vec.y,
			self.z - vec.z,
			self.w - vec.w)

	def multiply(self, num):
		return Vec(self.x * num, self.y * num, self.z * num, self.w * num)

	def negate(self):
		return Vec(-1 * self.x, -1 * self.y, -1 * self.z, -1 * self.w)

	def min(self):
		self.updateVec()
		return min(self.vec)

	def max(self):
		self.updateVec()
		return max(self.vec)

	def setVec(self, x, y, z, w = 0):
		self.x = self.r = self.h = self.vec[0] = x
		self.y = self.g = self.s = self.vec[1] = y
		self.z = self.b = self.v = self.vec[2] = z
		if w:
			self.w = w

	def getVec(self):
		return [self.x, self.y, self.z, self.w]

	def setX(self, x):
		self.x = self.r = self.h = self.vec[0] = x

	def setY(self, y):
		self.y = self.g = self.s = self.vec[1] = y

	def setZ(self, z):
		self.z = self.b = self.v = self.vec[2] = z

	def setW(self, w):
		self.w = self.a = self.vec[3] = w

	def setR(self, r):
		self.setX(r)

	def setG(self, g):
		self.setY(g)

	def setB(self, b):
		self.setZ(b)

	def setA(self, a):
		self.setW(a)

	def setH(self, h):
		self.setX(h)

	def setS(self, s):
		self.setY(s)

	def setV(self, v):
		self.setZ(v)

	def updateVec(self):
		self.vec = [self.x, self.y, self.z, self.w]
		self.setX(self.x)
		self.setY(self.y)
		self.setZ(self.z)
		self.setW(self.w)

	def __setitem__(self, index, value):
		if index == 0 or \
			index == 'x' or \
			index == 'r' or \
			index == 'h':
			self.setX(value)
		elif index == 1 or \
			index == 'y' or \
			index == 'g' or \
			index == 's':
			self.setY(value)
		elif index == 2 or \
			index == 'z' or \
			index == 'b' or \
			index == 'v':
			self.setZ(value)
		elif index == 3 or \
			index == 'w' or \
			index == 'a':
			self.setW(value)
		else:
			raise Exception('No index')

	def __getitem__(self, index):
		if index == 0 or index == 'x' or index == 'r':
			return self.x
		elif index == 1 or index == 'y' or index == 'g':
			return self.y
		elif index == 2 or index == 'z' or index == 'b':
			return self.z
		elif index == 3 or index == 'w' or index == 'a':
			return self.w
		else:
			raise Exception('Invalid index')

	def __mul__(self, other):
		if isinstance(other, Vec):
			return self.dot(other)
		elif isinstance(other, (float, int)):
			return self.multiply(other)
		else:
			return NotImplemented

	def __rmul__(self, other):
		if isinstance(other, Vec):
			return self.dot(other)
		elif isinstance(other, float) or isinstance(other, int):
			return self.multiply(other)
		else:
			return NotImplemented

	def __add__(self, other):
		if isinstance(other, Vec):
			return self.add(other)
		else:
			return NotImplemented

	def __sub__(self, other):
		if isinstance(other, Vec):
			return self.subtract(other)
		else:
			return NotImplemented

	def __str__(self):
		self.updateVec()
		return str(self.vec)

	def __json__(self):
		self.updateVec()
		return self.vec

	def __eq__(self, other):
		if isinstance(other, Vec):
			return self.equals(other)
		else:
			return NotImplemented

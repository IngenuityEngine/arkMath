
# Standard modules
from expects import *

# Our modules
import arkInit
arkInit.init()

import tryout
import arkMath
import json

class test(tryout.TestSuite):
	title = 'test/test_vec.py'

	def init(self):
		vec = arkMath.Vec(1,2,3,4)
		self.assertEqual(vec.x, 1)
		self.assertEqual(vec.y, 2)
		self.assertEqual(vec.z, 3)
		self.assertEqual(vec.w, 4)

		self.assertEqual(vec.r, 1)
		self.assertEqual(vec.g, 2)
		self.assertEqual(vec.b, 3)
		self.assertEqual(vec.a, 4)

		self.assertEqual(vec.h, 1)
		self.assertEqual(vec.s, 2)
		self.assertEqual(vec.v, 3)
		self.assertEqual(vec.a, 4)

	def create_from_string(self):
		vec = arkMath.Vec('(0.5, 0.637, 1)')
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)

		vec = arkMath.Vec('(0.5, 0.637, 1, .2)')
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, .2)

		vec = arkMath.Vec('( 0.5,  -.637,   1,  .2  )')
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, -0.637)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, .2)

	def set_from_string(self):
		vec = arkMath.Vec()
		vec.setFromString('(0.5, 0.637, 1)')
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)

		vec = arkMath.Vec()
		vec.setFromString('( 0.5,  -0.637,   1,  .2  )')
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, -0.637)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, .2)

	def set_from_list(self):
		vec = arkMath.Vec()
		vec.setFromList([0.5, 0.637, 1])
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)

		vec = arkMath.Vec()
		vec.setFromList([ 0.5,  0.637,   1,  .2  ])
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, .2)

	def set_from_tuple(self):
		vec = arkMath.Vec()
		vec.setFromList((0.5, 0.637))
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)

		vec = arkMath.Vec()
		vec.setFromList(( 0.5,  0.637,   1,  .2  ))
		self.assertEqual(vec.x, .5)
		self.assertEqual(vec.y, .637)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, .2)

	def serialize(self):
		vec = arkMath.Vec(1,0.5, 0.637, 1)
		print 'vec:', vec
		x = json.dumps(vec)
		self.assertEqual(x, '[1, 0.5, 0.637, 1]')
		data = json.loads(x)
		self.assertEqual(data, [1, 0.5, 0.637, 1])

	def math(self):
		# fix: laughable coverage
		vec = arkMath.Vec(1,0,0,0)
		self.assertEqual(vec.length(), 1)
		vec *= 12
		self.assertEqual(vec.x, 12)
		vec = vec.normalize()
		self.assertEqual(vec.x, 1)
		vec += arkMath.Vec(1,1,1,1)
		self.assertEqual(vec.x, 2)
		self.assertEqual(vec.y, 1)
		self.assertEqual(vec.z, 1)
		self.assertEqual(vec.w, 1)

if __name__ == '__main__':
	tryout.run(test)

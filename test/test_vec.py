
# Standard modules
from expects import *

# Our modules
import arkInit
arkInit.init()

import tryout
import arkMath

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

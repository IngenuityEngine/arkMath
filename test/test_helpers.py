
# Standard modules
from expects import *

# Our modules
import arkInit
arkInit.init()

import tryout
import arkMath

class test(tryout.TestSuite):
	title = 'test/test_vec.py'

	def is_vector(self):
		vec = arkMath.Vec(1,2,3,4)
		self.assertEqual(arkMath.isVector(vec), True)
		self.assertEqual(arkMath.isVector(12), False)

	def ensure_vector(self):
		vec = arkMath.Vec(1,2,3,4)
		ensured = arkMath.ensureVector(vec)
		self.assertEqual(ensured.x, vec.x)

		ensured = arkMath.ensureVector(12)
		self.assertEqual(ensured.x, 12)
		self.assertEqual(ensured.y, 0)

		ensured = arkMath.ensureVector(12, 5, 4, 9)
		self.assertEqual(ensured.x, 12)
		self.assertEqual(ensured.y, 5)
		self.assertEqual(ensured.z, 4)
		self.assertEqual(ensured.w, 9)

		ensured = arkMath.ensureVector([15, 25, 7, 2])
		self.assertEqual(ensured.x, 15)
		self.assertEqual(ensured.y, 25)
		self.assertEqual(ensured.z, 7)
		self.assertEqual(ensured.w, 2)


if __name__ == '__main__':
	tryout.run(test)

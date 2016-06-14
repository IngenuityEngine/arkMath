
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
		self.assertEqual(arkMath.isVector(vec), True)
		self.assertEqual(arkMath.isVector(12), False)

if __name__ == '__main__':
	tryout.run(test)

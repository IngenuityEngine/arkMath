
# Standard modules
from expects import *

# Our modules
import arkInit
arkInit.init()

import tryout
import arkMath
from arkMath import Mat44

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

	def is_matrix(self):
		matList = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
		matFromList = Mat44(matList)
		vec1 = arkMath.Vec(1.0, 0.0, 0.0, 0.0)
		vec2 = arkMath.Vec(0.0, 1.0, 0.0, 0.0)
		vec3 = arkMath.Vec(0.0, 0.0, 1.0, 0.0)
		vec4 = arkMath.Vec(0.0, 0.0, 0.0, 1.0)
		matFromVecs = Mat44(vec1, vec2, vec3, vec4)
		justVec = arkMath.Vec(1, 2, 3, 4)

		self.assertEqual(arkMath.isMatrix(matFromList), True)
		self.assertEqual(arkMath.isMatrix(matFromVecs), True)
		self.assertEqual(arkMath.isMatrix(justVec), False)

	# Should work if input already a matrix, 4 vectors, or 16 matrix values
	def ensure_matrix(self):
		matList = [1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0]
		goalMat = Mat44(matList)

		sixteenMat = arkMath.ensureMatrix(1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 1.0)
		self.assertEqual(type(sixteenMat), type(goalMat))

		vec1 = arkMath.Vec(1.0, 0.0, 0.0, 0.0)
		vec2 = arkMath.Vec(0.0, 1.0, 0.0, 0.0)
		vec3 = arkMath.Vec(0.0, 0.0, 1.0, 0.0)
		vec4 = arkMath.Vec(0.0, 0.0, 0.0, 1.0)

		vecsMat = arkMath.ensureMatrix(vec1, vec2, vec3, vec4)
		self.assertEqual(type(vecsMat), type(goalMat))

		# Ensure_matrix of already matrix should just return itself
		selfMat = arkMath.ensureMatrix(goalMat)
		self.assertEqual(type(selfMat), type(goalMat))

if __name__ == '__main__':
	tryout.run(test)

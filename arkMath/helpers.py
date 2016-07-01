
import Vec
import Mat44

def isVector(testVec):
	return isinstance(testVec, Vec.Vec)

def ensureVector(x, y=0, z=0, w=0):
	if isVector(x):
		return x
	else:
		return Vec.Vec(x, y, z, w)

# TODO: add to test_helpers.py with isMatrix and ensureMatrix

# Ensure testMat is a Mat44 matrix (4 row Vec4s)
def isMatrix(testMat):
	return isinstance(testMat, Mat44.Mat44)

# Ensure matrix, either a Mat44 object, 4 row Vec4s, 16 matrix values
zero =  Vec.Vec(0, 0, 0, 0)
def ensureMatrix(row0x, row0y=zero, row0z=zero, row0w=zero,
		row1x=zero, row1y=zero, row1z=zero, row1w=zero,
		row2x=zero, row2y=zero, row2z=zero, row2w=zero,
		row3x=zero, row3y=zero, row3z=zero, row3w=zero):
	if isMatrix(row0x):
		return row0x
	elif isVector(row0x) and isVector(row0y) and isVector(row0z) and isVector(row0w):
		return Mat44.Mat44(row0x, row0y, row0z, row0w)
	elif isinstance(row0x, list):
		return Mat44.Mat44(row0x)
	else:
		return Mat44.Mat44(row0x, row0y, row0z, row0w, row1x, row1y, row1z, row1w, row2x, row2y, row2z, row2w, row3x, row3y, row3z, row3w)
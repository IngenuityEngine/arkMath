
import Vec

def isVector(testVec):
	return isinstance(testVec, Vec.Vec)

def ensureVector(x, y=0, z=0, w=0):
	if isVector(x):
		return x
	else:
		return Vec.Vec(x, y, z, w)

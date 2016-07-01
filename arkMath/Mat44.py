import math
from Vec import Vec

class Mat44(object):

	def __init__(self,
		row0x=1.0, row0y=0.0, row0z=0.0, row0w=0.0,
		row1x=0.0, row1y=1.0, row1z=0.0, row1w=0.0,
		row2x=0.0, row2y=0.0, row2z=1.0, row2w=0.0,
		row3x=0.0, row3y=0.0, row3z=0.0, row3w=1.0):

		if isinstance(row0x, list):
			if len(row0x) == 16:
				self.row0 = Vec(row0x[0], row0x[1], row0x[2], row0x[3])
				self.row1 = Vec(row0x[4], row0x[5], row0x[6], row0x[7])
				self.row2 = Vec(row0x[8], row0x[9], row0x[10], row0x[11])
				self.row3 = Vec(row0x[12], row0x[13], row0x[14], row0x[15])
				self.col0 = Vec(row0x[0], row0x[4], row0x[8], row0x[12])
				self.col1 = Vec(row0x[1], row0x[5], row0x[9], row0x[13])
				self.col2 = Vec(row0x[2], row0x[6], row0x[10], row0x[14])
				self.col3 = Vec(row0x[3], row0x[7], row0x[11], row0x[15])
		elif isinstance(row0x, Vec) and isinstance(row0y, Vec) and isinstance(row0z, Vec) and isinstance(row0w, Vec):
			self.row0 = row0x
			self.row1 = row0y
			self.row2 = row0z
			self.row3 = row0w
		else:
			self.row0 = Vec(row0x, row0y, row0z, row0w)
			self.row1 = Vec(row1x, row1y, row1z, row1w)
			self.row2 = Vec(row2x, row2y, row2z, row2w)
			self.row3 = Vec(row3x, row3y, row3z, row3w)
		self.mat = [self.row0.x, self.row0.y, self.row0.z, self.row0.w,
		self.row1.x, self.row1.y, self.row1.z, self.row1.w,
		self.row2.x, self.row2.y, self.row2.z, self.row2.w,
		self.row3.x, self.row3.y, self.row3.z, self.row3.w]

	def getRow(self, index):
		if index == 0:
			return self.row0
		elif index == 1:
			return self.row1
		elif index == 2:
			return self.row2
		elif index == 3:
			return self.row3
		else:
			raise Exception('Invalid index')

	def getCol(self, index):
		self.updateMat()
		return Vec([self.mat[4*i + index] for i in xrange(4)])

	def setRow(self, index, vec):
		self.updateMat()
		if index == 0:
			self.row0 = vec
		elif index == 1:
			self.row1 = vec
		elif index == 2:
			self.row2 = vec
		elif index == 3:
			self.row3 = vec
		self.mat[index*4], self.mat[index*4 + 1], self.mat[index*4 + 2], self.mat[index*4 + 3] = vec.x, vec.y, vec.z, vec.w

	def updateRowVec(self, index, value):
		if index == 0:
			self.row0.x = value
		elif index == 1:
			self.row0.y = value
		elif index == 2:
			self.row0.z = value
		elif index == 3:
			self.row0.w = value
		elif index == 4:
			self.row1.x = value
		elif index == 5:
			self.row1.y = value
		elif index == 6:
			self.row1.z = value
		elif index == 7:
			self.row1.w = value
		elif index == 8:
			self.row2.x = value
		elif index == 9:
			self.row2.y = value
		elif index == 10:
			self.row2.z = value
		elif index == 11:
			self.row2.w = value
		elif index == 12:
			self.row3.x = value
		elif index == 13:
			self.row3.y = value
		elif index == 14:
			self.row3.z = value
		elif index == 15:
			self.row3.w = value
		else:
			raise Exception('invalid index')

	def transpose(self):
		self.updateMat()
		return Mat44([self.mat[row*4 + col] for col in range(4) for row in range(4)])

	def updateMat(self):
		self.mat = [self.row0.x, self.row0.y, self.row0.z, self.row0.w,
		self.row1.x, self.row1.y, self.row1.z, self.row1.w,
		self.row2.x, self.row2.y, self.row2.z, self.row2.w,
		self.row3.x, self.row3.y, self.row3.z, self.row3.w]
		self.row0 = Vec(self.row0.x, self.row0.y, self.row0.z, self.row0.w)
		self.row1 = Vec(self.row1.x, self.row1.y, self.row1.z, self.row1.w)
		self.row2 = Vec(self.row2.x, self.row2.y, self.row2.z, self.row2.w)
		self.row3 = Vec(self.row3.x, self.row3.y, self.row3.z, self.row3.w)

	def vectorMatrixMul(self, vec):
		if not isinstance(vec, Vec):
			raise Exception('invalid type: must be Vec')
		return Vec([vec*self.getCol(i) for i in range(4)])

	def matrixVectorMul(self, vec):
		if not isinstance(vec, Vec):
			raise Exception('invalid type: must be Vec')
		return Vec([vec*self.getRow(i) for i in range(4)])

	def matrixMatrixMul(self, mat):
		self.updateMat()
		# Assume self is left matrix.
		if not isinstance(mat, Mat44):
			raise Exception('invalid type: must be Mat44')
		return Mat44([self.getRow(i)*mat.getCol(j) for i in range(4) for j in range(4)])

	def scalarMul(self, alpha):
		self.updateMat()
		return Mat44([x*alpha for x in self.mat])

	# TODO: HERE
	def add(self, mat):
		return Mat44(self.x + mat.x, self.y + mat.y, self.z + mat.z, self.w + mat.w)

	def subtract(self, mat):
		return self + mat.scalarMul(-1)

	def determinant(self):
		return self[0,0]*self[1,1]*self[2,2]*self[3,3] + self[0,0]*self[1,2]*self[2,3]*self[3,1] + \
		self[0,0]*self[1,3]*self[2,1]*self[3,2] + self[0,1]*self[1,0]*self[2,3]*self[3,2] + \
		self[0,1]*self[1,2]*self[2,0]*self[3,3] + self[0,1]*self[1,3]*self[2,2]*self[3,0] + \
		self[0,2]*self[1,0]*self[2,1]*self[3,3] + self[0,2]*self[1,1]*self[2,3]*self[3,0] + \
		self[0,2]*self[1,3]*self[2,0]*self[3,1] + self[0,3]*self[1,0]*self[2,2]*self[3,1] + \
		self[0,3]*self[1,1]*self[2,0]*self[3,2] + self[0,3]*self[1,2]*self[2,1]*self[3,0] - \
		self[0,0]*self[1,1]*self[2,3]*self[3,2] - self[0,0]*self[1,2]*self[2,1]*self[3,3] - \
		self[0,0]*self[1,3]*self[2,2]*self[3,1] - self[0,1]*self[1,0]*self[2,2]*self[3,3] - \
		self[0,1]*self[1,2]*self[2,3]*self[3,0] - self[0,1]*self[1,3]*self[2,0]*self[3,2] - \
		self[0,2]*self[1,0]*self[2,3]*self[3,1] - self[0,2]*self[1,1]*self[2,0]*self[3,3] - \
		self[0,2]*self[1,3]*self[2,1]*self[3,0] - self[0,3]*self[1,0]*self[2,1]*self[3,2] - \
		self[0,3]*self[1,1]*self[2,2]*self[3,0] - self[0,3]*self[1,2]*self[2,0]*self[3,1]

	def inverse(self):
		# Loop unrolling for lightning fast speed.
		# And because I couldn't figure out an easy way to loop it...
		inverse = []
		append = inverse.append

		append(self.mat[5] * self.mat[10] * self.mat[15] - \
		self.mat[5] * self.mat[11] * self.mat[14] - \
		self.mat[9] * self.mat[6] * self.mat[15] + \
		self.mat[9] * self.mat[7] * self.mat[14] + \
		self.mat[13] * self.mat[6] * self.mat[11] - \
		self.mat[13] * self.mat[7] * self.mat[10])

		append(-self.mat[1] * self.mat[10] * self.mat[15] + \
		self.mat[1] * self.mat[11] * self.mat[14] + \
		self.mat[9] * self.mat[2] * self.mat[15] - \
		self.mat[9] * self.mat[3] * self.mat[14] - \
		self.mat[13] * self.mat[2] * self.mat[11] + \
		self.mat[13] * self.mat[3] * self.mat[10])

		append(self.mat[1] * self.mat[6] * self.mat[15] - \
		self.mat[1] * self.mat[7] * self.mat[14] - \
		self.mat[5] * self.mat[2] * self.mat[15] + \
		self.mat[5] * self.mat[3] * self.mat[14] + \
		self.mat[13] * self.mat[2] * self.mat[7] - \
		self.mat[13] * self.mat[3] * self.mat[6])

		append(-self.mat[1] * self.mat[6] * self.mat[11] + \
		self.mat[1] * self.mat[7] * self.mat[10] + \
		self.mat[5] * self.mat[2] * self.mat[11] - \
		self.mat[5] * self.mat[3] * self.mat[10] - \
		self.mat[9] * self.mat[2] * self.mat[7] + \
		self.mat[9] * self.mat[3] * self.mat[6])

		append(-self.mat[4] * self.mat[10] * self.mat[15] + \
		self.mat[4] * self.mat[11] * self.mat[14] + \
		self.mat[8] * self.mat[6] * self.mat[15] - \
		self.mat[8] * self.mat[7] * self.mat[14] - \
		self.mat[12] * self.mat[6] * self.mat[11] + \
		self.mat[12] * self.mat[7] * self.mat[10])

		append(self.mat[0] * self.mat[10] * self.mat[15] - \
		self.mat[0] * self.mat[11] * self.mat[14] - \
		self.mat[8] * self.mat[2] * self.mat[15] + \
		self.mat[8] * self.mat[3] * self.mat[14] + \
		self.mat[12] * self.mat[2] * self.mat[11] - \
		self.mat[12] * self.mat[3] * self.mat[10])

		append(-self.mat[0]  * self.mat[6] * self.mat[15] + \
		self.mat[0]  * self.mat[7] * self.mat[14] + \
		self.mat[4]  * self.mat[2] * self.mat[15] - \
		self.mat[4]  * self.mat[3] * self.mat[14] - \
		self.mat[12] * self.mat[2] * self.mat[7] + \
		self.mat[12] * self.mat[3] * self.mat[6])

		append(self.mat[0] * self.mat[6] * self.mat[11] - \
		self.mat[0] * self.mat[7] * self.mat[10] - \
		self.mat[4] * self.mat[2] * self.mat[11] + \
		self.mat[4] * self.mat[3] * self.mat[10] + \
		self.mat[8] * self.mat[2] * self.mat[7] - \
		self.mat[8] * self.mat[3] * self.mat[6])

		append(self.mat[4] * self.mat[9] * self.mat[15] - \
		self.mat[4] * self.mat[11] * self.mat[13] - \
		self.mat[8] * self.mat[5] * self.mat[15] + \
		self.mat[8] * self.mat[7] * self.mat[13] + \
		self.mat[12] * self.mat[5] * self.mat[11] - \
		self.mat[12] * self.mat[7] * self.mat[9])

		append(-self.mat[0] * self.mat[9] * self.mat[15] + \
		self.mat[0] * self.mat[11] * self.mat[13] + \
		self.mat[8] * self.mat[1] * self.mat[15] - \
		self.mat[8] * self.mat[3] * self.mat[13] - \
		self.mat[12] * self.mat[1] * self.mat[11] + \
		self.mat[12] * self.mat[3] * self.mat[9])

		append(self.mat[0]  * self.mat[5] * self.mat[15] - \
		self.mat[0]  * self.mat[7] * self.mat[13] - \
		self.mat[4]  * self.mat[1] * self.mat[15] + \
		self.mat[4]  * self.mat[3] * self.mat[13] + \
		self.mat[12] * self.mat[1] * self.mat[7] - \
		self.mat[12] * self.mat[3] * self.mat[5])

		append(-self.mat[0] * self.mat[5] * self.mat[11] + \
		self.mat[0] * self.mat[7] * self.mat[9] + \
		self.mat[4] * self.mat[1] * self.mat[11] - \
		self.mat[4] * self.mat[3] * self.mat[9] - \
		self.mat[8] * self.mat[1] * self.mat[7] + \
		self.mat[8] * self.mat[3] * self.mat[5])

		append(-self.mat[4] * self.mat[9] * self.mat[14] + \
		self.mat[4] * self.mat[10] * self.mat[13] + \
		self.mat[8] * self.mat[5] * self.mat[14] - \
		self.mat[8] * self.mat[6] * self.mat[13] - \
		self.mat[12] * self.mat[5] * self.mat[10] + \
		self.mat[12] * self.mat[6] * self.mat[9])

		append(self.mat[0] * self.mat[9] * self.mat[14] - \
		self.mat[0] * self.mat[10] * self.mat[13] - \
		self.mat[8] * self.mat[1] * self.mat[14] + \
		self.mat[8] * self.mat[2] * self.mat[13] + \
		self.mat[12] * self.mat[1] * self.mat[10] - \
		self.mat[12] * self.mat[2] * self.mat[9])

		append(-self.mat[0]  * self.mat[5] * self.mat[14] + \
		self.mat[0]  * self.mat[6] * self.mat[13] + \
		self.mat[4]  * self.mat[1] * self.mat[14] - \
		self.mat[4]  * self.mat[2] * self.mat[13] - \
		self.mat[12] * self.mat[1] * self.mat[6] + \
		self.mat[12] * self.mat[2] * self.mat[5])

		append(self.mat[0] * self.mat[5] * self.mat[10] - \
		self.mat[0] * self.mat[6] * self.mat[9] - \
		self.mat[4] * self.mat[1] * self.mat[10] + \
		self.mat[4] * self.mat[2] * self.mat[9] + \
		self.mat[8] * self.mat[1] * self.mat[6] - \
		self.mat[8] * self.mat[2] * self.mat[5])

		det = self.determinant()

		if (det == 0):
			raise Exception('singular matrix')

		det = 1.0 / det

		return Mat44([x * det for x in inverse])

	def toList(self):
		self.updateMat()
		return self.mat

	def __str__(self):
		return ' '.join(str(x) for x in [self.row0.x, self.row0.y, self.row0.z, self.row0.w, '\n' +
		str(self.row1.x), self.row1.y, self.row1.z, self.row1.w, '\n' + \
		str(self.row2.x), self.row2.y, self.row2.z, self.row2.w, '\n' + \
		str(self.row3.x), self.row3.y, self.row3.z, self.row3.w])

	def __getitem__(self, index):
		if isinstance(index, tuple):
			if index[0] < 0 or index[0] > 3 or index[1] < 0 or index[1] > 3 or not isinstance(index[0], (int, float)) or len(index) != 2:
				raise Exception('invalid index')
			return self.mat[index[0] * 4 + index[1]]
		elif isinstance(index, int):
			if index < 0 or index > 3:
				raise Exception('invalid index')
			return self.getRow(index)
		else:
			raise Exception('invalid index')

	def __setitem__(self, index, value):
		if isinstance(index, tuple):
			if index[0] < 0 or index[0] > 3 or index[1] < 0 or index[1] > 3 or not isinstance(index[0], (int, float)) or len(index) != 2:
				raise Exception('invalid index')
			if isinstance(value, (int, float)):
				self.mat[index[0] * 4 + index[1]] = value
				self.updateRowVec(index[0]*4 + index[1], value)
			else:
				raise Exception('invalid value: must be of type Int or Float')
		elif isinstance(index, int):
			if index < 0 or index > 3:
				raise Exception('invalid index')
			if not isinstance(value, Vec):
				raise Exception('invalid value: must be of type Vec')
			self.setRow(index, value)

	def __mul__(self, other):
		if isinstance(other, Mat44):
			return self.matrixMatrixMul(other)
		elif isinstance(other, Vec):
			return self.matrixVectorMul(other)
		elif isinstance(other, (int, float)):
			return self.scalarMul(other)
		else:
			return NotImplemented

	def __rmul__(self, other):
		if isinstance(other, Mat44):
			return other.matrixMatrixMul(self)
		elif isinstance(other, Vec):
			return self.vectorMatrixMul(other)
		elif isinstance(other, (int, float)):
			return self.scalarMul(other)
		else:
			return NotImplemented

	def __add__(self, other):
		if isinstance(other, (int, float)):
			return self.add(other)
		else:
			return NotImplemented

	def __sub__(self, other):
		if isinstance(other, (int, float)):
			return self.subtract(other)
		else:
			return NotImplemented

	def svd(self):
		# singular value decomposition
		# self = UwV' (V' is V transpose)
		# replaces self with U
		# returns self, w, V (NOT V TRANSPOSE),
		# where s is a vector of singular values in decreasing order
		# to make this work for arbitrary sizes, just make the function take in m and n
		# instead of hardcoding to be 4. (where self is an mxn matrix)
		# lol


		def pythag(a, b):
			absa = math.fabs(a)
			absb = math.fabs(b)
			if absa > absb:
				return absa * math.sqrt(1.0 + math.pow(absb / absa, 2))
			elif absb == 0.0:
				return 0.0
			else:
				return absb * math.sqrt(1.0 + math.pow(absa / absb, 2))

		w = [0]*4
		v = Mat44(row0x = 0, row1y = 0, row2z = 0, row3y = 0)
		rv1 = [0]*4
		g = scale = anorm = 0.0
		m = n = 4
		for i in range(1,5):
			l = i + 1
			rv1[i-1] = scale * g
			g = s = scale = 0.0
			if i <= m:
				for k in range(i, m+1):
					scale += abs(self[k-1,i-1])
				if scale:
					for k in range(i, m+1):
						self[k-1, i-1] /= scale
						s += self[k-1, i-1] * self[k-1, i-1]
					f = self[i-1, i-1]
					g = -(f/f) * math.sqrt(s)
					h = f * g - s
					self[i-1, i-1] = f - g
					for j in range(l, n+1):
						s = 0.0
						for k in range(i, m+1):
							s += self[k-1,i-1] * self[k-1,j-1]
						f = s / h
						for k in range(i, m+1):
							self[k-1, j-1] += f * self[k-1, i-1]
					for k in range(i, m+1):
						self[k-1, i-1] *= scale
			w[i-1] = scale * g
			g = s = scale = 0.0
			if i <= m and i != n:
				for k in range(l, n+1):
					scale += math.fabs(self[i-1, k-1])
				if scale:
					for k in range(l, n+1):
						self[i-1, k-1] /= scale
						s += self[i-1, k-1] * self[i-1, k-1]
					f = self[i-1, l-1]
					g = -(f/f) * math.sqrt(s)
					h = f * g - s
					self[i-1, l-1] = f - g
					for k in range(l, n+1):
						if h != 0: rv1[k-1] = self[i-1, k-1] / h
					for j in range(l, m+1):
						s = 0.0
						for k in range(l, n+1):
							s += self[j-1, k-1] * self[i-1, k-1]
						for k in range(l, n+1):
							self[j-1, k-1] += s * rv1[k-1]
					for k in range(l, n+1):
						self[i-1, k-1] *= scale
			anorm = max(anorm, (math.fabs(w[i-1]) + math.fabs(rv1[i-1])))
		for i in range(n, 0, -1):
			if i < n:
				if g:
					for j in range(l, n+1):
						if self[i-1, l-1] != 0 and g != 0: v[j-1, i-1] =  (self[i-1, j-1] / self[i-1, l-1]) / g
					for j in range(l, n+1):
						s = 0.0
						for k in range(l, n+1):
							s += self[i-1, k-1] * v[k-1, j-1]
						for k in range(l, n+1):
							v[k-1, j-1] += s * v[k-1, i-1]
			v[i-1, i-1] = 1.0
			g = rv1[i-1]
			l = i
		for i in range(min(m, n), 0, -1):
			l = i + 1
			g = w[i-1]
			for j in range(l, n+1):
				self[i-1, j-1] = 0.0
			if g:
				g = 1.0 / g
				for j in range(l, n+1):
					s = 0.0
					for k in range(l, m+1):
						s += self[k-1, i-1] * self[k-1, j-1]
						f = (s / self[i-1, i-1]) * g
						for k in range(i, m+1):
							self[k-1, j-1] += f * self[k-1, i-1]
			else:
				for j in range(i, m+1):
					self[k-1, i-1] = 0.0
			self[i-1, i-1] += 1
		for k in range(n, 0, -1):
			for its in range(1, 31):
				flag = 1
				for l in range(k, 0, -1):
					nm = l-1
					if float(math.fabs(rv1[l-1]) + anorm) == anorm:
						flag = 0
						break
					if float(math.fabs(w[nm-1]) + anorm) == anorm:
						break
				if flag:
					c = 0.0
					s = 1.0
					for i in range(l, k+1):
						f = s * rv1[i-1]
						rv1[i-1] = c * rv1[i-1]
						if float(math.fabs(f) + anorm) == anorm:
							break
						g = w[i-1]
						h = pythag(f, g)
						w[i-1] = h
						h = 1.0 / h
						c = g * h
						s = -f * h
						for j in range(1, m+1):
							y = self[j-1, nm-1]
							z = self[j-1, i-1]
							self[j-1, nm-1] = y * c + z * s
							self[j-1, i-1] = z * c - y * s
				z = w[k -1]
				if l == k:
					if z < 0.0:
						w[k-1] = -z
						for j in range(1, n+1):
							v[j-1, k-1] = -v[j-1, k-1]
					break
				if its == 30:
					raise Exception('no convergence in 30 iterations')
				x = w[l-1]
				nm = k -1
				y = w[nm-1]
				g = rv1[nm-1]
				h = rv1[k-1]
				f = ((y - z) * (y + z) + (g - h) * (g + h)) / (2.0 * h * y)
				g = pythag(f, 1.0)
				if x != 0 and (f + (g * (f / f))) != 0: f = ((x - z) * (x + z) + h * ((y / (f + (g * (f / f)))) - h)) / x
				c = s = 1.0
				for j in range(l, nm+1):
					i = j + 1
					g = rv1[i-1]
					y = w[i-1]
					h = s * g
					g = c * g
					z = pythag(f, h)
					rv1[j-1] = z
					c = f / z
					s = h / z
					f = x * c - x * s
					h = y * s
					y *= c
					for jj in range(1, n+1):
						x = v[jj - 1, j - 1]
						z = v[jj - 1, i - 1]
						v[jj-1, j-1] = x * c + z * s
						v[jj-1, i-1] = z * c - x * s
					z = pythag(f, h)
					w[j-1] = z
					if z:
						z = 1.0 / z
						c = f * z
						s = h * z
					f = c * g + s * y
					x = c * y - s * g
					for jj in range(1, m+1):
						y = self[jj - 1, j - 1]
						z = self[jj - 1, i - 1]
						self[jj - 1, j - 1] = y * c + z * s
						self[jj - 1, i - 1] = z * c - y * s
				rv1[l-1] = 0.0
				rv1[k-1] = f
				w[k-1] = x
		return self, Vec(w), v


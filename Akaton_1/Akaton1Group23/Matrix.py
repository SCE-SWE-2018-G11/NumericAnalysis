def copyMatrix(m):
	cpy = Matrix(m.columns, m.rows)
	for i in range(m.rows):
		for j in range(m.columns):
			cpy.setAt(j, i, m[i][j])
	return cpy

class Matrix:
	def __init__(self, columns, rows):
		self.data = []
		self.columns = columns
		self.rows = rows
		for i in range(rows):
			column = []
			for j in range(columns):
				column.append(0)
			self.data.append(column)
	
	def __getitem__(self, column, row=-1):
		if row < 0:
			return self.data[column]
		return self.data[column][row]
	
	def __str__(self):
		return self.data.__str__()
	
	def __mul__(self, other):
		if type(other) == int or type(other) == float:
			mat = copyMatrix(self)
			for i in range(mat.rows):
				for j in range(mat.columns):
					mat.setAt(j, i, self[i][j] * other)
			return mat
		if type(other) is Matrix:
			if other.rows != self.columns:
				raise ValueError("incompatible matrices")
			mat = Matrix(other.columns, self.rows)
			for i in range(self.columns):
				for j in range(other.columns):
					sum = 0
					for k in range(self.columns):
						sum += self[i][k] * other[k][j]
					mat.setAt(j, i, sum)
			return mat
		raise ValueError("matrix multiplication not by matrix or scalar")
	
	def __rmul__(self, other):
		if type(other) == int or type(other) == float:
			return self * other
		if type(other) == Matrix:
			return other.__mul__(self)
		raise ValueError("matrix multiplication not by matrix or scalar")
	
	def __add__(self, other):
		if type(other) == Matrix:
			if self.columns != other.columns or self.rows != other.rows:
				raise ValueError("incompatible matrices")
			mat = Matrix(self.columns, self.rows)
			for i in range(self.rows):
				for j in range(self.columns):
					mat.setAt(j, i, self[i][j] + other[i][j])
			return mat
			
		raise ValueError("addition supports only matrices")
	
	def setAt(self, column, row, value):
		self.data[row][column] = value

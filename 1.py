import numpy as np

def is_symmetric(matrix):
	if np.equal(matrix, matrix.T).all():
		print 'Symmetric'
	else:
		print 'Not symmetric'

def read_input():
	f = open('test3.txt', 'r')
	for line in f:
		rows = line.split(';')
		n = len(rows)
		#print n
		matrix = np.empty((n, n))
		#print matrix.shape
		for i in range(n):
			els = rows[i].split(',')
			for j in range(n):
				matrix[i, j] = els[j]
		is_symmetric(matrix)


if __name__ == '__main__':
	read_input()
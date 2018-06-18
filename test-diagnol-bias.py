import numpy as numpy

import random
w, h = 15, 15;

ResultMatrix = [[0 for x in range(w)] for y in range(h)]

print()
print()


topWeight = 1
leftWeight = 1
diagonalWeight = 1

leftCount = 0
upCount = 0
diagonalCount = 0

for i in range(10000):

	# fill random stuff in the cost matrix
	Matrix = [[random.uniform(0, 1) for x in range(w)] for y in range(h)]






	# fill cumulative cost matrix with stuff
	for i in range(h):
		for j in range(w):
			top = float('inf')
			left = float('inf')
			diagonal = float('inf')
			if(i - 1 >= 0):
				top = ResultMatrix[i - 1][j] + topWeight*Matrix[i][j]
			
			if(j - 1 >= 0):
				left = ResultMatrix[i][j - 1]+ leftWeight*Matrix[i][j]
			
			if(i - 1 >= 0 and j - 1 >= 0):
				diagonal = ResultMatrix[i - 1][j - 1] + diagonalWeight*Matrix[i][j]
			
			if(i == 0 and j == 0):
				ResultMatrix[i][j] = Matrix[0][0]
			else:
				ResultMatrix[i][j] = min(top, left, diagonal)
				# choice = min(top, left, diagonal)
				# if choice == top :
				# 	upCount = upCount + 1
				# elif choice == left :
				# 	leftCount = leftCount + 1
				# elif choice == diagonal:
				# 	diagonalCount = diagonalCount + 1

	#print('\n'.join(['  '.join(['{:4}'.format(item) for item in row]) for row in ResultMatrix]))

	#print()
	#print()

	row = h - 1
	column = w - 1

	# draw the shortest path on the cumulative matrix. 
	while row != 0 or column != 0 : 

		if(row == 0):
			ResultMatrix[row][column] = '  x'
			column = column - 1
			leftCount = leftCount + 1
		elif(column == 0):

			ResultMatrix[row][column] = '  x'
			row = row - 1
			upCount = upCount + 1

		elif(row != 0 and column != 0):
			#print('column : ' + `column` + ' row: ' + `row`)
			top = float('inf')
			left = float('inf')
			diagonal = float('inf')
			
			if(row - 1 >= 0 ):
				top = ResultMatrix[row - 1][column] + topWeight*Matrix[row][column]
			
			if(column - 1 >= 0):
				left = ResultMatrix[row][column - 1] + leftWeight*Matrix[row][column]
			
			if((row - 1 >= 0) and (column - 1 >= 0)):
				diagonal = ResultMatrix[row - 1][column - 1] + diagonalWeight*Matrix[row][column]

			choice = min(top, left, diagonal)

			ResultMatrix[row][column] = '  x'

			if choice == top :
				row = row - 1
				upCount = upCount + 1
			elif choice == left :
				column = column - 1
				leftCount = leftCount + 1
			else :
				row = row - 1
				column = column - 1
				diagonalCount = diagonalCount + 1


#print('\n'.join(['  '.join(['{:4}'.format(item) for item in row]) for row in ResultMatrix]))

print('left count : ' + `leftCount`)
print('diagonalCount : ' + `diagonalCount`)
print('upCount : ' + `upCount`)










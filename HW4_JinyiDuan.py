#part 1
def my_function(some_list):
	string = ''
	

	if len(some_list)>2:
		for i in range(len(some_list)-1):
			string += some_list[i] + ', '
		string = string + 'and ' + some_list[-1]+ '.'

	elif len(some_list)==2:
		for i in range(len(some_list)-1):
			string += some_list[i] + ' '
		string = string  + 'and ' + some_list[-1]+'.'

	elif len(some_list)==1:
		string=some_list[0]+'.'

	return string

vegetables = ['carrot', 'lettuce', 'onion', 'radish']
print(my_function(vegetables))



#part 2
grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]



#rotate the 2d grid 90 degrees clockwise
gridRotated=''
for i in range(6):
	for q in range(9):
		gridRotated+=gridRotated[q][i]
	print(gridz)
	gridRotated=''

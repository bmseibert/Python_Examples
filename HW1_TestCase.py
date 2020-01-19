from ex1 import ConnectFour
import boards
'''
Make sure you put ex1.py in the same directory as this file.
run with command "python3 -u HW1_TestCase.py"
We cannot exhaust all possibilities, so passing this test does not guarantee final success.
boards are made up for fun, they do not represent reality
'''

def test1():
	'''isLineAt'''
	print("Start of test1, progressing ", end='')

	Board = "Board 1: "
	c = ConnectFour(boards.BOARD1, boards.W, boards.H)
	# horizontal
	assert c.isLineAt(4,0,1,0) == False,	Board + "There's no such line starting at (4,0) horizontally"
	assert c.isLineAt(1,1,1,0) == True,		Board + "There are 4 0s starting at (1,1) horizontally"
	assert c.isLineAt(1,5,1,0) == True,		Board + "There are 4 1s starting at (1,5) horizontally"
	print("...", end='')
	# vertical
	assert c.isLineAt(3,0,0,1) == True,		Board + "There are 4 0s starting at (3,0) vertically"
	assert c.isLineAt(2,1,0,1) == False,	Board + "There's no such line starting at (2,1) vertically"
	assert c.isLineAt(6,4,0,1) == False,	Board + "There's no such line starting at (6,4) vertically"
	print("...", end='')
	# Diagonal up
	assert c.isLineAt(1,1,1,1) == True,		Board + "There are 4 0s starting at (1,1) diagonally up"
	assert c.isLineAt(4,4,1,1) == False,	Board + "There's no such line startng at (4,4) diagonally up"
	assert c.isLineAt(0,1,1,1) == True,		Board + "There are 4 2s starting at (0,1) diagonally up"
	print("...", end='')
	# Diagonal down
	assert c.isLineAt(0,2,1,-1) == False,	Board + "There's no such line starting at (0,2) diagonally down"
	assert c.isLineAt(2,4,1,-1) == True,	Board + "There are 4 0s starting at (2,4) diagonally down"
	assert c.isLineAt(1,3,1,-1) == False,	Board + "There's no such line starting at (1,3) diagonally down"
	print("...", end='')

	print("")

	# success!
	print("Test1: isLineAt, PASS!!!")
	print("")
	return True

def test2():
	print("Start of test2, progressing ", end='')
	'''getOutcome'''

	Board = "Board 2: "
	c = ConnectFour(boards.BOARD2, boards.W, boards.H)
	assert c.getOutcome() == 0,	Board + "No Winner!!! You got it wrong."
	print("...", end='')

	Board = "Board 3: "
	c = ConnectFour(boards.BOARD3, boards.W, boards.H)
	assert c.getOutcome() == 1,	Board + "The winner should be player 1. Check starting point (2,0) diagonally up"
	print("...", end='')

	Board = "Board 4: "
	c = ConnectFour(boards.BOARD4, boards.W, boards.H)
	assert c.getOutcome() == 1,	Board + "The winner should be player 1. Check starting point (0,0) horizontally"
	print("...", end='')

	print("")

	# success
	print("Test2: getOutcome, PASS!!!")
	print("")
	return True

def main():
	print("Test of ex1 begins, check boards.py when in doubt, contact Guanyi if you found any bug.")
	print("Make sure you put HW1_TestCase.py and boards.py in the same directory as ex1.py.")
	print("")
	test1()
	test2()
	print("Congrats! I cannot find any obvious bug in ex1. Test will end now.")

if __name__ == '__main__':
	main()
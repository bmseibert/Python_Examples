from ex2 import isreverse

def test():
	print("Test of ex2 begins, make sure you put this file in the same dir as ex2.py.")
	assert isreverse("","") == True,		"Two empty strings are the reverse of each other, expecting True"
	assert isreverse("a","a") == True,		"Two single character a, expecting True"
	assert isreverse("ab","ba") == True,	"ab is the reverse of ba, expecting True"
	assert isreverse("ba","ab") == True,	"ba is the reverse of ab, expecting True"
	assert isreverse("","a") == False,		"empty string is not the reverse of a, expecting False"
	assert isreverse("a","") == False,		"a is not the reverse of empty string, expecing False"
	print("Yeah you passed this simple test of ex2! Congrats!!!")

if __name__ == '__main__':
	test()
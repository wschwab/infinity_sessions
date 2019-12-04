import sys

score = int(sys.argv[1])

def grader(_score):
	if _score < 10:
	    print("F")
	elif _score <30:
	    print("E")
	elif _score < 50:
	    print("D")
	elif _score < 70:
	    print("C")
	elif _score < 90:
	    print("B")
	else:
	    print("A")

grader(score)

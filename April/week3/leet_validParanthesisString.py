#  Let lo, hi respectively be the smallest and largest possible number of open left brackets after processing the current character in the string.
# If we encounter a left bracket (c == '('), then lo++, otherwise we could write a right bracket, so lo--. 
# If we encounter what can be a left bracket 
# (c != ')'), then hi++, otherwise we must write a right bracket, so hi--. If hi < 0, then the current
# prefix can't be made valid no matter what our choices are. Also, we can never have less than 0 open left brackets. At the end, we should check that we can have exactly 0 open left brackets.

def checkValidString(s):
	if s == None or len(s) == 0:
		return True

	low,high = 0,0
	n = len(s)
	for i in range(n):
		if s[i] == '(' :
			low += 1
			high += 1
		elif s[i] == ')' :
			if low > 0 :
				low -= 1
			high -= 1

		else :
			if low > 0 :
				low -= 1
			high += 1

		if high < 0 :
			return False 

	return (low == 0)
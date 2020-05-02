def countSumSquare(n):
    summ = 0
    if n < 10 :
        summ += n**2
    else:
        summ += (n%10)**2 + countSumSquare(n//10)
    return summ

# print(countSumSquare(100))\


def isHappy(n):
	hashSet = set()
	while(1):
		s = countSumSquare(n)
		if s == 1 :
			return True
		if s not in hashSet :
			hashSet.add(s)
		else :
			return False
		n = s

	

print(isHappy(82))
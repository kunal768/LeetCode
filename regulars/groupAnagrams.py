
# O(n^2) is brute force
# but what else ?
# fuck yes this is a medium QUESTION 
# sad part : i couldnt solve it :( in the first go 
# but thanks to Kevin Naughton Jr. i now know how to solve this

test = ["eat", "tea", "tan", "ate", "nat", "bat"]

def groupAnagrams(stringList):
	# returning array
	ans = []
	hashMap = dict()
	for i in stringList:
		x = "".join(sorted(i))
		if x not in hashMap :
			hashMap[x] = []
		hashMap[x].append(i)
	for i in hashMap:
		ans.append(hashMap[i])
	return ans


print(groupAnagrams(test))
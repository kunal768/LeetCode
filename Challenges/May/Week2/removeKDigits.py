# Greedy Approach if string is sorted remove from end else remove nums whose next num is smaller than them
# Result - Accepted 
# O(n) time and O(1) space
class Solution:
    def removeKdigits(self, string: str, k: int) -> str:
        if len(string) == k :
            return "0"
        arr = [i for i in string]
        for j in range(k):
            i = 0
            while (i < len(arr) - 1) and (arr[i] <= arr[i+1]): 
                i += 1
            arr.remove(arr[i])

        # remove leading zeroes
        while len(arr) > 1 and arr[0] == "0" :
            arr = arr[1:]

        if len(arr) == 0 :
            return "0"
        return "".join(arr)


# O(n) space
def removeK_stack(string,k):
    # last case
    if len(string) == k :
        return "0"
    
    stack = []
    i = 0 
    
    while i < len(string) :
        while k > 0 and stack and int(stack[-1]) > int(string[i]):
            stack.pop()
            k -= 1
        stack.append(string[i])
        i += 1

    # corner case like 1111 (all dups)
    while k > 0 :
        stack.pop()
        k -=1 

    while len(stack) > 1 and stack[0] == "0":
        stack.pop(0)

    return "".join(stack)



# DFS Approach for Greedy Problem - Aise Hi sexy lag rha tha 
# Result - Large Input Testcase - TLE( But code is code )
class Solution:
    def dfs(self,num,res,path,index,n,k): 
        if len(path) == n - k :
            if not path :
                return 
            x = int("".join(path))
            res.add(x)
            return 
        if index == n:
            return 
        
        for i in range(index,n):
            self.dfs(num,res,path+[num[i]],i+1,n,k)
            
    def removeKdigits(self, num: str, k: int) -> str:
        # dfs bhi kr skte hai seeing which number is smallest 
        res = set()
        self.dfs(num,res,[],0,len(num),k)
        if len(res) == 0 :
            return "0"
        return str(min(res))

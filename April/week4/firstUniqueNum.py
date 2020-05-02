from collections import defaultdict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.hashset = set()
        self.unique = defaultdict(lambda:0)
        for i in nums :
            self.add(i)
        

    def showFirstUnique(self) -> int:
        if len(self.unique) != 0 :
            return list(self.unique.keys())[0]
        else:
            return -1

    def add(self, value: int) -> None:
        if value in self.hashset: # means value is repeated so no use of this 
            # we need to also delete this value from the unique
            if value in self.unique:
                del self.unique[value]
            else:
                pass
                
        else:
            self.unique[value] += 1
            self.hashset.add(value)
        


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
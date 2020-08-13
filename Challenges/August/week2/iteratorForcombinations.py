# Cheating Way
class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.comb = ["".join(i) for i in combinations(characters,combinationLength)]
        

    def next(self) -> str:
        if self.comb:
            return self.comb.pop(0)
        

    def hasNext(self) -> bool:
        if self.comb :
            return True 
        return False
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

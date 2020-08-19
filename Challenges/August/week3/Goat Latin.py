class Solution:
    def toGoatLatin(self, s: str) -> str:
        if not s :
            return ""
        new = []
        for idx,val in enumerate(s.split(" ")):
            if val[0].lower() in {"a","e","i","o","u"} :
                new.append(val+"ma"+"a"*(idx+1))
            else:
                new.append(val[1:]+val[0]+"ma"+"a"*(idx+1))
        return " ".join(new)
        

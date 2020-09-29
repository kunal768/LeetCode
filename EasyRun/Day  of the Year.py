class Solution(object):
    def dayOfYear(self, date):
        """
        :type date: str
        :rtype: int
        """
        params = date.split('-')
        year, month, date = int(params[0]), int(params[1]), int(params[2])
        ans = 0 
        ty = { 4, 6, 9, 11 }
        to = { 1, 3, 5, 7, 8, 10, 12 }
        feb = 28 
        if (((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0)):
            feb = 29
        
        for i in range(1,month):
            if i in ty :
                ans += 30 
            elif i in to :
                ans += 31
            elif i == 2 :
                ans += feb 
        
        return date+ans
        
        
        
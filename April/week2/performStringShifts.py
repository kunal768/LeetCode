def rotate(a,direction,k):
    if direction == 0:
        return a[k:] + a[:k]
    else:
        return a[-k:] + a[:-k]
    
# class Solution:
def stringShift(s,shift):
    net = [0,0]
    for q in shift :
    	if q[1] >= net[1]:
    		if q[0] == net[0] :
    			net[1] = net[1]+q[1]
    		else :
    			net = [q[0],q[1]-net[1]]
    	else :
    		net[1] = net[1]- q[1]
    print(net)
    return rotate(s,net[0],net[1])

# [1,4] , [0,5] , [0,4] , [1,1], [1,5]

# [1,4]
# [0,1]
# [0,5]
# [1,1]
# [1,1]
shift = [[1,4],[0,5],[0,4],[1,1],[1,5]]
s = "mecsk"
print(stringShift(s,shift))

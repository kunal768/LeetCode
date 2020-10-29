# Geeks Solution

def diff(n, mid):
  if n > mid*mid*mid :
    return n - (mid*mid*mid)
  
  return ((mid*mid*mid) - n)


def cubthroot(n):
  l, h = 0, n 
  e = 0.0000001

  while True :
    mid = (l+h)/2
    error = diff(n, mid)

    if error <= e :
      return mid   
    # Geeks Solution
    
    
    if mid*mid*mid > n :
      h = mid 
    
    else :
      l = mid 


print((cubthroot(27)))

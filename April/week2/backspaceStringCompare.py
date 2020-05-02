def backspaceCompare( S ,T) :
    n = len(S)
    print(S)
    for i in range(1,n):
        if S[i] == "#" and S[i-1] != "#":
            S[i-1].replace(S[i-1],"#")
    print(S)




S = "a##c"
T = "#a#c"

print(backspaceCompare(S,T))

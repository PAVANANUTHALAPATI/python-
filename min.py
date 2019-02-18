def samllest (pav,n):  
    min = pav[0]
    for i in range(1, n): 
        if pav[i] > min: 
            min = pav[i] 
    return min
pav = [1,2,3,4,] 
n = len(pav) 
Ans = samllest (pav,n) 
print ("samllest in given array is",Ans) 

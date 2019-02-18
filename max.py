def largest(pav,n):  
    max = pav[0]
    for i in range(1, n): 
        if pav[i] > max: 
            max = pav[i] 
    return max
pav = [10, 32, 45, 90, 98] 
n = len(pav) 
Ans = largest(pav,n) 
print ("Largest in given array is",Ans)

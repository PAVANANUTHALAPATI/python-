li=int(input(""))
lu=0
for i in range(2,li//2+1):
    if(li%i==0):
        lu=lu+1
if(lu<=0):
    print("Number is prime")
else:
    print("Number isn't prime")

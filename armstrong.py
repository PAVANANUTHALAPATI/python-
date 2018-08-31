indira=int(input(""))
reddy=list(map(int,str(indira)))
pavala=list(map(lambda x:x**3,reddy))
if(sum(pavala)==indira):
    print("yes")
else:
    print("no")

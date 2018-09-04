indra = int(input(""))
reddy = int(input(""))
for pavala in range(indra,reddy + 1):
   if pavala > 1:
       for i in range(2,pavala):
           if (pavala % i) == 0:
               break
       else:
           print(pavala)

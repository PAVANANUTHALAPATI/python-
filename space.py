indira = int(input(""))
reddy = int(input(""))
for pavala in range(indira,reddy + 1):
   mama = 0
   madhu = pavala
   while madhu > 0:
       digit = madhu % 10
       mama += digit ** 3
       madhu //= 10
       if pavala == mama:
         print(pavala)

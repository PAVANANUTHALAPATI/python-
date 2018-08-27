n16=int(input(""))
if(n16%4==0 and n16%100!=0 or n16%400==0):
    print("The year is a leap year")
else:
    print("The year isn't a leap year")

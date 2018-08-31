def factorial(indra):
    if indra == 1:
        return indra
    else:
        return indra * factorial(indra - 1)
indra = int(input(""))
if indra < 0:
    print("Factorial cannot be found for negative numbers")
elif indra == 0:
    print("1")
else:
    print( factorial(indra))

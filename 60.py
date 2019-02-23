k=int(raw_input(""))
if k < 0:
  print("")
else:
  sum=0
  while(k > 0):
    sum+=k
    k-=1
print(sum)

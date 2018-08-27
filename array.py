indra,reddy = [int(j) for j in raw_input().split(" ")]
values = [int(j) for j in raw_input().split(" ") ]
sum = 0
for x in range(reddy):
    sum += values[x]
print(sum)

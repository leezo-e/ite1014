
list = ["apple", "sos", "orange", "011"]

sum = 0

for i in range (3) :
    if len(list[i]) >= 2 and list[i][0] == list[i][-1] :
         sum += 1

print (sum)

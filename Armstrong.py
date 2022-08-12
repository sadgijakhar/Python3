
num = int(input("Enter a number: "))
sum = 0
list = []
for i in range(100,num+1): 
    temp = i
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if  i == sum:
        if(i%2 == 0):
            list.append(sum)
    sum = 0
print(list)


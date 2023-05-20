# Write a program that asks the user how many Fibonnaci numbers
# to generate and then generates them.

fibo = {0: 1, 1: 1}

for i in range(2, int(input())):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

print(list(fibo.values()))

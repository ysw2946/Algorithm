import sys
total = int(sys.stdin.readline())

number = [1,2,4]

for i in range(3,10):
    number.append(sum(number[i-3:i]))

for _ in range(total):
    n = int(sys.stdin.readline())
    print(number[n-1])

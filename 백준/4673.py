number_list = [i for i in range(1,10001)]

for i in range(1,10001):
    n = [int(a) for a in str(i)]
    n = i + sum(n)
    if n in number_list:
        number_list.remove(n)
        
for n in number_list:
    print(n)
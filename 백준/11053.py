n = int(input())
number_list = list(map(int,input().split()))

dp = [1] * n

for i in range(n):
    for j in range(i):
        if number_list[i] > number_list[j] :
            dp[i] = max(dp[j]+1, dp[i])
            
print(max(dp))
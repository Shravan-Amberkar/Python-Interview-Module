'''
Bytelandian gold coins

Dynamic Programming + recursion + memoization

'''
dp = dict()
def hom(n):
    if n not in dp:
        #recursively break down n into smaller denominations up until it is profitable
        dp[n] = max(n, hom(n//2)+hom(n//3)+hom(n//4)) 
        #print(dp)
    return dp[n]

for u in range(0,12): # 12-->LCM of 2,3 and 4
    dp[u] = u

while(True):
    try:
        n = int(input())
        print(hom(n))
    except:
        break

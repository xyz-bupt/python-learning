#埃氏筛（筛素数）
#时间复杂度：O(nloglogn)
primes = []
is_prime = [True] * (n+1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(math.sqrt(n)) + 1):  #i*i<=n
    if is_prime[i]:
        for j in range(i*i, n+1, i):   #从i*i开始(之前的处理过了)
            is_prime[j] = False
for i in range(2,n+1):
    if is_prime[i]:
        primes.append(i)
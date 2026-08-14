n=int(input())
nums= list(map(int,input().split()))

sumexpected= n*(n+1)//2
sumactual= sum(nums)
print(sumexpected - sumactual) #missing number



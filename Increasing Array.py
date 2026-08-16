n=int(input())
nums= list(map(int, input().split()[:n]))
count=0
prev=nums[0]
for i in range(1,n):
    if nums[i] < prev:
        count+= prev - nums[i]
    else:
        prev= nums[i]    
print(count)        
    
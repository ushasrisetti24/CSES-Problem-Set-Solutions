strng= input().strip()
curr_len=1
max_len=1

for i in range(1,len(strng)):
    if(strng[i]==strng[i-1]):
        curr_len+=1
        max_len= max(curr_len,max_len)
    else:
        curr_len=1    
print(max_len)
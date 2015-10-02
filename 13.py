A = list(map(int, input().split()))
i=0
count=0
sum=0
while i<len(A)-1:
    if A[i]==2 and A[i+1]!=2:
        count+=1
        sum+=A[i+1]
        i+=2
    elif A[i]!=2:
        count+=1
        sum+=A[i]
        i+=1
    elif A[i]==2 and A[i+1]:
        count+=1
        sum+=A[i]
        i+=1

if A[len(A)-1]==2:
        count+=1
        sum+=2
print(sum//count)

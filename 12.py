n=int(input())
A = list(map(int, input().split()))
sr=sum(A)/n
i=0
min=100
while i<n:
    if abs((A[i]-sr))<min:
        min=abs((A[i]-sr))
        z=A[i]
    i+=1
print(z)

A = list(map(int, input().split()))
B=[0]*100
n=A[0]
k=A[1]
i=0
while i<n:
    B[i]=1
    i+=1
l=n
while l<=k:
    j=1
    while j<=n:
        B[l]=B[l]+B[l-j]
        j+=1
    l+=1
print(B[k])

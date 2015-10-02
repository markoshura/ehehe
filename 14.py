n=int(input())
A=[]
B=[]
i=0
count=0
while i<n:
    A.append(int(input()))
    B.append(int(input()))
    i+=1
t=int(input())
i=0
while i<n:
    if (A[i]<=t and B[i]<=t) or (A[i]>=t and B[i]>=t) or (A[i]==t) or (B[i]==t):
        count+=1

    i+=1
print(count)

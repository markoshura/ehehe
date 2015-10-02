n=int(input())
i=3
A1=[1]
A2=[1,1]
A0=[0]*8
if n==1:
    print(A1)
    print(A2)
else:
    print(A1)
    print(A2)
    A0=A2[::]
    while i<n+1:
        k=1

        while k<i-1:
            A0[k]=0
            A0[k]=A2[k-1]+A2[k]
            k+=1
        A0.append(1)
        print(A0)
        A2=A0[::]
        i+=1

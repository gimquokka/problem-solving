a,m,d,t = map(int,input().split())

def Seq(n):
    if n==1:
        return a
    return  m*Seq(n-1)+d



print(Seq(t))

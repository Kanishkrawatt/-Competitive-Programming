n = int(input())                      #n = number of Test Cases
for i in range(n):
    N,Q = map(int,input().split())    #N =Number Of boxes , Q = Num of Queries 
    Maggipack = list(map(int,input().split()))
    Maggipack.sort(reverse=True)
    for j in range(Q):
        X = int(input())
        sum = 0
        k=0
        flag = 0
        for k in range(N):
            if(X>sum):
                sum += Maggipack[k]
                flag += 1
            else:
                break
        if (flag<N):
            print(flag)
        else:
            if(X<=sum):
                print(N)
            else:
                print("-1")


                
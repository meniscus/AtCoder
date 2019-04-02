# やりたかったこと
# a(1)は1個、a(2)は2個、a(3)からa(k-2)は3個、a(k-1)は2個、a(k)は1個 、
# みたいな足し方
# K倍に至らないケースがあるので、その場合わけが難しそう

def main() :
    N,K = [int(i) for i in input().split()]
    l = [int(i) for i in input().split()]

    # sum = 0
    # for i in range(1,N+1) :
    #     print((min([i-1,N-i,K-1])+1))
    #     sum += l[i-1] * (min([i-1,N-i,K-1])+1)
    
    # print(sum)

    sum = 0
    for i in range(K-1) :
        # print("l[i] * (i+1) : " + str(l[i]) + " * " + str((i+1)))
        sum += l[i] * (i+1)
        # print("l[N-1-i] * (i+1) : " + str(l[N-1-i]) + " * " + str((i+1)))
        sum += l[N-1-i] * (i+1)
    
    # for i in range(K,N-K+1) :
    for i in range(K-1, N-K+1) :
        # print("l[i] * K : " + str(l[i]) + " * " + str(K))
        sum += l[i] * K
    
    print(sum)

main()
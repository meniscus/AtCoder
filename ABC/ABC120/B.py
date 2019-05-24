import fractions as frac

A,B,K = [int(i) for i in input().split()]

cd_list = []
for i in range(1,max(A,B)+1) :
    if (A % i == 0 and B % i == 0) :
        cd_list.append(i)
        # if (len(cd_list) >= K) :
        #     break

print(cd_list[-K])
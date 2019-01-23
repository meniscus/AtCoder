def main() :
    N = input()
    for i in range(len(N)) :
        if (N[i] != N[-1 * i - 1]) :
            print("No")
            return
    
    print("Yes")

main()
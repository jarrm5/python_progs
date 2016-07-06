def print_subsets(X):
    for i in range(0,len(X)):
        start = 0
        while(start <= i):
            Z = []
            for j in range(start,i+1):
                Z.append(X[j])
            print(Z)
            start += 1
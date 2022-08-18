if __name__ == "__main__":
    p = int(input())
    a = 1600
    original = p

    while (p >= 0.1 *original): 
        n = 0.01*p
        m = 0.06*p
        p = p + n - m
        
        print('{},{:.0f},{:.0f},{:.0f}'.format(a,n,m,p))

        a += 1
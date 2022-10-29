lastNumber = 1;

def ex5():
    signal = 1;
    h = 1;
    s = 1;
    p = 2;

    lastNumber = 1;

    n = int(input("N: "));

    for i in range(2, n+1):
        h += calc_h(i, signal);
        s += calc_s(i, signal*-1);

        if is_prime(i):
            lastNumber+=2;
            p += calc_p(i,lastNumber);

        signal *= -1;
    
    print("H: " + str(h))
    print("S: " + str(s))
    print("P: " + str(p))

def calc_h(n, signal):
    return signal * (((n * 2) - 1) / n)

def calc_s(n, signal):
    return signal * (n/(n*n))

def calc_p(n, lastNumber):
    return n/(lastNumber**3)

def is_prime(num):
    if num == 1 or num == 2:
        return False;
    
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            return False
            
    return True

ex5()
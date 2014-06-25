
    
def getPrimes(n):
    primes = []
    i = 2
    while i * i <= n:
        while n % i == 0:
            primes.append(i)
            n /= i
        i += 1
    if n > 1:
        primes.append(n)
    return primes

def getFactors(n):
    factors = []
    x = int(n**0.5)
    #TODO Randomize or pick a better way to find divisions
    while n%x != 0 and x > 2:
        x -= 1
    if n%x == 0:
        if x != 1 and x != n:
            factors.append([x, getFactors(x)])
        y = n/x
        if y != 1 and y != n:
            factors.append([y, getFactors(y)])
    return factors

if __name__ == "__main__":
    n = int(input("> "))
    p = getPrimes(n)
    print "Primes: " + str(p)
    print getFactors(n)

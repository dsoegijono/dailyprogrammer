
    
def get_primes(n):
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

def get_factors(n):
    factors = []
    x = int(n**0.5)
    #TODO Randomize or pick a better way to find divisions
    while n%x != 0 and x > 2:
        x -= 1
    if n%x == 0:
        if x != 1 and x != n:
            factors.append([x, get_factors(x)])
        y = n/x
        if y != 1 and y != n:
            factors.append([y, get_factors(y)])
    return factors
    
def print_inverse_tree(primes, level):
    s = ""
    for i in range(len(primes)):
        if i%2 == 0:
            s += " " * (level*2)
        else:
            s += "x"
            s += "-" * level
        s += str(primes[i])
        if i%2 == 0 and i < len(primes)-1:
            s += "-" * level
        else:
            s += " " * level
    print s
    a = []
    if len(primes) > 1:
        x = 0
        while x < len(primes)-1:
            a.append(primes[x] * primes[x+1])
            x += 2
        if x == len(primes)-1:
            a.append(primes[x])
    if a:
        print_inverse_tree(a, level+1)

def print_tree(factors):
    #print "Factors = " + str(factors)
    #print "Level = " + str(level)
    if not factors:
        return
    for node in factors:
        if not node:
            return
        else:
            print node[0]
            del node[0]
            print_tree(node)
        #print_tree(i)
        #print node
    #print factors[0]
    #print_tree(factors[0])

if __name__ == "__main__":
    n = int(input("> "))
    p = get_primes(n)
    #print_inverse_tree(p, 1)
    print_tree(get_factors(n))
    #print get_factors(n)
"""
http://www.reddit.com/r/dailyprogrammer/comments/284mep/6142014_challenge_166b_easy_planetary_gravity/
"""

import math

G = 6.67e-11

def volume(r):
    return 4 * math.pi * r**3 / 3

def force(m1, m2, r):
    return G * m1 * m2 / r**2

def main():
    filename = raw_input("Please enter input file name. Enter 'manual' to input manually.\n--> ")
    
    planets = []
    
    if filename == "manual":
        m1 = int(raw_input("Mass: "))
        n = int(raw_input("Number of planets: "))
        if n > 0:
            print "Enter planet(s) information:"
        for i in range(n):
            planets.append(raw_input()) #TODO invalid input?
        for p in planets:
            print p
    else:
        file = open(filename, 'r')
        m1 = int(file.readline())
        n = int(file.readline())
        for i in range(n):
            planets.append(file.readline())
    print ""
    
    for p in planets:
        planet = p.split()
        radius = float(planet[1][:-1])
        m2 = volume(radius) * float(planet[2])
        print planet[0][:-1] + ": " + str(force(m1, m2, radius) )

if __name__ == "__main__":
    main()
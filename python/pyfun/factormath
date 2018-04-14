#!/usr/bin/env python3
def prime_factors(n): #prime factorizes a number, used as the basis for many other functions
    i = 2
    primetree = []
    while i**2 <= n:
        if n % i > 0: 
            i += 1
        else:
            n //= i
            primetree.append(i)
    if n > 1:
        primetree.append(n)
    return sorted(primetree)

def mult_list(l): #multiplies the contents of a list, used in many functions
    product = 1
    for x in l:
        product *= x
    return product

def factors(n): #uses the primetree to produce factors. Designed for high speed with high numbers.
    primetree = prime_factors(n)
    if len(primetree) == 1:
        return []
    elif len(primetree) == 2:
        return primetree
    else:
        segments = []
        new_segment = []
        for x in range(0, len(primetree)): #initializes the segment list
            if primetree[0:x]+primetree[x+1:len(primetree)] not in new_segment:
                new_segment.append(primetree[0:x]+primetree[x+1:len(primetree)]) #all unique combinations of numbers 
        segments.append(new_segment)
    
        for x in range(0, (len(primetree)-3)): #continues with the segment list, will only run if len(primetree) > 3
            new_segment = []
            for l in segments[-1]:
                for x in range(0, len(l)):
                    if l[0:x]+l[x+1:len(l)] not in new_segment:
                        new_segment.append(l[0:x]+l[x+1:len(l)]) #all unique combinations of numbers 
            segments.append(new_segment)
        
        #the following code converts the list segements into numbers
        factor_list = []
        for x in segments:
            for y in x:
                factor_list.append(mult_list(y))
        for x in primetree:
            if x not in factor_list:
                factor_list.append(x)
        return sorted(factor_list)
    
def factor_separate(*args): #metabolic pathways for gcf and lcm
    primetrees = []
    for x in args:
        primetrees.append(prime_factors(x))
    common_primefacs = []
    for x in primetrees[0]:
        common = True
        for y in primetrees: #checks if x is in all of the other lists
            if x not in y:
                common = False
                break
        if common == True: #if x in all lists
            common_primefacs.append(x)
            for y in primetrees[1:]: #avoids messing up the first primetree, it will be fixed later
                y.remove(x)
    for x in common_primefacs:
        primetrees[0].remove(x) #cleans up the first primetree
    uncommon_primefacs = []
    for x in primetrees:
        for y in x:
            uncommon_primefacs.append(y)
    return common_primefacs, uncommon_primefacs

def gcf(*args): #greatest common factor
    common, uncommon = factor_separate(*args)
    return mult_list(common)

def lcm(*args): #least common multiple
    l = sorted(list(args))[::-1]
    m = l #the arguments without multiples
    for x in range(0, (len(l) - 1)):
        for y in l[x+1:]:
            if l[x]%y == 0:
                m.remove(y) #all arguments that are factors of other arguments will be removed
    n = m[0] #the LCM of the numbers, going 2 at a time
    for x in range(1, len(m)):
        common, uncommon = factor_separate(*tuple([n, m[x]]))
        n = mult_list(common)*mult_list(uncommon)
    return n

if __name__ == "__main__":
    while True:
        func = input('> ').lower()
        if func in ['prime factors', 'prime factorization', 'primefac', 'primetree']:
            n = int(input('Enter a number to prime factorize > '))
            print(prime_factors(n))
        elif func == 'factors':
            n = int(input('Enter a number to find the factors of > '))
            print(factors(n))
        elif func in ['gcf', 'greatest common factor', 'gcd', 'greatest common divisor']:
            args = [int(x) for x in input('Enter numbers separated by commas and spaces > ').split(', ')]
            print(gcf(*tuple(args)))
        elif func in ['lcm', 'least common multiple']:
            args = [int(x) for x in input('Enter numbers separated by commas and spaces > ').split(', ')]
            print(lcm(*tuple(args)))
        else:
            print("Valid functions include 'primefac', 'factors', 'gcf', and 'lcm'")

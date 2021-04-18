import math

def isPrime(a,b):

    if a == 2 and b == 2:
        prime = True
    elif a % 2 == 0 or a <= 1 and b % 2 == 0 or b <= 1 :
        prime = False
    else:
        sqra = int(math.sqrt(a)) + 1
        sqrb = int(math.sqrt(b)) + 1

        for divisor in range(3, sqra, 2):
            if a % divisor == 0 :
                prime = False
                break
        else: 
            prime = True

        for divisor in range(3, sqrb, 2):
            if b % divisor == 0 :
                prime = False
                break
        else: 
            prime = True

    if prime:
        print("Les deux nombres sont premiers ", prime)
    else:
        print("Un des deux nombres n'est pas premier ", prime)
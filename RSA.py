# THIS IS MY PROJECT ON CRYPTOGRAPHY BASICS : ENCRYPTION AND DECRYPTION USING RSA


import random
text =  input("Enter the message: ")

def GCD(x,y): # assertion: the gcd of two numbers x, y is x when y <= 0
    while y > 0:  # Invarient :  0 < y < x and  x = (q * y) + rem 
        q = x // y
        rem = x % y
        x, y = y, rem
    return x # final assertion : the gcd of two numbers is x.
# Time Complexity: O(log y) as the number of operations depend upon mod of x and y where y is min(x, y)
# Space Complexity: O(1) = constant as the instantaneous value of 2 variables are required to be stored.

def choose_e(m):    # assertion : the value of e is the number whose gcd with phiOfN i.e m  is 1.
    num = random.randint(3,m)  #   (because 1 < e <= m)  
    for i in range (num, m, 2):   # invarient :  num <= i <= m  where i is the value of e.
        if(GCD(m,i) == 1):       # calls the GCD function to check if the GCD of m and i is 1 or not 
            return i           # final assertion : the value of e is i which is co-prime with m
# Time Complexity : O(m).

def Euclidean_gcd(a,b):   # assertion : The euclidean_gcd of (a,b) is 1.
    s, prev_s = 0, 1  # Initialize the values as the base case for the recurrence
    t, prev_t = 1, 0  # Initialize the values as the base case for the recurrence
    while(a!= 0):     # Invarient : ( 0 < a < b) ^  b = (quotient * a) + rem  and uses the formula :  gcd = (prev_t * a + prev_s * b)
        quotient  = b // a  # a is E which is always smaller than m
        rem = b % a 
        b, a = a, rem
        prev_s, s = s, prev_s - (quotient * s)
        prev_t, t= t, prev_t - (quotient * t)
    return b, prev_s, prev_t                     # final assertion : (b = gcd) and prev_s and prev_t(which is d) are the coefficient of b = m (phiOfN) and (a = E) respectively. (a*s + b*t = 1)
# Time Complexity: O(log a) where a is the minimum between a and b

def Multiplicative_Inverse(x, y):
    gcd, s, t = Euclidean_gcd(x, y) # assertion : gcd of two numbers with the coefficients of x and y
    if (t < 0): # To make sure that negative modulus comes back to its positive modulus equivalent. For example : -4 mod 7 = 3 mod 7  (because : -4 + 7 = 3)
        t += m     
    return t                  # final assertion : The t is the part of private key
E, m = 0, 0

d = Multiplicative_Inverse(E, m)      # The Modular Multiplicative Inverse of e and phiOfN = m , which is actually the private key 
def sqr(x):
    return x*x

def Modular_Exponentiation(m,e,n): # assertion : The modular exponentiation of m^e mod n = ((m ^ e/2) mod n * (m mod e/2) mod n ) mod n using Recursion 
    if (e == 0):
        return 1
    elif (e % 2 == 0):
       return sqr((Modular_Exponentiation(m, e/2, n)%n))%n   
    else:
       return (m%n * Modular_Exponentiation(m, e-1, n))%n   # final assertion : (a * b)mod n = [(a mod n) * (b mod n)] mod n
# Time Complexity : Using the concept of squaring and dividing: multiplying the digits of m with log e times, to get m^e mod n it takes, O(log n^3). 

list_cipher = []   # empty list to store all the encrypted integer values of each character of the message.
def encrypt(E, N, text):  # assertion : The message entered gets encrypted to its integer equivalent of each characters of the message and gets stored in list_cipher 
    for i in text:     #  Invarient : i < length of text entered.
        M = ord(i)   # function to convert the character to its integer value
        list_cipher.append(pow(M, E, N)) 
        #list_cipher.append(Modular_Exponentiation(M, E, N))   # the inbuilt function pow(M, E, N) makes it more efficient. 
    return list_cipher
# Time Complextiy : if length of text= L , O(L) * O(log E). = O( L * log E)

list_decrypt= []                      # list to contain the decrepted values
def decrypt(N, list_cipher):          # It takes the list of cipher values in the form of integers returned by encrypt() function 
    for i in list_cipher:
        list_decrypt.append(chr(pow(i, d, N)))  
        #list_decrypt.append(chr(Modular_Exponentiation(i, d, N)))     # pow() is REPLACED WITH MODULAR_EXPONENTION 
        # appends the each char converted value of correspoinding integer to a string
    finalstring = "".join(list_decrypt)        # Converts the list of characters into the String
    return finalstring
# Time Complexity : O(L) * O(log d) = O( L * log d)

def Fermats_prime_test(p, k):    # assertion :  The Fermat's test is made to run k number of times to check the Primality.
    if p == 2:   # It is a base case : trival statement. 
        return True

    if p % 2 == 0:
        return False

    for i in range(k):
        a = 0        # Initially a= 0 so as to force the while condition to be false for the first time.
        while( a <= 1 or a >= p-1 ):   # Because Fermats Theorem :   1 < a < p-1 where a is a natural num.
            a = random.randint(1, p-1)
        # p is the number whose primality is to be tested.
        if (pow(a, p-1, p) != 1):    # Fermat's Theorme : a ^ p-1 mod p = 1 ; If not "1" then it is not a prime num
             # pow() is REPLACED WITH modular_Exponention function
            return False
            
    return True     # If the 'if' condition is false then it means the if condition does not execute i.e it has rem as 1 and returns true after coming out of the loop.
# Time Complexity : O(k) * O(log p) = O(k log p)
    
def generate_number(size= 1024):  # assertion: generates the random large number of bit size= 1024
    number = random.randrange(2**(size-1) + 1, 2**size - 1)    # the number of bit size = size is from range ( 0 to 2 ^ n - 1 )
    return number 

# The Program starts from here
p = generate_number()
while(not Fermats_prime_test(p, 5)):  
     # if Fermat's test returns False then only generate the random number again as it was not prime.
    p = generate_number()

q = generate_number()
while(not Fermats_prime_test(q, 5)):
    q = generate_number()
n = p * q
m = (p-1) * (q-1)   # assertion : the value of PhiOfN = m 
E = choose_e(m)
d = Multiplicative_Inverse(E, m)   # assertion : d is the modular multiplicative inverse of E and m using the Extended _ Euclidean Algorithm.
public_key = (E, n)
private_key = (d, n)
print ("The generated public keys are : ", public_key)
print ("The generated Private keys are :",private_key)
print("The list of encrypted values for the entered message are",encrypt(E, n, text))
print("The decrypted value for the message :",decrypt(n, list_cipher))




 #  CITATIONS :   1)  https://www.youtube.com/watch?v=bE-MxVEQyR4&list=WL&index=3
 #               2)  https://www.youtube.com/c/WilliamYFeng
 #               3)  https://gist.github.com/Ayrx/5884802
# https://mathworld.wolfram.com/FermatsLittleTheorem.html#:~:text=Fermat%27s%20Little%20Theorem%20%20%202%20%20,%20%2087%20%2015%20more%20rows%20


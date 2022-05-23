import random
import time

def passwords_quantity(password_length):
    return 2**password_length

length_password=[2**i for i in range(3,13)]

for i in length_password:
    print (f'{passwords_quantity(i)}\n')

def random_password(password_length):
    return random.getrandbits(password_length)

A = []

for i in length_password:
    n = random_password(i)
    A.append(n)
    print (f'{n}\n')  

for password in A:
    n = 0
    t1 = time.perf_counter()
    while n != password:
        n += 1
    t2 = time.perf_counter()
    print(f'{n} - {(t2 - t1)*1000}')

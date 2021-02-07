p=int(input('Enter the prime number:'))



def power(a,b,c):
    if b==1:
        return int(a)
    else:
        return int((a**b)%c)

def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

def primRoots(modulo):
    roots = []
    required_set = set(num for num in range (1, modulo) if gcd(num, modulo) == 1)

    for g in range(1, modulo):
        actual_set = set(pow(g, powers) % modulo for powers in range (1, modulo))
        if required_set == actual_set:
            roots.append(g)
    return roots


primitive_roots = primRoots(p)
print(primitive_roots)


root=int(input('Enter the any primitive root of upper list:'))

a=int(input('Enter the secret of key of A:'))

b=int(input('Enter the secret key of B:'))

x=power(root,a,p)
y=power(root,b,p)

ask=power(y,a,p)
bsk=power(x,b,p)

print('The secret key of A: %s'%ask)
print('The secret key of B: %s'%bsk)

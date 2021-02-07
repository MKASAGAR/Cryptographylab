def multiply(A, B, m, n):
    prod = [0] * (m + n - 1)

    for i in range(m):

        for j in range(n):
            prod[i + j] += A[i] * B[j]

    return prod


def add(A,B,m,n):
    size= max(m,n)
    sum=[0 for i in range(size)]
    for i in range(0,m,1):
        sum[i]=A[i]
    for i in range(n):
        sum[i]+=B[i]
    return sum

def minus(A,B,m,n):
    size= max(m,n)
    sum=[0 for i in range(size)]
    for i in range(0,m,1):
        sum[i]=A[i]
    for i in range(n):
        sum[i]-=B[i]
    return sum

##########print polynomial


def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end="")
        if (i != 0):
            print("x^", i, end="")
        if (i != n - 1):
            print(" + ", end="")

#################Input#############

ra=int(input('Enter the value of polynomial A :'))

A=[]
for j in range(ra):
    data= int(input('Enter the coefficient of x to the power '+ str(j) +' :'))
    A.append(data)

print(A)

rb=int(input('Enter the value of polynomial B :'+ '\n'))

B=[]
for j in range(rb):
    data= int(input('Enter the coefficient of x to the power '+ str(j) +' :'))
    B.append(data)

print(B)

m = len(A)
n = len(B)
size=max(m,n)


print("First polynomial is ")
printPoly(A, m)
print("\nSecond polynomial is ")
printPoly(B, n)

prod = multiply(A, B, m, n)

print("\nProduct polynomial is ")
printPoly(prod, m + n - 1)
print('\n')
ADD=add(A,B,m,n)

Minus=minus(A,B,m,n)
print('\n')
print('Addition of two polynomial:')

printPoly(ADD,size)
print('\n')
print('Subtraction of two polynomial:')
printPoly(Minus,size)




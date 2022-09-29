#1 task
#1
n = int(input("Enter the number: "))
arr = [[int(input()) for j in range(n)] for i in range(n)]
print("Enter the list: ", arr)
s = 0
count= 0
for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr[i])):
        if arr[i][j] > 0:
            s += arr[i][j]
            count += 1
print("Sum of positive elements: ", s)
print("Number of positive elements: ", count)




#2 
n = int(input("Enter the number: "))
b= [[int(input()) for j in range(n)] for i in range(n)]
for i in b:
    for j in i:
        print(j, end = " ")
    print()
for i, row in enumerate(b):
    max = min = 0
    for j, elem in enumerate(row):
        if elem > row[max]:
            max = j
        if elem < row[min]:
            min = j
    row[max], row[0] = row[0], row[max]
    row[min], row[-1] = row[-1], row[min]
print(b)


#2 task 
#1


N = 3
A = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
s = 0
for i in range(N):
    s += A[0][i]

b = "magic square"
for i in range(N):
    s1 = 0
    s2 = 0
    for j in range(N):
        s1 += A[i][j]
        s2 += A[j][i]
    if s1 != s or s2 != s:
        b = "NO"
        break
print(b)


#2 


N = 3
M = 3

A = [[1, 2, 3],[4, 5, 6],[7,8, 9]]
print("Current matrix: ")
for i in A:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(N):
    tmp = A[i][0]
    A[i][0] = A[i][M-1]
    A[i][M-1] = tmp

for i in range(N):
    for j in range(M):
        print("%2d " % A[i][j], end='')
    print()



#3 task
#1

N = 3
A = [[1, 2, 3],[2, 5, 6],[3, 6, 4]]
b = "symmetric"
for i in range(N):
    for j in range(N):
        if A[i][j] != A[j][i]:
            b = "no"
            break
print(b)




#2
from random import randint
 
a = [[randint(10, 99) for i in range(6)] for j in range(6)]
for row in a:
    print(*map('{:2d}'.format, row))
print()
 
max_elem = a[0][0]
ie = je = 0
for i in range(len(a)):
    for j in range(len(a[0])):
        if a[i][j] > max_elem:
            max_elem = a[i][j]
            ie = i 
            je = j 
a[0], a[ie] = a[ie], a[0]
a[0][0], a[0][je] = a[0][je], a[0][0]
for row in a:
    print(*map('{:2d}'.format, row))


#4 task

   #1
   from random import randint
size = int(input('Array size: '))
matrix = [[randint(1,99) for x in range(size)] for _ in range(size)]

for i in range (size): print(*matrix[i])

maxsum=[0]*size
for i in range (size): maxsum[i]=sum(matrix[i])
print (f'MAX row {maxsum.index(max(maxsum))+1} sum {max(maxsum)}')
print (f'MIN row {maxsum.index(min(maxsum))+1} sum {min(maxsum)}')

#2

a = [[1,2,-3],[-1,2,3],[1,-2,3]]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()
a = [[1 if x>0 else 0 for x in i] for i in a]
for i in range(len(a)):
    print(*[a[i][x] if x<=i else '' for x in range(len(a[i]))],'')




#5 task
   #1


n=int(input("n: "))
m=int(input("m: "))
a= [[int(input()) for j in range(n)] for i in range(n)]
print(list(map(sorted, a)))

def qsort(a): 
    if len(a) <= 1:
        return a
    else:
        return qsort( [x for x in a[1:] if x < a[0]]) + [a[0]] + qsort([x for x in a[1:] if x >= a[0]] )
qsort(a)




#6 task
#1

import random
n=int(input("n: "))
m=n
a=[[random.randrange(10) for i in range(n)] for j in range(m)]
for i in a:
    for j in i:
        print(j, end=" ")
    print()
print()

for i in range(n):
    print(a[i],max(a[i]))
for i in range(m):  
    x=[x[i] for x in a]
    print(min(x), end=" ")
print("\n")

#2
import random
n=int(input("Enter n: "))
arr=[[random.randrange(10) for i in range(n)] for j in range(n)]
for i in arr:
    print(i)
print()
 
a = sum(arr, [])
max1 = max(a[::n+1])
max2 = max(a[n-1::n-1][:n])
if max1 > max2:
    i1 = j1 = a[::n+1].index(max1)
else:
    i1 = a[n-1::n-1][:n].index(max2)
    j1 = n - 1 - i1
arr[n//2][n//2], arr[i1][j1] = arr[i1][j1], arr[n//2][n//2]
 
for i in arr:
    print(i)



#8 task 
#1
n = int(input('Enter the N:))

k = int(input('Enter the K:))

arr = [[int(input()) for j in range(n)] for i in range(n)]

for i in range(n):

   for j in range(n):

       if k == i:

           arr[i][j] = arr[i][j] / arr[i][i]

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))


#2
n = int(input())

arr = [[int(input()) for j in range(n)] for i in range(n)]

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))

arr = list(zip(*arr))

print('\n'.join([''.join([str(f'{i:4}') for i in row]) for row in arr]))


#9 task
#1
 matrix = input().split("],[")

matrix[0] = matrix[0][1:]

matrix[len(matrix) - 1] = matrix[len(matrix)-1][:len(matrix[len(matrix) - 1])-1]

newMatrix = []

for arr in matrix:

   line = list(map(int, arr.split(",")))

   newMatrix.append(line)

matrix = newMatrix

print(matrix)


k = int(input("k: "))

maximum = matrix[0][0]

counter = 0

for arr in matrix:

   for num in arr:

       if num % k == 0:

           if maximum < num:

               maximum = num

           counter += 1

print("{0} the number of multiples of numbers {1}".format(counter, k))

if maximum != 0:
              print("The maximum number is a multiple of {0} - {1}".format(k, maximum))

else:

   print(" there are no multiple numbers {0}".format(k))





#12 task
#1

arr = [[1, 2, 3, -4], [2, -3, -1, -8], [3, -1, 7, 7], [-4, -8, 2, -8]]
for i in arr :
    print(*map('{:2d}'.format, i))
print()
n = 4
arr_rev = list(map(list,zip(*arr)))
for i in range(n) :
    for j in range(n) :
        if arr[i] == arr_rev[j] :
            print(i+1, 'row and ', j+1, 'column equal')


#2
m = [[2, 3, 4, 5, 3],
     [7, 7, 7, 7, 7],
     [3, 2, 3, 2, 3],
     [6, 6, 6, 6, 6],
     [1, 1, 1, 1, 1], ]
 
for i in range(len(m) - 1):
    for j in range(len(m[0])):
        m[i][j] -= m[-1][j]
 
for i in m:
    print(*i)





#13 task
#1
import random
 
N = int(input('enter the number:'))
M = int(input('enter the number:'))
B = [[random.randrange(10) for i in range(M)] for j in range(N)]
 
for i in B:
    print(*map('{:3}'.format, i))
 
for i in range(0, N): 
    k = min(B[i])
    print('The minimum of the row %d is %d' % (i+1, k))




#2
n = int(input())
m = int(input())
a = []
 
for i in range(n):
    a.append(list(map(int, input().split())))
 
max1 = max(max(a))
ind_max1 = a.index(max(a))
ind_max2 = a[ind_max1].index(max1)
 
min1 = min(min(a))
ind_min1 = a.index(min(a))
ind_min2 = a[ind_min1].index(min1)
 
a[ind_min1][ind_min2], a[ind_max1][ind_max2] = max1, min1
 
for i in a:
    print(*i)


#14 task

    #1
from random import randint
 
m = 3
l = [[randint(-10, 10) for j in range(5)] for i in range(5)]
print(*l, sep='\n')
print()
 
ll = []
for i in range(len(l)):
    ll.append(l[i][i])
 
maxid = ll.index(max(ll))
l[maxid], l[m] = l[m], l[maxid]
print(*l, sep='\n')

    
#2
n = int(input('enter the number'))
mat = [[0]*n for i in range(n)]
st, m = 1, 0
mat[n//2][n//2]=n*n
for v in range(n//2):
    
    for i in range(n-m):
        mat[v][i+v] = st
        st+=1
        #i+=1
   
    for i in range(v+1, n-v):
        mat[i][-v-1] = st
        st+=1
        #i+=1
    
    for i in range(v+1, n-v):
        mat[-v-1][-i-1] =st
        st+=1
        #i+=1
    
    for i in range(v+1, n-(v+1)):
        mat[-i-1][v]=st
        st+=1
        
    m+=2

for i in mat:
    print(*i)


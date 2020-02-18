
a = float(input())

k = 1

s = 0

while s < a:

    s = s + 1.0/k

    k = k + 1

print(k-2)

k = 1
s = 0
s = 1
k = 2
s = 1+1/2
k = 3
s = 1+1/2+1/3
k = 4
s = 1+1/2+1/3+1/4
k = 5
print(k-2)
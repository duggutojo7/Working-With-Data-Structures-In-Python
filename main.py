# WAP to perform different set operations.

E={0,1,2,3}
N={4,5,6,8}
U=E.union(N)
print(U)
F={0,1,5,7}
G={1,7,6,9}
H=F.intersection(G)
print(H)
A={9,8,7}
B={6,5,4}
C=A.difference(B)
print(C)
D=A.symmetric_difference(B)
print(D)

my_tuple=()
print(my_tuple)
thistuple=(1,2,3,4,5)
print(thistuple)
thistuple=(1,2,3),"Avdhi",(5,6,7)
print(thistuple)
thistuple=(1,2,3),"Avdhi",(5,6,7),[5,9,8]
print(thistuple[0])
print(thistuple[3])
print(thistuple)
thistuple=23,'CSIT',8
print(thistuple)
a,b,c=thistuple
print(a)
print(b)
print(c)
a=23
b='CSIT'
c=87
print(a)
print(thistuple)
print(type(thistuple))
thistuple=('Avdhi')
print(type(thistuple))
thistuple=(1,2,3),"Avdhi",(5,6,7),[5,9,8]
print(thistuple)
print(thistuple[0])
print(thistuple[2])
print(thistuple[0][2])
print(thistuple[1][3])
print(thistuple[-1][-2])
print(thistuple[:])
print(thistuple[-2:-2])
print(thistuple[0:1])
print(thistuple[:-1])
thistuple=(1,2,8)+(2,7,4)
print(thistuple)
print(('Avdhi',)*5)
print((95)*2)
print(thistuple)
del(thistuple)
thistuple=('A','v','d','h','i')
print(thistuple)
print(thistuple.count('A'))
print(thistuple.count('y'))
print(thistuple.index('A'))
print('a' in thistuple)
print('z' in thistuple)
for m in ('Avdhi','Riddh'):
    print('hello',m)
a=(6,8,9)
for n in a:
    print(2*n)
b=[5,9,4]
b.sort()
print(b)
b=sorted(a)
a=(6,3,7)
b=sorted(a)
print(b)
print(a)

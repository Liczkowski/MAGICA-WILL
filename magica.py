a = ['A1','A2','A3','A4','A5','A6','A7']
b = ['B1','B2','B3','B4','B5','B6','B7']
c = ['C1','C2','C3','C4','C5','C6','C7']


print("A  B  C")
for i in range(0,7):
    print(a[i],b[i],c[i])

First = input("Em qual coluna está seu numero? (1,2,3): ")


if First == '1':
    Embaralhar1 = b+a+c
elif First == '2':
    Embaralhar1 = a+b+c
else:
    Embaralhar1 = a+c+b

n = 3
Embaralhar2 = [Embaralhar1[i::n] for i in range(7)]

a = Embaralhar2[0]
b = Embaralhar2[1]
c = Embaralhar2[2]
print("A  B  C")
for i in range(0,7):
    print(a[i],b[i],c[i])

second = input("Em qual coluna está seu numero? (1,2,3): ")


if second == '1':
    Embaralhar3 = b+a+c
elif second == '2':
    Embaralhar3 = a+b+c
else:
    Embaralhar3 = a+c+b

n = 3
Embaralhar4 = [Embaralhar3[i::n] for i in range(7)]


a = Embaralhar4[0]
b = Embaralhar4[1]
c = Embaralhar4[2]
print("A  B  C")
for i in range(0,7):
    print(a[i],b[i],c[i])

third = input("Em qual coluna está seu numero? (1,2,3): ")
print("A, B ou C?")

if third == '1':
    Embaralhar5 = b+a+c
elif third == '2':
    Embaralhar5 = a+b+c
else:
    Embaralhar5 = a+c+b

print(f'Sua carta é:  {Embaralhar5[10]} ')
final = input("yes or no? ")
if final == 'yes':
    print("parabens")
else:
    print("Repita o processo")

n=int(input('Dati numarul de elemente din vector='))
a=[]
print('Introduceti ',n,' elemente pentru vectorul creat')
# if n<10:
for i in range(0,n):
    x=int(input('Dati elementul='))
    a.extend([x])
print(a)
print('a)  afişează pe ecran componentele tabloului la un interval de 5 poziţii;')
print(a[:5])
print('b)  afişează pe ecran numerele în ordinea inversă a introducerii în calculator;')
for i in range(len(a),0, -1):
    print(a[i-1])
print('c)  sortează componentele tabloului în ordine descrescătoare;')
b=sorted(a)
b.sort(reverse=True)
print(b)
print('d)  afişează pe ecran doar componentele pare;')
c=[]
for i in range(0,len(a)):
    if a[i]%2==0:
        y=a[i]
        c.extend([y])
print(c)
print('e)  afişează pe ecran media aritmetică a componentelor pare;')
print(sum(c)/len(c))
print('f)  afişează pe ecran doar componentele impare;')
d=[]
for i in range(0,len(a)):
    if a[i]%2!=0:
        y=a[i]
        d.extend([y])
print(d)
print('n)  creează un tablou nou, format doar din componentele divizibile cu 3 ale tabloului introdus de la tastatură;')
at = []
for i in a:
    if i % 3 == 0:
        at.append(i)
print('m)  creează un tablou nou, format doar din componentele pare ale tabloului introdus de la tastatură;')
egal = []
for i in a:
    if i % 2 == 0:
        egal.append(i)
print('i)  afişează pe ecran poziţiile (indicii) componentelor impare negative;')
for i in a:
    if i < 0 and i%2==1:
        print(a.index(i))
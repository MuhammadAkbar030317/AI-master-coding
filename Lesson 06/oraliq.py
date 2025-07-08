# 1. Agar berilgan son 2 ga bo’linsa yaxshi aks xolda yomon degan sozni ekrang 
a=4
if a%2==0:
    print("Yaxshi")
else:
    print("Yomon")


# 2. Agar berilgan son musbat bo’lsa yaxshi aks xolda yomon degan sozni ekrang 
b=26
if b>0:
    print("Yaxshi")
else:
    print("Yomon")

# 3. Agar berilgan 5 ga va 3 ga bolinsa yaxshi aks xolda yomon degan sozni ekrang 
c=17
if (c%5==0) and (c%3==0):
    print("Yaxshi")
else:
    print("Yomon")

# 4. Agar berilgan so’zning bosh xarfi ‘a’ bolsa yaxshi aks xolda yomon degan sozni ekrang 
text= "Salom"
if text[0]=="a":
    print("Yaxshi")
else:
    print("Yomon")

# 5. Agar berilgan so’zning oxirgi xarfi ‘a’ bolsa yaxshi aks xolda yomon degan sozni ekrang chiqaring 
so="Samarqand"
if so[-1]=="a":
    print("Yaxshi")
else:
    print("Yomon")

# 6. Agar berilgan so’zning bosh xarfi ‘b’ va oxirgi xarfi ‘a’ bolsa yaxshi aks xolda yomon degan sozni ekrang 
s="bo'lsa"
if (s[0]=="b") and(s[-1]=="a"):
    print("Yaxshi")
else:
    print("Yomon")

# 7. Berilgan sonning musbat ekanligini isbotlang
a= 30
b=a>0
print(b)

# 8. Berilgan sonning manfiy ekanligini isbotlang
c=-23
d=c<0
print(d)

# 9. Berilgan sonning nol ekanligini isbotlang
number=0
comp= 0==0
print(comp)

# 10. Berilgan sonning 2 ga bolinishini isbotlang
a=10
bolish=10%2==0
print(bolish)

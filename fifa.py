'''
Csapat;Helyezes;Valtozas;Pontszam
Anglia;4;0;1662
Argentína;10;0;1614
'''
class Fifa:
  def __init__(self,sor):
    Csapat,Helyezes,Valtozas,Pontszam = sor.strip().split(";")
    self.Csapat = Csapat
    self.Helyezes = int(Helyezes)
    self.Valtozas = int(Valtozas)
    self.Pontszam = int(Pontszam)


lista=[]
with open('fifa.txt', encoding='latin2')as f:
  f.readline()
  for sor in f:
    lista.append(Fifa(sor))

#3 feladat
csapatok=[]
for sor in lista:
  csapatok.append(sor.Csapat)
print(f"Csapatok száma: {len(csapatok)}")

#4 feladat
pontok=[]
for sor in lista:
  pontok.append(sor.Pontszam)

ossz=sum(pontok)
atlag=ossz/len(pontok)
atlag=f"{atlag:.2f}"
atlag=atlag.replace('.',',')
print(f"A csapatok átlagos pontszáma: {atlag}")

#5 feladat
valtozasok=[(sor.Valtozas,sor) for sor in lista]
#nagy, adat = max(valtozasok)
legtobbetjavitocsapat=max(lista,key=lambda x:x.Valtozas)
legtobbetjavitocsapat.Csapat
legtobbetjavitocsapat.Helyezes
legtobbetjavitocsapat.Pontszam
print(f"""A legtöbbet javító csapat:
          Csapat: {legtobbetjavitocsapat.Csapat}
          Helyezés: {legtobbetjavitocsapat.Helyezes}
          Pontszam: {legtobbetjavitocsapat.Pontszam}""")


#6 feladat
van_e=False
for sor in lista:
  if sor.Csapat =="Magyarorszag":
    van_e =True

if van_e ==True:
  print("A csapatok között van Magyarország")
else:
  print("A csapatok között nincs Magyarország")






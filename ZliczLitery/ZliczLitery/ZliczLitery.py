
alfabet = "aąbcćdeęfghijklłmnńoóprsśtuwyzźż"
wartosci = []
for i in range(0,len(alfabet)):
    wartosci.append(0)
file = open("slownik.txt","r",encoding="utf-8")
if file: print("Udało się znaleźć odpowiedni plik!")
else: exit()
print("Zaczekaj chwilę!")
for line in file:
    for i in range(0,len(line)):
        for j in range(0,len(alfabet)):
            if line[i] == alfabet[j] : wartosci[j]+=1
for i in range(0,len(wartosci)):
    print(alfabet[i]," : ",wartosci[i]) 
file.close()
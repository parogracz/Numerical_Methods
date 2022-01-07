a=int(input("Podaj pierwszą liczbę:"))
b=int(input("Podaj drugą liczbę:"))

# print(a,":",b,"=",a/b) #standardowy output
# print(a,":",b,"=",round(a/b,2)) #użycie funkcji round()
# print(a,":",b,"=",round(a/b,20)) #nieefektywne (dlaczego?)

# print(f"{a} : {b} = {a/b}") #fstring
# print(f"{a} : {b} = {a/b:.3}")
# print(f"{a} : {b} = {a/b:.20}")

# string = str(a)+" : "+str(b)+" = "+str(a/b) #zdef. string
# print(string)

# print("{} : {} = {}".format(a,b,a/b)) #użycie funkcji format
# print("{} : {} = {:.4}".format(a,b,a/b))
# print("{} : {} = {:.20}".format(a,b,a/b))
# print("Vector [{},{},{:.3}]".format(a,b,a/b))

# print("%d : %d = %f" % (a,b,a/b)) #stary styl formatowania
# print("%d : %d = %.4f" % (a,b,a/b))
# print("%d : %d = %.20f" % (a,b,a/b))

# for i in range(1,11):
#     print(" {} {} {} ".format(i,i*i,i*i*i)) #bez justowania
# for i in range(1,11): #manualne justowanie
#     print(" {:2d} {:3d} {:4d} ".format(i,i*i,i*i*i))
# for i in range(1,11): #automatyczne justowanie
#     print(str(i).rjust(2),\
#     str(i*i).rjust(3), str(i*i*i).rjust(4))

# print(str(a).zfill(5),":",str(b).zfill(5),"="\
# ,str(a/b).zfill(20)) #uzupełnianie

# print ("home\natan") #\n oznacza przejście do nowej linii
# print(r"home\natan") #wyłączamy specjalne znaczenie stringa \n
# print ("1\t2\t") #\t oznacza tabulator
# print(r"1\t2\t") #wyłączamy specjalne znaczenie stringa \t


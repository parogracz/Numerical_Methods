# class Kalkulator(object):
#     def __init__(self,*a):
#         if len(a) == 2:
#             self.a = a[0]
#             self.b = a[1]
#         if len(a) == 3:
#             self.a = a[0]
#             self.b = a[1]
#             self.c = a[2]
#     def __str__(self):
#         if "self.c" in locals():
#             return "Obiekt dodający i odejmujący liczby: %d oraz %d oraz %d"%(self.a, self.b, self.c)
#         else:
#             return "Obiekt dodający i odejmujący liczby: %d oraz %d"%(self.a, self.b)
#     def dodawanie(self):
#         return self.a+self.b+self.c
#     def odejmowanie(self):
#         if self.a < self.b:
#             return self.b - self.a
#         else: 
#             return self.a - self.b
#     def show(self):
#         print(self.a)
#         print(self.b)
#         print(self.c)
    

# obj = Kalkulator(6,5)
# print(obj.dodawanie())
# print(obj.odejmowanie())
# obj.show()
# print(obj)

# class Człowiek(object):
#     def __init__(self, imie, nazwisko):
#         self.imie, self.nazwisko = imie, nazwisko
#     def info(self):
#         print(f"To {self.imie} {self.nazwisko}.")

# class Studenciak(Człowiek):
#     def __init__(self, imie, nazwisko, nr_alb, kierunek):
#         super().__init__(imie, nazwisko)
#         self.nr_alb, self.kierunek = nr_alb, kierunek
#     def info(self):
#         super().info()
#         print(f"Numer albumu: {self.nr_alb} \nKierunek: {self.kierunek}")

# s1 = Studenciak("Adam","Nowak",123,"Informatyka")
# s1.info()

# class DoubleTab(object):
#     def __init__(self,a,b):
#         self.a , self.b = a, b
#     def __iter__(self):
#         for i in self.b:
#             yield i

# a=[1,3,5,7,9]
# b=[2,4,6,8,0]
# tab = DoubleTab(a,b)

# for i in tab:
#     print(i)

# class Tajne(object):
#     def __init__(self, a) -> None:
#         super().__init__()
#         self.__a= a
#     def __metoda(self):
#         print(self.__a)

# obj = Tajne(5)

# obj._Tajne__metoda()
# print(obj._Tajne__a)

# class Tablica(object):
#     def __init__(self,n):
#         self.a=['lalalawel' for i in range (n)]
#     def __str__(self):
#         return str(self.a)
#     def oblicz(self,f): #definicja delegata
#         return f(self.a)

# t = Tablica(10)
# print(t)
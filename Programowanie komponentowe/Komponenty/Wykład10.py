from pakiet import matematyka

class Człowiek(object):
    def __init__(self, imie, nazwisko, pesel, wiek):
        self.imie, self.nazwisko, self.__pesel, self.wiek = imie, nazwisko, pesel, wiek
    def przedstawSię(self):
        print("Cześć, jestem ",self.imie, self.nazwisko,"!")
    def podajWiek(self):
        print("Mam aktualnie ",self.wiek)

class Student(Człowiek):
    def __init__(self, imie, nazwisko, pesel, wiek, numerAlbumu, uczelnia, kierunek):
        super().__init__(imie, nazwisko, pesel, wiek)
        self.__numerAlbumu, self.uczelnia, self.kierunek = numerAlbumu, uczelnia, kierunek
    def jakaUczelnia(self):
        print("Studiuję na ", self.uczelnia)

class Robol(Człowiek):
    def __init__(self, imie, nazwisko, pesel, wiek, zakładPracy):
        super().__init__(imie, nazwisko, pesel, wiek)
        self.zakładPracy = zakładPracy
    def praca(self):
        print("Pracuję w ", self.zakładPracy)

s1 = Student("Bartosz", "Konarski", 123456789, 22, "s129823", "SGGW", "Informatyka")
s2 = Student("Daniel", "Kankowski", 125534209, 23, "s129521", "SGH", "Zarządzanie")

matematyka.OpracjeCzlowieka.ktoStarszy(s1,s2)

matematyka.OperacjeStudenta.numerAlbumu(s1)
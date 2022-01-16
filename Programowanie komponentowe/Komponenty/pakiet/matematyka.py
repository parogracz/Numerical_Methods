class Operacje():
    def dodawanie(x,y):
        return x+y
    def odejmowanie(x,y):
        return x-y
class OpracjeCzlowieka():
    def ktoStarszy(czlowiek1,czlowiek2):
        if czlowiek1.wiek < czlowiek2.wiek:
            print(czlowiek2.imie," jest starszy!")
        elif czlowiek1.wiek > czlowiek2.wiek:
            print(czlowiek1.imie," jest starszy")
        else: 
            print("Są w tym samym wieku")
    def karta(człowiek):
        print(f"Imię: {człowiek.imie}\nNazwisko: {człowiek.nazwisko}\nWiek: {człowiek.wiek}")
class OperacjeStudenta():
    def numerAlbumu(student):
        print(student._Student__numerAlbumu)
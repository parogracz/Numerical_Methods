from interface import interfejsy
from zope.interface import interface, implementer

@implementer(interfejsy.IForemny)
class Kwadrat(object):
    def __init__(self):
        pass
    def pole(self):
        return self.a**2
    def obwod(self):
        return self.a*4
    def daneWczyt(self,a):
        self.a = a

k= Kwadrat()
k.daneWczyt(5)
print(k.obwod())
print(k.pole())
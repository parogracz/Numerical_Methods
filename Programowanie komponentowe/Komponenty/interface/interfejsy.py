from zope.interface import Interface

class IForemny(Interface):
    def daneWczyt(): 
        """Wczytywanie danych"""
    def pole():
        """Liczenie Pola"""
    def obwod():
        """Liczenie Obwodu"""
from tkinter import *

class Program(object):

    def __init__(self) -> None:
        super().__init__()
        self.okno = Tk()
        self.okno.title="Tytuł okna"
        self.okno.geometry("800x600")

        self.frame = Frame(self.okno)
        self.frame.grid()

        self.przycisk1 = Button(self.frame)
        self.przycisk1["text"] = "Click me!"
        self.przycisk1.grid(row=1, column=1) #Teraz się pojawia
        self.przycisk1["command"] = self.eventButton

        self.etykieta1 = Label(self.frame)
        self.etykieta1["text"] = "Label n the hood"
        self.etykieta1.grid(row=1, column=2)

        self.wejscie1 = Entry(self.frame) 
        self.wejscie1.grid(row=1, column=3)

        self.wejscie2 = Text(width=30,height=10)
        self.wejscie2.grid()

        self.okno.mainloop()

    def eventButton(self):
        print("print text to console")
        self.przycisk1["text"] = "Clicked!"
 
Program()

# okno=Tk()
# okno.title("Licznik kliknięć")
# okno.geometry("800x600")

# ramka=Frame(okno)
# ramka.grid()

# przycisk1=Button(ramka) #utworzenie przycisku
# przycisk1["text"]="Click me!" #tekst
# przycisk1.grid() #przycisk staje się widoczny


# okno.mainloop()

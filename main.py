from graphics import *


class Stare:
    def __init__(self, name):
        self.nume = name

    def Punct(self):
        return Point(x, y)


def same(nod1, nod2):
    if nod1.name == nod2.name:
        return 1
    else:
        return 0


def search(lista, nume):
    for i in range(len(lista)):
        if lista[i].nume == nume:
            return i
    else:
        return "eroare"


def selftranzitie(x,y,directie,nume,win):
    if directie=="left":
        x-=45
        c=Circle(Point(x+20,y),2)
        c.setFill('pink')
        c.setOutline('pink')
    if directie=="right":
        x+=45
        c=Circle(Point(x-20,y),2)
        c.setFill('pink')
        c.setOutline('pink')
    if directie=="up":
        y-=45
        c=Circle(Point(x,y+20),2)
        c.setFill('pink')
        c.setOutline('pink')
    if directie=="down":
        y+=45
        c=Circle(Point(x,y-20),2)
        c.setFill('pink')
        c.setOutline('pink')
    cir=Circle(Point(x,y),20)
    cir.setOutline('pink')
    cir.setWidth(2)
    cir.draw(win)
    c.draw(win)
    text=Text(Point(x,y),nume)
    text.setSize(10)
    text.setTextColor('pink')
    text.draw(win)

def tranzitie(x1,y1,x2,y2,nume,win):
    if x1>x2:
        x2+=25
        x1-=25
    else:
        x1+=25
        x2-=25
    if y1>y2:
        y2+=25
        x1-=25
    else:
        y1+=25
        y2-=25
    ln=Line(Point(x1,y1),Point(x2,y2))
    ln.setArrow("last")
    ln.setWidth(2)
    if x1>x2 or y1<y2:
        ln.setFill('aqua')
        pt = ln.getCenter()
        if x1!=x2:
            pt.y-=10
        if y1!=y2:
            pt.x-=10
        tx = Text(pt, nume)
        tx.setTextColor('aqua')
        tx.setSize(10)
    else:
        ln.setFill('red')
        pt = ln.getCenter()
        if x1!=x2:
            pt.y+=10
        if y1!=y2:
            pt.x+=10
        tx = Text(pt, nume)
        tx.setTextColor('red')
        tx.setSize(10)
    ln.draw(win)
    tx.draw(win)

#def stare(x,y,text,final):





class Automat:

    def citire(self):
        with open("automat.in", 'r') as f:
            s = f.readline().split()  #
            self.stari = []
            for i in s:
                self.stari.append(Stare(i))
            t = f.readline().replace("\n", "")  #
            self.sin = self.stari[search(self.stari, t)]
            s = f.readline().split()
            self.sfin = []
            for i in s:
                (self.sfin).append(self.stari[search(self.stari, i)])
            self.tranzitii = {}
            for i in self.stari:
                self.tranzitii[i] = {}
            x = f.readline()
            while x:
                x = x.split()
                self.tranzitii[self.stari[search(self.stari, x[0])]][x[1]] = self.stari[search(self.stari, x[2])]
                x = f.readline()

    def afisare(self):

        print([i.nume for i in self.stari])
        print(self.sin.nume)
        print([i.nume for i in self.sfin])
        print(self.tranzitii)
        print()
        print(self.stari)
        print(self.sin)
        print(self.sfin)
        print(self.tranzitii)

    def verificare(self, cuvant):
        s = self.sin
        ok = 1
        for i in cuvant:
            if i in self.tranzitii[s].keys():
                s = self.tranzitii[s][i]
            else:
                ok = 0
        if (s in self.sfin) and ok == 1:
            return 1
        else:
            return 0

    def afisare_grafica(self):
        win = GraphWin("Automat", 1600, 800)
        win.setBackground('black')
        ok=1
        for i in self.stari:
            if len(self.tranzitii[i].keys())>3:
                ok=1
        if ok==0:
            txt=Text(Point(800,350),"Afisarea automatului nu s-a realizat")
            txt.setTextColor('red')
            txt.setSize(30)
            txt.draw(win)
        else:
            x = 200
            y = 400
            s = aut.sin
            nodviz = {}
            for i in aut.stari:
                nodviz[i] = 0
            #while True:
            tranzitie(x,y,x+100,y+100,"da",win)
            selftranzitie(x-100,y-100,"up","nu",win)






        #####################################
        #####################################
        input_box = Entry(Point(800, 700), 20)
        input_box.draw(win)
        output = Text(Point(800, 750), "da")
        if aut.verificare("")==1:
            output.setTextColor('lime')
        else:
            output.setTextColor('red')
        output.draw(win)
        while True:
            cuv = input_box.getText()
            if aut.verificare(cuv) == 1:
                output.setText("Cuvant acceptat")
                output.setTextColor('lime')
            else:
                output.setText("Cuvant respins")
                output.setTextColor('red')
        win.getMouse()  # Pause to view result
        win.close()  # Close window when done


aut = Automat()
aut.citire()
with open("cuvinte.in") as g:
    cuv = g.readline()
    while cuv:
        cuv = cuv.replace("\n", "")
        print(cuv, end=" - ")
        if aut.verificare(cuv)==1:
            print("Cuvant acceptat")
        else:
            print("Cuvant respins")
        cuv = g.readline()

######################
aut.afisare_grafica()#
######################

from graphics import *
from math import *


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


def selftranzitie(nod,nume,win):
    x=nod.x
    y=nod.y
    if x<250:
        directie="left"
    elif x>550:
        directie="right"
    elif y<=250:
        directie="up"
    else:
        directie="down"
    if directie=="left":
        x-=70
        c=Circle(Point(x+20,y),2)

    if directie=="right":
        x+=70
        c=Circle(Point(x-20,y),2)

    if directie=="up":
        y-=70
        c=Circle(Point(x,y+20),2)

    if directie=="down":
        y+=70
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

def tranzitie(nod1,nod2,nume,win):
    x1=nod1.x
    y1=nod1.y
    x2=nod2.x
    y2=nod2.y
    """
    #Ajustare muchie
    if x1>x2:
        x2+=50
        x1-=50
    else:
        x1+=50
        x2-=50
    if y1>y2:
        y2+=50
        y1-=50
    else:
        y1+=50
        y2-=50
    """
    ln=Line(Point(x1,y1),Point(x2,y2))
    ln.setArrow("last")
    ln.setWidth(3)
    x=(3*x1+x2)//4
    y=(3*y1+y2)//4
    pt = Point(x,y)
    if x1>x2 or y1<y2:
        ln.setFill('aqua')

    else:
        ln.setFill('yellow')
    tx = Text(pt, nume)
    tx.setTextColor('red')
    tx.setSize(20)
    ln.draw(win)
    tx.draw(win)

def stare(nod,final,win):
    x=nod.x
    y=nod.y
    text=nod.nume
    cir=Circle(Point(x,y),50)
    cir.setOutline('white')
    cir.setWidth(2)
    cir.draw(win)
    if final==1:
        cir2=Circle(Point(x,y),40)
        cir2.setOutline('white')
        cir2.setWidth(2)
        cir2.draw(win)
    elif final==-1:
        ln=Line(Point(x,y+100),Point(x,y+50))
        ln.setArrow("last")
        ln.setWidth(3)
        ln.setOutline('green')
        ln.draw(win)
    tx=Text(Point(x,y),text)
    tx.setSize(20)
    tx.setTextColor('red')
    tx.draw(win)


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
        elif ok==0:
            return 0
        else:
            return -1

    def afisare_grafica(self):
        win = GraphWin("Automat", 1600, 800)
        win.setBackground('black')
        ##############################
        #determinare coordonate noduri
        ##############################
        """
        #mod1 - nu prea bun :)))
        i=0
        self.stari[0].x=100
        self.stari[0].y=400

        #stare(self.stari[0],1,win)

        n=len(self.stari)
        l=1200//n
        print(100,400)
        sx=sy=1
        for i in range(1,n):
            x0=self.stari[i-1].x
            y0=self.stari[i-1].y
            x1=x0+sx*l
            y1=y0+sy*l
            if x1<=100:
                if x1<100:
                    x1=200-x1
                sx*=-1
            if y1<=100:
                if y1<100:
                    y1=200-y1
                sx*=-1
            if x1>=700:
                if x1>700:
                    x1= 1400-x1
                sx*=-1
            if y1>=700:
                if y1>700:
                    y1= 1400-y1
                sy*=-1
            print(x1,y1)
            self.stari[i].x=x1
            self.stari[i].y=y1
        """

        #mod2 - sa speram ca merge mai bine
        n=len(self.stari)
        alpha=2*pi/n
        #print(alpha)
        r=300  #raza
        for i in range(n):
            x=r*sin(i*alpha)
            y=r*cos(i*alpha)
            self.stari[i].x=x+400
            self.stari[i].y=y+400
            #print(x,y)
        print(stare(self.sin,-1,win))
        for i in self.stari:
            if i in self.sfin:
                stare(i,1,win)
            elif i==self.sin:
                print("da")
                stare(i,-1,win)
            else:
                stare(i,0,win)
            for j in self.tranzitii[i].keys():
                if i==self.tranzitii[i][j]:
                    selftranzitie(i,j,win)
                else:
                    tranzitie(i,self.tranzitii[i][j],j,win)

        #####################################
        #####################################


        input_box = Entry(Point(1200, 400), 30)
        input_box.draw(win)
        output = Text(Point(1200, 350), "da")
        output.setSize(25)
        ln=Line(Point(800,0),Point(800,800))
        ln.setWidth(3)
        ln.setFill('white')
        ln.setOutline('white')
        ln.draw(win)
        cir=Circle(Point(400,400),300)
        """
        cir2=Circle(Point(700,400),50)
        cir2.setWidth(2)
        cir2.setOutline('white')
        cir2.draw(win)
        cir2 = Circle(Point(770, 400), 20)
        cir2.setWidth(2)
        cir2.setOutline('white')
        cir2.draw(win)
        cir.setOutline('white')
        cir.setWidth(2)
        cir.draw(win)
        """
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
            elif aut.verificare(cuv) == 0:
                output.setText("Cuvant respins (nu exista un drum posibil)")
                output.setTextColor('red')
            else:
                output.setText("Cuvant respins (nodul in care s-a oprit nu e stare finala)")
                output.setTextColor('red')
        win.getMouse()  # Pause to view result
        win.close()  # Close window when done

        #####################################
        #####################################


####MAIN####
aut = Automat()
aut.citire()
with open("cuvinte.in") as g:
    cuv = g.readline()
    while cuv:
        cuv = cuv.replace("\n", "")
        print(cuv, end=" - ")
        if aut.verificare(cuv)==1:
            print("Cuvant acceptat")
        elif aut.verificare(cuv) == 0:
            print("Cuvant respins (nu exista un drum posibil)")
        else:
            print("Cuvant respins (nodul in care s-a oprit nu e stare finala)")

        cuv = g.readline()

######################
aut.afisare_grafica()#
######################

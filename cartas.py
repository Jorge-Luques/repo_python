class Carta:
    listaDePalos = ["Oros", "Bastos", "Copas","Espadas"]
    listaDeValores = ["nada", "As", "2", "3", "4", "5", "6", "7","Sota", "Caballo", "Rey"]
    listaOrdenmport = []
    def __init__(self, palo=0, valor=0, peso=0):
        self.palo = palo
        self.valor = valor
        self.peso = peso
    def __str__(self):
        return (self.listaDeValores[self.valor] + " de " + self.listaDePalos[self.palo])
    
    def asignarPeso(self):
        if self.valor == 1 and self.palo == 3:
            self.peso = 20
        elif self.valor == 1 and self.palo == 1:
            self.peso = 19
        elif self.valor == 7 and self.palo == 3:
            self.peso = 18
        elif self.valor == 7 and self.palo == 0:
            self.peso = 17
        elif self.valor == 3:
            self.peso = 15
        elif self.valor == 2:
            self.peso = 14
        elif self.valor == 1 and (self.palo == 0 or self.palo == 2):
            self.peso = 12
        elif self.valor == 10:
            self.peso = 10
        elif self.valor == 9:
            self.peso = 9
        elif self.valor == 8:
            self.peso = 8
        elif self.valor == 7 and (self.palo == 1 or self.palo == 2):
            self.peso = 7
        elif self.valor == 6:
            self.peso = 6
        elif self.valor == 5:
            self.peso = 5
        else:
            self.peso = 4
        
    def comparar(self,carta):
        if self.peso > carta.peso:
            return 1
        elif self.peso == carta.peso:
            return 0
        else:
            return -1
    
    
class Mazo:
    def __init__(self):
        self.cartas = []
        self.jugadores = []
        carta = Carta()
        for palo in range(4):
            for valor in range(1, 11):
                carta = Carta(palo, valor)
                carta.asignarPeso()
                #print("cp ",carta.peso)
                self.cartas.append(carta)
    
    def addJugador(self,jug):
        self.jugadores.append(jug)
    
    def muestraMazo(self):
        for carta in self.cartas:
            print (carta)
            
    def mezclar(self):
        import random
        nCartas = len(self.cartas)
        for i in range(nCartas):
            j = random.randrange(i, nCartas)
            self.cartas[i], self.cartas[j] = self.cartas[j], self.cartas[i]
    
    def eliminaCarta(self, carta):
        if carta in self.cartas:
            self.cartas.remove(carta)
            return 1
        else:
            return 0
    
    def darCarta(self):
        return self.cartas.pop()
    
    def estaVacio(self):
        return (len(self.cartas) == 0)
    
        
    def repartir(self, jug1, jug2):
        for carta in range(6):
            if carta % 2:
                jug1.append(self.darCarta())
            else:
                jug2.append(self.darCarta())
    
    def reparte(self, nCartas=999):
        nManos = len(self.jugadores)
        mano = Carta()
        for i in range(nCartas):
            if self.estaVacio(): break # fin si se acaban las cartas
            carta = self.darCarta() # da la carta superior
            mano = self.jugadores[i % nManos] # a quien le toca?
            mano.agregaCarta(carta) # agrega la carta a la mano


class Jugador(Mazo):
    def __init__(self, nombre=""):
        self.cartas = []
        self.nombre = nombre
        
    def agregaCarta(self,carta) :
        self.cartas.append(carta)
        
    def verReparto(self):
        carta = Carta()
        print("El jugador",self.nombre,"tiene las cartas:")
        for carta in self.cartas:
            print(carta)
    
    def manoGanadora(self, jug2, pos):
        cartaJ1 = self.cartas[pos]
        cartaJ2 = jug2.cartas[pos]
        if cartaJ1.comparar(cartaJ2) == 1:
            return 1
        elif cartaJ1.comparar(cartaJ2) == 0:
            return 0
        else:
            return -1

class JuegoDeCartas:
    def __init__(self, mazo):
        self.mazo = mazo
        self.mazo.mezclar()
        self.cantCartasJug = 3
    
    def repartirCartas(self,mazo):
        cantJug = len(mazo.jugadores)
        mazo.reparte(self.cantCartasJug * cantJug)
        
    
                
class Truco(JuegoDeCartas):
    def __init__(self, mazo):
        super().__init__(mazo)  # Usar super() para llamar al constructor de la clase base
        self.jugadores = self.mazo.jugadores  # Acceder a los jugadores a través de la instancia
            
    
    def ganaTruco(self):
        cantManosWinJ1 = 0
        jugador1 = self.jugadores[0]
        jugador2 = self.jugadores[1]
        for mano in range(self.cantCartasJug):
            cantManosWinJ1 += jugador1.manoGanadora(jugador2, mano)
        if cantManosWinJ1 > 0:
            print("El truco lo gana",jugador1.nombre)
        elif cantManosWinJ1 < 0:
            print("El truco lo gana",jugador2.nombre)
        else:
            if jugador1.manoGanadora(jugador2, 0) == 1:  #quien gano la primera
                print("El truco lo gana",jugador1.nombre)
            elif jugador1.manoGanadora(jugador2, 0) == -1:
                print("El truco lo gana",jugador1.nombre)
            else:
                print("Gana el que es mano")
                
    def calcularTanto(self, jugador):
        def contarPorPalos(self):
            palos = [0, 0, 0, 0]
            for carta in jugador.cartas:
                palos[carta.palo] += 1
            return palos

        def anularValorFiguras(self, carta):
            if carta.valor in range(8, 11):
                return 0
            else:
                return carta.valor

        def mayorValorCarta(self):
            mayor = 0
            for carta in jugador.cartas:
              valorTemp = anularValorFiguras(self, carta)
              if valorTemp > mayor:
                mayor = valorTemp
            return mayor

        def paloMayor(self):
            palos = contarPorPalos(self)
            return palos.index(max(palos))

        pje = 0
        numCartas = 0
        palo_predominante = paloMayor(self)
        for carta in jugador.cartas:
            if carta.palo == palo_predominante:
                valorTemp = anularValorFiguras(self, carta)
                pje += valorTemp
                numCartas += 1
        if numCartas == 2:
            pje += 20
        elif numCartas == 3:
            print("TIENE FLOR")
        else:
            pje = mayorValorCarta(self)
        return pje

class Puntos(Truco):
    
    def __init__(self,mazo,puntos=0):
        #mazo = super.__init__(mazo)
        #self.jugadores = self.mazo.jugadores 
        self.puntos = puntos
        #self.ordenPorCanto = {"flor":0, "envido":1, "real envido":2, "truco":4, "retruco":5, "quiero vale 4":6}
    
    def valorPuntajeJuego(self,canto):
        canta = canto.lower()
        if canta == "envido":
            return 2
        elif canta == "real envido":
            return 3
        elif canta == "falta envido":
            return calcularLaFalta(self)
        elif canta == "truco":
            return 2
        elif canta == "retruco":
            return 3
        elif canta == "quiero vale 4":
            return 4
        elif canta == "flor":
            return 3
        else:
            print("CANTATE OTRA QUE ESA NO VA")
            return 0
            
    def calcularLaFalta(self):
        pass
    
    def pjePorManoTanto(self):
        pass
    
    def cantaPoder():
        pass
        
                
mazo = Mazo()
jug1 = Jugador("jorge")
jug2 = Jugador("george")
mazo.addJugador(jug1)
mazo.addJugador(jug2)
juegoTruco = JuegoDeCartas(mazo)
juegoTruco.repartirCartas(mazo)

jug1.verReparto()
jug2.verReparto()
truco = Truco(mazo)
print("el tanto de ",jug1.nombre,"es:",truco.calcularTanto(jug1))
print("el tanto de ",jug2.nombre,"es:",truco.calcularTanto(jug2))
truco.ganaTruco()
ptos = Puntos(0)
print(ptos.valorPuntajeJuego("Quiero vale 4"))


#mazo.muestraMazo()
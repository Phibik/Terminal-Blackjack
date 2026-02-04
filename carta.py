class Carta:
    def __init__(self, v, p, t = "MOSTRADA"):
        self.simbolo = v
        self.tipo = t
        match v:
            case "A":
                self.valor = 11
            case "J":
                self.valor = 10
            case "Q":
                self.valor = 10
            case "K":
                self.valor = 10
            case _:
                self.valor = int(v)
        match p:
            case "C":
                self.palo = "♥"
            case "D":
                self.palo = "♦"
            case "T":
                self.palo = "♣"
            case "P":
                self.palo = "♠"
            case _:
                self.palo = p

    def mostrar(self):
        return self.palo + self.valor

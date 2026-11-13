from pannello.py import PannelloFotovoltaico

class ImpiantoSolare:
    def __init__(self, codice: str, modello: str, localita: str, potenza_massima_kw: float, stato: str) -> None:
        if potenza_massima_kw <= 0: raise ValueError("Potenza non può essere zero o minore")
        self.codice = codice
        self.modello = modello
        self.località = località
        self.potenza_massima_kw = potenza_massima_kw
        self.stato = stato
        self.pannelli : list[PannelloFotovoltaico] = []
    
    def aggiungi_pannello(pannello: PannelloFotovoltaico) -> None:
        for p in self.pannelli:
            if p.codice == pannello.codice:
                raise ValueError("codice gia esistente")
        if pannello.potenza_kw > self.potenza_massima_kw:
            raise ValueError("potenza troppo alta")
        self.pannelli.append(pannello)
    
    def potenza_pannelli -> float:
        somma = 0.0
        for p in self.pannelli:
            somma = somma + p.potenza_kw
        return somma
    
    def cerca_pannello(codice: str) -> PannelloFotovoltaico:
        for p in self.pannelli:
            if p.codice == codice:
                return p
        return None
    
    def rimuovi_pannello(codice: str) -> PannelloFotovolatico:
        for p in self.pannelli:
            if p.codice == codice:
                self.pannelli.remove(p)
                return p
        return None
    
    def pannelli_sotto_potenza(potenza_massima: float) -> list[PannelloFotovoltaico]:
        lista: list[PannelloFotovoltaico] = []
        for p in self.pannelli:
            if p.potenza_kw <= potenza_massima:
                lista.append(p)
        return lista
        
        
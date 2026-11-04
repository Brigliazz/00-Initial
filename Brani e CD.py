
from typing import List, Optional


class Brano:
    def __init__(self, titolo: str, autore: str, durata: int) -> None:
        self.titolo = titolo
        self.autore = autore
        self.durata = durata

    @property
    def titolo(self) -> str:
        return self._titolo

    @titolo.setter
    def titolo(self, valore: str) -> None:
        if not valore:
            raise ValueError("Il titolo non può essere vuoto")
        self._titolo = valore

    @property
    def autore(self) -> str:
        return self._autore

    @autore.setter
    def autore(self, valore: str) -> None:
        if not valore:
            raise ValueError("L'autore non può essere vuoto")
        self._autore = valore

    @property
    def durata(self) -> int:
        return self._durata

    @durata.setter
    def durata(self, valore: int) -> None:
        if valore <= 0:
            raise ValueError("La durata deve essere positiva")
        self._durata = valore

    def short_song(self) -> bool:
        return self.durata <= 180

    def __str__(self) -> str:
        return f"{self.titolo} - {self.autore} ({self.durata} secondi)"


class Playlist:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.brani = [] # inizializzare una lista vuota

    def aggiungi_brano(self, brano: Brano) -> None:
        self.brani.append(brano)

    def durata_totale(self) -> int:
        return sum(brano.durata for brano in self.brani)

    def __str__(self) -> str:
        return f"Playlist: {self.nome} ({len(self.brani)} brani)"


class CD:
    def __init__(self, titolo: str, autore: str, brani: Optional[List[Brano]] = None) -> None:
        self.titolo = titolo
        self.autore = autore
        self.brani = brani if brani is not None else []

    def aggiungi_brano(self, brano: Brano) -> None: # la funzione non ritorna nulla
        self.brani.append(brano)

    @property
    def durata_totale(self) -> int:
        totalDuration = 0
        for brano in self.brani:
            totalDuration += brano.durata
        return totalDuration
        # return sum(brano.durata for brano in self.brani)

    def filtra_brani_per_autore(self, autore: str) -> List[Brano]:
        newList = []
        for brano in self.brani:
            if autore == brano.autore:
                newList.append(brano)
        return newList
        # return [brano for brano in self.brani if autore == brano.autore]

    def copia_brani(self) -> List[str]:
        # newBrani = []
        # for brano in self.brani:
        #     newBrani.append(brano)
        # return newBrani
        # [] -> creano la lista
        # il ciclo rimane uguale
        # l'operazione o ciò che voglio allegare alla lista lo defin
        return [str(brano) for brano in self.brani] # cast a stringa nel caso in cui il titolo di una canzone sia un numero es "47"
    
    def __str__(self) -> str: # ToString
        descrizione = [str(brano) for brano in self.brani] # list comprehension    
        return f"CD: {self.titolo} di {self.autore}\n- " + "\n- ".join(descrizione)

if __name__ == "__main__":
    brano1 = Brano("Bohemian Rhapsody", "Queen", 355)
    brano2 = Brano("Imagine", "John Lennon", 183)
    brano3 = Brano("Stairway to Heaven", "Led Zeppelin", 482)

    print(brano1)
    print(f"E' un brano breve? {brano2.short_song()}")

    cd = CD("Classic Hits", "Vari artisti", [brano1, brano2, brano3])
    print(cd)
    print(f"Durata totale: {cd.durata_totale} secondi")

    playlist = Playlist("Miei favoriti")
    playlist.aggiungi_brano(brano1)
    playlist.aggiungi_brano(brano2)
    print(playlist)
    print(f"Durata playlist: {playlist.durata_totale()} secondi")
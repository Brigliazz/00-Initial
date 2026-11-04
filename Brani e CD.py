"""Questa riportata è una possibile implementazione.
Non per forza è necessario utilizzare il decorator @property con setter o meno.
E' possibile semplicemente dichiararli come properità classiche senza decorator come riportato anche negli altri
esercizi risolti nelle altre cartelle.
"""
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



from typing import List, Tuple

class Jogada:
    
    __slots__ = ('_caminho', '_ganho', '_destino')

    def __init__(self, caminho: List[Tuple[int, int]], ganho: int):
        self._caminho = caminho
        self._ganho = ganho
        self._destino = caminho[-1]

    @property
    def caminho(self) -> List[Tuple[int, int]]:
        return self._caminho

    @property
    def ganho(self) -> int:
        return self._ganho

    @property
    def destino(self) -> Tuple[int, int]:
        return self._destino

from typing import List, Tuple

class Jogada:
    # Tirei ganho
    __slots__ = ('_caminho', '_destino')

    def __init__(self, caminho: List[Tuple[int, int]]):
        self._caminho = caminho
        self._destino = caminho[-1]

    @property
    def caminho(self) -> List[Tuple[int, int]]:
        return self._caminho

    @property
    def destino(self) -> Tuple[int, int]:
        return self._destino

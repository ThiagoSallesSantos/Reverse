from typing import List, Tuple

## Classe Jogada, responsável por gerenciar uma jogada das varias jogadas
class Jogada:

    __slots__ = ('_caminho', '_destino')

    def __init__(self, caminho: List[Tuple[int, int]]): ## Contrutor da classe
        self._caminho = caminho ## Caminho a ser percorrido
        self._destino = caminho[-1] ## Destino do caminho a ser percorrido

    @property
    def caminho(self) -> List[Tuple[int, int]]: ## Pega o caminho da jogada
        return self._caminho

    @property
    def destino(self) -> Tuple[int, int]: ## Pega o destino da jogada
        return self._destino

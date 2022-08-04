from jogada import Jogada
from typing import List, Tuple, Union

class Pecas:
    
    __slots__ = ('_cor', '_posicao_pecas', '_jogadas_disponiveis')

    def __init__(self, cor: str, posicoes_iniciais: List[Tuple[int, int]]) -> None:
        self._cor = cor
        self._posicao_pecas = [] + posicoes_iniciais
        self._jogadas_disponiveis = []

    def set_jogada_disponivel(self, jogada: Jogada) -> None:
        if jogada:
            if jogada.destino in [j.destino for j in self._jogadas_disponiveis]:
                for j in self._jogadas_disponiveis:
                    if jogada.destino == j.destino:
                        j.caminho.extend(jogada.caminho)
                        break
            else:   
                self._jogadas_disponiveis.append(jogada)

    def adiciona_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None:
        
        self._posicao_pecas += lista_posicoes
        self._posicao_pecas = list(dict.fromkeys(self._posicao_pecas))

        print(self.cor, "-add: ",self.lista_posicoes, end="\n")

    def remove_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None:
        for posicao in lista_posicoes:
            if posicao in self._posicao_pecas:
                self._posicao_pecas.remove(posicao)
        print(self.cor, "-remove: ",self.lista_posicoes, end="\n")
        

    def consulta_jogada(self, posicao: Tuple[int, int]) -> Union[bool, Jogada]:
        for jogada in self._jogadas_disponiveis:
            if jogada.destino == posicao:
                return jogada
        return False

    @property
    def reseta_jogadas(self) -> None:
        self._jogadas_disponiveis = []

    @property
    def lista_jogadas(self) -> List[Jogada]:
        return self._jogadas_disponiveis

    @property
    def lista_posicoes(self) -> List[Tuple[int, int]]:
        return self._posicao_pecas
    
    @property
    def cor(self) -> str:
        return self._cor

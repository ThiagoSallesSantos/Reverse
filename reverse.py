from agent import Agent
from pecas import Pecas
from tabuleiro import Tabuleiro
from jogada import Jogada
from typing import Tuple, List, Union

class Reverse:

    __slots__ = ('_agent', '_tabuleiro')

    def __init__(self) -> None:
        self._agent = Agent()
        self._tabuleiro = Tabuleiro()
    
    def start(self) -> List[Tuple[str, List[Tuple[int, int]]]]:
        self._tabuleiro.atualiza_pecas()
        return self._tabuleiro.lista_pecas_posicoes

    def get_jogadas_disp(self, pecas:str) -> List[Jogada]:
        return self._tabuleiro.analisa_jogada(self._tabuleiro.busca_pecas(pecas)).lista_jogadas

    def valida_jogada(self, pecas:str, posicao:Tuple[int, int]) -> Union[bool, Jogada]:
        jogada = self._tabuleiro.busca_pecas(pecas).consulta_jogada(posicao)
        if jogada:
            return jogada
        return False

    def realiza_jogada(self, pecas:str, jogada:Jogada) -> List[Tuple[int, int]]:
        peca = self._tabuleiro.busca_pecas(pecas)
        self._tabuleiro.faz_jogada(peca, jogada)
        destinos = [x.destino for x in filter(lambda x: x!=jogada, peca.lista_jogadas)]
        peca.reseta_jogadas
        return destinos
    
    def agente(self, pecas:str) -> Jogada:
        peca = self._tabuleiro.busca_pecas(pecas)
        jogada = self._agent.melhorJogada(self._tabuleiro, peca)
        self._tabuleiro.faz_jogada(peca, jogada)
        peca.reseta_jogadas
        return jogada

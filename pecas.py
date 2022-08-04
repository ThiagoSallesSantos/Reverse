from jogada import Jogada
from typing import List, Tuple, Union

## Classe Peças, responsável por gerenciar um conjunto de peças, seja ela branca ou preta
class Pecas:
    
    __slots__ = ('_cor', '_posicao_pecas', '_jogadas_disponiveis') ## Variaveis da classe

    def __init__(self, cor: str, posicoes_iniciais: List[Tuple[int, int]]) -> None: ## Construtor da classe
        self._cor = cor ## Cor das peças
        self._posicao_pecas = [] + posicoes_iniciais ## Adiciona as peças inicias, na lista de posições, que armazena o local onde estão as peças do jogador x ou y
        self._jogadas_disponiveis = [] ## Armazenar as jogadas disponiveis na rodada

    def set_jogada_disponivel(self, jogada: Jogada) -> None: ## Adiciona na variaveis de jogads disponiveis, as jogadas disponiveis para aquela peças na rodada
        if jogada:
            if jogada.destino in [j.destino for j in self._jogadas_disponiveis]: ## Verifica se tem jogadas com o mesmo destino, caso possivo realizar uma união entre as jogadas
                for j in self._jogadas_disponiveis:
                    if jogada.destino == j.destino:
                        j.caminho.extend(jogada.caminho)
                        break
            else:   
                self._jogadas_disponiveis.append(jogada)

    def adiciona_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None: ## Adiciona as novas posições das novas peças na lista de posições
        self._posicao_pecas += lista_posicoes
        self._posicao_pecas = list(dict.fromkeys(self._posicao_pecas))

    def remove_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None: ## Remove peças que foram tomadas, da lista de posções das peças
        for posicao in lista_posicoes:
            if posicao in self._posicao_pecas:
                self._posicao_pecas.remove(posicao)
        
    def consulta_jogada(self, posicao: Tuple[int, int]) -> Union[bool, Jogada]: ## Verifica se a jogada realizada na rodada é válida
        for jogada in self._jogadas_disponiveis:
            if jogada.destino == posicao:
                return jogada
        return False

    @property
    def reseta_jogadas(self) -> None: ## Limpa a lista de jogadas da rodada
        self._jogadas_disponiveis = []

    @property
    def lista_jogadas(self) -> List[Jogada]: ## Pega as jogadas disponiveis na rodada
        return self._jogadas_disponiveis

    @property
    def lista_posicoes(self) -> List[Tuple[int, int]]: ## Pega a lista de posições das peças
        return self._posicao_pecas
    
    @property
    def cor(self) -> str: ## Pega qual é a cor da peça
        return self._cor

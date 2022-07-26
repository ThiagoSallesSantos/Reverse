from jogada import Jogada
from tabulate import tabulate
from pecas import Pecas
from typing import Tuple, Union, List

class Tabuleiro:
    
    __slots__ = ('_tamanho', '_posicao_default', '_tabuleiro', '_lista_pecas')

    def __init__(self) -> None:
        self._tamanho = (8,8)
        self._posicao_default = 'o'
        self._tabuleiro = [[self._posicao_default for i in range(self._tamanho[1])] for i in range(self._tamanho[0])]
        self._lista_pecas = self.cria_pecas()

    def cria_pecas(self) -> Tuple[Pecas, Pecas]:   
        pecas_brancas = Pecas('B', [(int(self._tamanho[0]/2 - 1), int(self._tamanho[1]/2 - 1)), (int(self._tamanho[0]/2), int(self._tamanho[1]/2))])
        pecas_pretas = Pecas('P', [(int(self._tamanho[0]/2), int(self._tamanho[1]/2 - 1)), (int(self._tamanho[0]/2 - 1), int(self._tamanho[1]/2))])
        return pecas_brancas, pecas_pretas
    
    def busca_pecas(self, cor:str) -> Pecas:
        return list(filter(lambda x: x.cor == cor, self._lista_pecas))[0]

    @property
    def lista_pecas_posicoes(self) -> List[Tuple[str, List[Tuple[int, int]]]]:
        return [(x.cor, x.lista_posicoes) for x in self._lista_pecas]

    def faz_jogada(self, pecas:Pecas, jogada:Jogada):
        if pecas.cor == "B":
            pecas_adv = self.busca_pecas("P")
        else:
            pecas_adv = self.busca_pecas("B")
        pecas.adiciona_posicao(jogada.caminho)
        pecas_adv.remove_posicao(jogada.caminho)
        self.atualiza_pecas()

    def analisa_jogada(self, pecas: Pecas) -> Pecas:
        for peca in pecas.lista_posicoes:
            pecas.set_jogada_disponivel(self._analisa_baixo(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_esquerda(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_direita(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_esq_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_dir_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_esq_baixo(peca, pecas.cor))
            pecas.set_jogada_disponivel(self._analisa_dir_baixo(peca, pecas.cor))
        return pecas

    def _analisa_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0], peca[1]-1]
        caminho = [tuple(aux)]
        while aux[1]-1 >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] -= 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0], peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0], peca[1]+1]
        caminho = [tuple(aux)]
        while aux[1]+1 < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] += 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0], peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_esquerda(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]]
        caminho = [tuple(aux)]
        while aux[0]-1 >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_direita(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]]
        caminho = [tuple(aux)]
        while aux[0]+1 < self._tamanho[0] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_esq_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]-1]
        caminho = [tuple(aux)]
        while aux[0]-1 >= 0 and aux[1]-1 >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] -= 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_dir_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]-1]
        caminho = [tuple(aux)]
        while aux[0]+1 < self._tamanho[0] and aux[1]-1 >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] -= 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_esq_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]+1]
        caminho = [tuple(aux)]
        while aux[0]-1 >= 0 and aux[1]+1 < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] += 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def _analisa_dir_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]+1]
        caminho = [tuple(aux)]
        while aux[0]+1 < self._tamanho[0] and aux[1]+1 < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] += 1
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None
    
    def atualiza_pecas(self) -> None:
        for pecas in self._lista_pecas:
            for peca in pecas.lista_posicoes:
                self._tabuleiro[peca[0]][peca[1]] = pecas.cor

    @property
    def imprimi(self) -> None:
        tabela = [linha for linha in self._tabuleiro]
        print(tabulate(tabela))

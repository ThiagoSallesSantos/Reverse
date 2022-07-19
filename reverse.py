from pecas import Pecas
from tabulate import tabulate
from typing import Tuple, Union

class Reverse:

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

    def start(self) -> None:
        self.adiciona_pecas()
        self.imprimi()
        while True:
            for pecas in self._lista_pecas:
                print("Peca " + pecas.cor + " jogando!")
                self.analisa_jogada(pecas)
                texto = "\n".join("Movimento: " + str(x[0]) + " Ganho: " + str(x[1]) for x in pecas.lista_jogadas)
                print(texto)
                posicao, move = self.input_usr(pecas)
                print(posicao)
                print(move)
                self.imprimi()

    def input_usr(self, pecas: Pecas):
        x = None
        y = None
        move = None
        while True:
            x = int(input("x: "))
            y = int(input("y: "))
            vigia, move = pecas.consulta_jogada(tuple((x, y)))
            if vigia:
                break
            print("Posição invalida!")
        return tuple((x, y)), move
        

    def adiciona_pecas(self) -> None:
        for pecas in self._lista_pecas:
            for peca in pecas.lista_posicoes:
                self._tabuleiro[peca[0]][peca[1]] = pecas.cor

    def imprimi(self) -> None:
        tabela = [linha for linha in self._tabuleiro]
        print(tabulate(tabela))
        
    def analisa_jogada(self, pecas: Pecas) -> None:
        for peca in pecas.lista_posicoes:
            pecas.set_jogada_disponivel(self.analisa_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_baixo(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_esquerda(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_direita(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_esq_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_dir_cima(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_esq_baixo(peca, pecas.cor))
            pecas.set_jogada_disponivel(self.analisa_dir_baixo(peca, pecas.cor))

    def analisa_cima(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0], peca[1]-1]
        while aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] -= 1
            ganho += 1
        return ('cima', tuple(aux), ganho) if aux != [peca[0], peca[1]-1] else None

    def analisa_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0], peca[1]+1]
        while aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] += 1
            ganho += 1
        return ('baixo', tuple(aux), ganho) if aux != [peca[0], peca[1]+1] else None

    def analisa_esquerda(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]-1, peca[1]]
        while aux[0] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            ganho += 1
        return ('esquerda', tuple(aux), ganho) if aux != [peca[0]-1, peca[1]] else None

    def analisa_direita(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]+1, peca[1]]
        while aux[0] < self._tamanho[0] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            ganho += 1
        return ('direita', tuple(aux), ganho) if aux != [peca[0]+1, peca[1]] else None

    def analisa_esq_cima(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]-1, peca[1]-1]
        while aux[0] >= 0 and aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] -= 1
            ganho += 1
        return ('esq_cima', tuple(aux), ganho) if aux != [peca[0]-1, peca[1]-1] else None

    def analisa_dir_cima(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]+1, peca[1]-1]
        while aux[0] < self._tamanho[0] and aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] -= 1
            ganho += 1
        return ('dir_cima', tuple(aux), ganho) if aux != [peca[0]+1, peca[1]-1] else None

    def analisa_esq_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]-1, peca[1]+1]
        while aux[0] >= 0 and aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] += 1
            ganho += 1
        return ('esq_baixo', tuple(aux), ganho) if aux != [peca[0]-1, peca[1]+1] else None

    def analisa_dir_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]:
        ganho = 1
        aux = [peca[0]+1, peca[1]+1]
        while aux[0] < self._tamanho[0] and aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] += 1
            ganho += 1
        return ('dir_baixo', tuple(aux), ganho) if aux != [peca[0]+1, peca[1]+1] else None
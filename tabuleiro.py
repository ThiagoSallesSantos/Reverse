from jogada import Jogada
from tabulate import tabulate
from pecas import Pecas
from typing import Tuple, Union

class Tabuleiro:
    
    __slots__ = ('_turn', '_tamanho', '_posicao_default', '_tabuleiro', '_tabuleiro_pesos', '_lista_pecas')

    def __init__(self) -> None:
        self._turn = 'P'
        self._tamanho = (8,8)
        self._posicao_default = 'o'
        self._tabuleiro = [[self._posicao_default for i in range(self._tamanho[1])] for i in range(self._tamanho[0])]
        self._tabuleiro_pesos = [[120, -20, 20, 5, 5, 20, -20, 120],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [120, -20, 20, 5, 5, 20, -20, 120]]
        self._lista_pecas = self.cria_pecas()

    def cria_pecas(self) -> Tuple[Pecas, Pecas]:   
        pecas_brancas = Pecas('B', [(int(self._tamanho[0]/2 - 1), int(self._tamanho[1]/2 - 1)), (int(self._tamanho[0]/2), int(self._tamanho[1]/2))])
        pecas_pretas = Pecas('P', [(int(self._tamanho[0]/2), int(self._tamanho[1]/2 - 1)), (int(self._tamanho[0]/2 - 1), int(self._tamanho[1]/2))])
        return pecas_brancas, pecas_pretas
    
    # retorna as jogadas disponiveis para o jogadoor
    def jogadas_disponiveis(self):
        brancas, pretas = self._lista_pecas
        return brancas._jogadas_disponiveis if self._turn == 'B' else pretas._jogadas_disponiveis

    # altera pecas no tabuleiro e posicao das pecas
    def faz_jogada_valida(self, jogada):
        brancas, pretas = self._lista_pecas
        if jogada:
            if self._turn == 'B':
            
                brancas.adiciona_posicao(jogada.caminho)
                pretas.remove_posicao(jogada.caminho)
            elif self._turn == 'P':
            
                pretas.adiciona_posicao(jogada.caminho)
                brancas.remove_posicao(jogada.caminho)
            
            self._lista_pecas = brancas, pretas
            # print(self._lista_pecas[0]._posicao_pecas, end=' -> Pecas Brancas')
            # print(self._lista_pecas[1]._posicao_pecas, end=' -> Pecas Pretas')
            self.atualiza_pecas(self._lista_pecas)
            self._turn = 'B' if self._turn == 'P' else 'P'


    
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

    def analisa_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0], peca[1]-1]
        
        caminho = [tuple(aux)]
        while aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] -= 1
        
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0], peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0], peca[1]+1]
        
        caminho = [tuple(aux)]
        while aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[1] += 1
            
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0], peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_esquerda(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]]
        
        caminho = [tuple(aux)]
        while aux[0] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1

            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_direita(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]]

        caminho = [tuple(aux)]
        while aux[0] < self._tamanho[0] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_esq_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]-1]
        
        caminho = [tuple(aux)]
        while aux[0] >= 0 and aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] -= 1

            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_dir_cima(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]-1]
        
        caminho = [tuple(aux)]
        while aux[0] < self._tamanho[0] and aux[1] >= 0 and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] -= 1
            
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]-1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_esq_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]-1, peca[1]+1]
        
        caminho = [tuple(aux)]
        while aux[0] >= 0 and aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] -= 1
            aux[1] += 1
            
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]-1, peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None

    def analisa_dir_baixo(self, peca: Tuple[int, int], cor: str) -> Union[Jogada, None]:
        aux = [peca[0]+1, peca[1]+1]
        
        caminho = [tuple(aux)]
        while aux[0] < self._tamanho[0] and aux[1] < self._tamanho[1] and self._tabuleiro[aux[0]][aux[1]] not in [self._posicao_default, cor]:
            aux[0] += 1
            aux[1] += 1
            
            caminho.append(tuple(aux))
        return Jogada(caminho) if aux != [peca[0]+1, peca[1]+1] and self._tabuleiro[aux[0]][aux[1]] == self._posicao_default else None
    
    def atualiza_pecas(self, lista_pecas) -> None:
        for pecas in lista_pecas:
            for peca in pecas.lista_posicoes:
                self._tabuleiro[peca[0]][peca[1]] = pecas.cor

    def imprimi(self) -> None:
        tabela = [linha for linha in self._tabuleiro]
        print(tabulate(tabela))
from pecas import Pecas
from tabulate import tabulate

class Reverse:

    def __init__(self):
        self.tamanho = (8,8)
        self.posicao_default = 'o'
        self.tabuleiro = [[self.posicao_default for i in range(self.tamanho[1])] for i in range(self.tamanho[0])]
        self.lista_pecas = self.cria_pecas()

    def cria_pecas(self):   
        pecas_brancas = Pecas('B', [(int(self.tamanho[0]/2 - 1), int(self.tamanho[1]/2 - 1)), (int(self.tamanho[0]/2), int(self.tamanho[1]/2))])
        pecas_pretas = Pecas('P', [(int(self.tamanho[0]/2), int(self.tamanho[1]/2 - 1)), (int(self.tamanho[0]/2 - 1), int(self.tamanho[1]/2))])
        return pecas_brancas, pecas_pretas

    def start(self):
        while True:
            self.adiciona_pecas()
            self.imprimi()
            self.analisa_jogada()
            break
    
    def adiciona_pecas(self):
        for pecas in self.lista_pecas:
            for peca in pecas.posicao_pecas:
                self.tabuleiro[peca[0]][peca[1]] = pecas.cor

    def imprimi(self):
        tabela = [linha for linha in self.tabuleiro]
        print(tabulate(tabela))
        
    def analisa_jogada(self):
        for pecas in self.lista_pecas:
            for peca in pecas.posicao_pecas:
                pecas.jogadas_disponiveis['cima'] = self.analisa_cima(peca, pecas.cor)
                pecas.jogadas_disponiveis['baixo'] = self.analisa_baixo(peca, pecas.cor)
                pecas.jogadas_disponiveis['esquerda'] = self.analisa_esquerda(peca, pecas.cor)
                pecas.jogadas_disponiveis['direita'] = self.analisa_baixo(peca, pecas.cor)
                print("Jogas diponiveis para a " + str(pecas.cor) + ":" + str(list(filter(lambda x: x, pecas.jogadas_disponiveis.values()))))
                x = int(input())
                y = int(input())
                print("Jogada escolhida é: " + str(list(pecas.jogadas_disponiveis.keys())[list(pecas.jogadas_disponiveis.values()).index([x, y])]))

    def analisa_cima(self, peca, cor):
        aux = [peca[0], peca[1]-1]
        while aux[1] >= 0 and self.tabuleiro[aux[0]][aux[1]] not in [self.posicao_default, cor]:
            aux[1] -= 1
        return aux if aux != [peca[0], peca[1]-1] else None

    def analisa_baixo(self, peca, cor):
        aux = [peca[0], peca[1]+1]
        while aux[1] < self.tamanho[1] and self.tabuleiro[aux[0]][aux[1]] not in [self.posicao_default, cor]:
            aux[1] -= 1
        return aux if aux != [peca[0], peca[1]+1] else None

    def analisa_esquerda(self, peca, cor):
        aux = [peca[0]-1, peca[1]]
        while aux[0] >= 0 and self.tabuleiro[aux[0]][aux[1]] not in [self.posicao_default, cor]:
            aux[1] -= 1
        return aux if aux != [peca[0]-1, peca[1]] else None

    def analisa_direita(self, peca, cor):
        aux = [peca[0]+1, peca[1]]
        while aux[0] < self.tamanho[0] and self.tabuleiro[aux[0]][aux[1]] not in [self.posicao_default, cor]:
            aux[1] -= 1
        return aux if aux != [peca[0]+1, peca[1]] else None

from agent import Agent
from pecas import Pecas
from tabuleiro import Tabuleiro
from jogada import Jogada
from tabulate import tabulate
from typing import Tuple

class Reverse:

    __slots__ = ('_agent', '_tabuleiro', '_tabuleiro_pesos')

    def __init__(self) -> None:
        self._agent = Agent()
        self._tabuleiro = Tabuleiro()
        self._tabuleiro_pesos = [[120, -20, 20, 5, 5, 20, -20, 120],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [120, -20, 20, 5, 5, 20, -20, 120]]
        
    # TODO - mudar logica : colocar analiza jogada sem parametro (usar turn do proprio tabuleiro)
    def start(self) -> None:
        self._tabuleiro.atualiza_pecas(self._tabuleiro._lista_pecas)
        self._tabuleiro.imprimi()
        while True:
            brancas, pretas = self._tabuleiro._lista_pecas
            pecas = brancas if self._tabuleiro._turn == 'B' else pretas
            
            print("Peca " + pecas.cor + " jogando!")
            self._tabuleiro.analisa_jogada(pecas)
            texto = "\n".join("Movimento: " + str(x.destino) for x in pecas.lista_jogadas)
            print(texto)
            # TODO - Mudar logica de jogadas para Jogada,
            #  já que agora que existe apenas uma por destino.
            if self._tabuleiro._turn == 'P':
                jogada = self.input_usr(pecas)
            else:
                print(id(self._tabuleiro), end=" -> ID TAB REVERSE\n")
                jogada = self._agent.melhorJogada(self._tabuleiro)

            self._tabuleiro.faz_jogada_valida(jogada)
            
            if jogada:
            
                print(jogada.caminho)
                print(jogada.destino)
            self._tabuleiro.imprimi()

    def input_usr(self, pecas: Pecas) -> Jogada:
        x = None
        y = None
        jogada = None
        while True:
            x = int(input("x: "))
            y = int(input("y: "))
            jogada = pecas.consulta_jogada(tuple((x, y)))
            if jogada:
                break
            print("Posição invalida!")
        return jogada
        

    
        
    
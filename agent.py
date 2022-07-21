import imp
from typing import List, Tuple
from copy import deepcopy

from sklearn.metrics import SCORERS

class Agent:
    
   

    def __init__(self):
        self._tabuleiro_pesos = [[120, -20, 20, 5, 5, 20, -20, 120],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [120, -20, 20, 5, 5, 20, -20, 120]]

    def _avaliacao(self, tabuleiro):
        # TODO - Heuristica
        # por agora eu tô somando fazendo o score somando as peças do tabuleiro: B +
        # P -. não sei onde deixo os pesos do tabuleiro 
        brancas, pretas = tabuleiro._lista_pecas
        score = 0
        for x, y in brancas.lista_posicoes:
            score += self._tabuleiro_pesos[x][y]
        for x, y in pretas.lista_posicoes:
            score -= self._tabuleiro_pesos[x][y]
        
        return score
    
    def melhorJogada(self, tabuleiro):
        
        idx = 0
        a = -10000
        b = 100000
        
        depth = 3
        jogadas = tabuleiro.jogadas_disponiveis()
        
        for i in range(0, len(jogadas)):
            tempBoard = deepcopy(tabuleiro)
            # print(id(tempBoard), end=" -> ID TAB AGENT\n")
            tempBoard.faz_jogada_valida(jogadas[i])
            minmax = self._min_max(tempBoard, depth, a, b, True)

            if minmax>a:
                a=minmax
                idx = i
                
        return jogadas[idx]


    def _min_max(self, tabuleiro, depth, alpha, beta, max_payer):
        jogadas = tabuleiro.jogadas_disponiveis()
        # folhaaas -> fim da rec
        if depth == 0:
            return self._avaliacao(tabuleiro)
        
        if max_payer:
            max_eval = -10000
            for jogada in jogadas:
                tempBoard = deepcopy(tabuleiro)
                # print(id(tempBoard), end=" -> ID TAB {}\n".format(depth))
                tempBoard.faz_jogada_valida(jogada)
                eval = self._min_max(tempBoard, depth-1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
            
            return max_eval

        else:
            min_eval = 10000
            for jogada in jogadas:
                tempBoard = deepcopy(tabuleiro)
                tempBoard.faz_jogada_valida(jogada)
                eval = self._min_max(tempBoard, depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
            
            return min_eval
import imp
from typing import List, Tuple
from copy import deepcopy

from sklearn.metrics import SCORERS
from jogada import Jogada

from pecas import Pecas
# Classe agent
class Agent:
    # construtor seta atributo do peso das posições no tabuleiro
    def __init__(self):
        self._tabuleiro_pesos = [[120, -20, 20, 5, 5, 20, -20, 120],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [5, -5, 3, 3, 3, 3, -5, 5],
                                [20, -5, 15, 3, 3, 15, -5, 20],
                                [-20, -40, -5, -5, -5, -5, -40, -20],
                                [120, -20, 20, 5, 5, 20, -20, 120]]
    # método avaliação retorna a pontuação do agente em determinado estado do tabuleiro
    def _avaliacao(self, tabuleiro):
        brancas, pretas = tabuleiro.busca_pecas('B'), tabuleiro.busca_pecas('P')
        score = 0
        for x, y in brancas.lista_posicoes:
            score += self._tabuleiro_pesos[x][y]
        for x, y in pretas.lista_posicoes:
            score -= self._tabuleiro_pesos[x][y]
        return score
    
    # método recebe o estado do tabuleiro e as peças do agente, 
    # com isso encontra qual a melhor jogada imediata com maior ganho
    # em com uma profundidade pré definida de 3 jogadas 
    def melhorJogada(self, tabuleiro, peca:Pecas) -> Jogada:
        idx = 0
        a = -10000
        b = 100000
        depth = 3
        tabuleiro.analisa_jogada(peca)
        jogadas = peca.lista_jogadas
        for i in range(0, len(jogadas)):
            tempBoard = deepcopy(tabuleiro)
            peca = tempBoard.busca_pecas(peca.cor)
            tempBoard.faz_jogada(peca, jogadas[i])
            minmax = self._min_max(tempBoard, "P" if peca.cor == "B" else "B", depth, a, b, True)
            if minmax>a:
                a=minmax
                idx = i
        return jogadas[idx]

    # método auxiliar recursivo para definição da melhor jogada imediata (min_max)
    def _min_max(self, tabuleiro, pecas, depth, alpha, beta, max_payer):
        peca = tabuleiro.busca_pecas(pecas)
        jogadas = peca.lista_jogadas
        # Se profundidade = 0 ou o numero de jogadas possiveis acabaram
        # retorna a avaliação estatica do estado do tabuleiro
        if depth == 0 or len(jogadas) == 0:
            return self._avaliacao(tabuleiro)
        # avaliação maxima para jogador maximador
        if max_payer:
            max_eval = -10000
            for jogada in jogadas:
                tempBoard = deepcopy(tabuleiro)
                tempBoard.faz_jogada(peca, jogada)
                eval = self._min_max(tempBoard, "P" if peca.cor == "B" else "B", depth-1, alpha, beta, False)
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                # poda
                if beta <= alpha: 
                    break
            
            return max_eval
        # avaliação minima para jogador minimizador
        else:
            min_eval = 10000
            for jogada in jogadas:
                tempBoard = deepcopy(tabuleiro)
                tempBoard.faz_jogada(peca, jogada)
                eval = self._min_max(tempBoard, "P" if peca.cor == "B" else "B", depth-1, alpha, beta, True)
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                # poda
                if beta <= alpha:
                    break
            
            return min_eval
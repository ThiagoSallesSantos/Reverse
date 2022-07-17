class Pecas:
    
    def __init__(self, cor, posicoes_iniciais):
        self.cor = cor
        self.posicao_pecas = [] + posicoes_iniciais
        self.jogadas_disponiveis = dict({'cima': None, 'baixo': None, 'esquerda': None, 'direita': None, 'esq_cima': None, 'dir_cima': None, 'esq_baixo': None, 'dir_baixo': None})

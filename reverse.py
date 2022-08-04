from agent import Agent
from tabuleiro import Tabuleiro
from jogada import Jogada
from typing import Tuple, List, Union

## Classe responsável, pela gerenciamento do reverse e seus jogadores
class Reverse:

    __slots__ = ('_agent', '_tabuleiro')

    def __init__(self) -> None:
        self._agent = Agent() ## Cria o agente
        self._tabuleiro = Tabuleiro() ## Cria um tabuleiro
    
    ## Inicia o jogo
    def start(self) -> List[Tuple[str, List[Tuple[int, int]]]]:
        self._tabuleiro.atualiza_pecas()
        return self._tabuleiro.lista_pecas_posicoes

    ## Pega as jogadas disponíveis de determinado peças, apartir da cor dela
    def get_jogadas_disp(self, pecas:str) -> List[Jogada]:
        return self._tabuleiro.analisa_jogada(self._tabuleiro.busca_pecas(pecas)).lista_jogadas

    ## Realiza validação da jogada
    def valida_jogada(self, pecas:str, posicao:Tuple[int, int]) -> Union[bool, Jogada]:
        jogada = self._tabuleiro.busca_pecas(pecas).consulta_jogada(posicao)
        if jogada:
            return jogada
        return False

    ## Realiza a jogada, fazendo que o movimento seja concretizado, e as peças atualizadas
    def realiza_jogada(self, pecas:str, jogada:Jogada) -> List[Tuple[int, int]]:
        peca = self._tabuleiro.busca_pecas(pecas)
        self._tabuleiro.faz_jogada(peca, jogada)
        destinos = [x.destino for x in filter(lambda x: x!=jogada, peca.lista_jogadas)]
        peca.reseta_jogadas ## Reseta as jogadas
        return destinos
    
    ## Realiza a jogada do agente, baseado na procura de melhor jogada realizada pelo agente
    def agente(self, pecas:str) -> Jogada:
        peca = self._tabuleiro.busca_pecas(pecas)
        jogada = self._agent.melhorJogada(self._tabuleiro, peca) ## Busca a melhor jogada
        if jogada:
            self._tabuleiro.faz_jogada(peca, jogada)
            peca.reseta_jogadas ## Reseta as jogadas
            return jogada
        else:
            return None

    ## Pega o score do game
    def get_game_score(self) -> Tuple[int, int]:
        return self._tabuleiro.game_score
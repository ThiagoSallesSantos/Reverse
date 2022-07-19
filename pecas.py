from typing import List, Tuple, Union

class Pecas:
    
    __slots__ = ('_cor', '_posicao_pecas', '_jogadas_disponiveis', '_ganho_jogada')

    def __init__(self, cor: str, posicoes_iniciais: List[Tuple[int, int]]) -> None:
        self._cor = cor
        self._posicao_pecas = [] + posicoes_iniciais
        self._jogadas_disponiveis = dict({})
        self._ganho_jogada = dict({})

    def set_jogada_disponivel(self, args: Union[Tuple[str, Tuple[int, int], int], Tuple[str, None]]) -> None:
        if args:
            self._jogadas_disponiveis.update(dict({args[0] : args[1]}))
            self._ganho_jogada.update({args[1] : args[2]})

    def adiciona_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None:
        self._posicao_pecas += lista_posicoes
        self._reseta_jogadas_disponiveis

    def remove_posicao(self, lista_posicoes: List[Tuple[int, int]]) -> None:
        for posicao in lista_posicoes:
            if posicao in self._posicao_pecas:
                self._posicao_pecas.remove(posicao)

    def consulta_jogada(self, posicao: Tuple[int, int]) -> bool:
        if posicao in self._jogadas_disponiveis.values():
            return True, list(self._jogadas_disponiveis.keys())[list(self._jogadas_disponiveis.values()).index(posicao)]
        return False, None

    @property
    def _reseta_jogadas_disponiveis(self):
        self._jogadas_disponiveis = dict({})
        self._ganho_jogada = dict({})

    @property
    def lista_jogadas(self) -> List[Tuple[Tuple[int, int], int]]:
        return sorted(list(self._ganho_jogada.items()), key=lambda y: y[1], reverse=True)

    @property
    def lista_posicoes(self) -> List[Tuple[int, int]]:
        return self._posicao_pecas
    
    @property
    def cor(self) -> str:
        return self._cor

from tkinter import *
from typing import Tuple, List
from reverse import Reverse
from functools import partial

class Interface:

    __slots__ = ('_janela', '_lista_botoes', '_label', '_cores', '_reverse', '_bot')

    def __init__(self, tamanho: Tuple[int, int]) -> "Interface":
        self._janela = Tk()
        self._lista_botoes = None
        self._label = Label(self._janela, bg="#FFFFFF", anchor=CENTER, font=('Helvetica 14 bold'), pady=10)
        self._cores = dict({"verde" : "#00BB0D", 
                        "verdeEsc" : "#006E07", 
                        "vermelho" : "#FF040F",
                        "vermelhoEsc" : "#8C030A",
                        "azul" : "",
                        "P": "#000000",
                        "B": "#FFFFFF"})
        self._config()
        self._monta_tabela(tamanho, "verde", "verdeEsc")
        self._reverse = Reverse()
        self._bot = None

    def _config(self) -> None:
        self._janela.title("Reverse")
        self._janela.geometry("900x680")
        self._janela.config(bg="#FFFFFF")
    
    def _monta_tabela(self, tamanho: Tuple[int, int], cor:str, corEsc:str) -> None:
        self._label.pack()
        tabela = Frame(self._janela)
        tabela.config(bg="#FFFFFF")
        tabela.place(relx = 0.1, rely = 0.1, relwidth = 0.8, relheight = 0.8)
        self._lista_botoes = []
        x = 1/tamanho[0]
        y = 1/tamanho[1]
        for i in range(tamanho[0]):
            self._lista_botoes.append([])
            for j in range(tamanho[1]):
                funcao = partial(self._jogada, i, j)
                self._lista_botoes[i].append(Button(tabela))
                self._lista_botoes[i][j].config(bg=self._cores["verde"], borderwidth=1, activebackground=self._cores["verdeEsc"], command = funcao)
                self._lista_botoes[i][j].place(relx = y*j, rely = x*i, relwidth = y, relheight = x)

    def _alerta(self, texto:str, cor:str) -> None:
        self._label.configure(text=texto, fg=cor)

    def _jogada(self, x:int, y:int) -> None:
        jogada = self._reverse.valida_jogada('P', (x, y))
        if not jogada:
            self._alerta("Jogada invalida", self._cores["vermelho"])
            return
        destinos = self._reverse.realiza_jogada('P', jogada)
        self._atualiza_tabela(jogada.caminho, self._cores['P'], self._cores['P'])
        self._atualiza_tabela(destinos, self._cores['verde'], self._cores["verdeEsc"])
        self._alerta("Agente jogando", self._cores["P"])
        self._ultima_jogada_agent(False)
        jogada = self._reverse.agente("B")
        self._bot = jogada.destino
        self._ultima_jogada_agent(True)
        self._atualiza_tabela(jogada.caminho, self._cores['B'], self._cores['B'])
        self._mostra_jogadas()

    def _mostra_jogadas(self) -> None:
        self._atualiza_tabela([x.destino for x in self._reverse.get_jogadas_disp('P')], self._cores["vermelho"], self._cores["vermelhoEsc"])
        self._alerta("Faça sua jogada", self._cores["P"])

    def _ultima_jogada_agent(self, add:bool):
        if add:
            self._lista_botoes[self._bot[0]][self._bot[1]].configure(text="X")
        elif self._bot:
            self._lista_botoes[self._bot[0]][self._bot[1]].configure(text="")

    def _atualiza_tabela(self, posicoes:List[Tuple[int, int]], cor:str, corEsc:str) -> None:
        for posicao in posicoes:
            self._lista_botoes[posicao[0]][posicao[1]].configure(bg=cor)
            self._lista_botoes[posicao[0]][posicao[1]].configure(activebackground=corEsc)

    def start(self) -> None:
        for pecas_posicoes in self._reverse.start():
            self._atualiza_tabela(pecas_posicoes[1], self._cores[pecas_posicoes[0]], self._cores[pecas_posicoes[0]])
        self._mostra_jogadas()
        self._janela.mainloop()


    
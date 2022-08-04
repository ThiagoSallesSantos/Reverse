from tkinter import *
from typing import Tuple, List
from reverse import Reverse
from functools import partial

## Classe Interface, responsável por criar e gerenciar a interface
class Interface:

    __slots__ = ('_janela', '_lista_botoes', '_label', '_cores', '_reverse', '_bot', '_label_score', '_rodando')

    def __init__(self, tamanho: Tuple[int, int]) -> "Interface": ## Contrutor da classe
        self._janela = Tk() ## Cria a janela
        self._lista_botoes = None
        self._label = Label(self._janela, bg="#FFFFFF", anchor=CENTER, font=('Helvetica 14 bold'), pady=10)
        self._label_score = Label(self._janela, bg="#FFFFFF", anchor=CENTER, font=('Helvetica 14 bold'), pady=10)
        self._cores = dict({"verde" : "#00BB0D", 
                        "verdeEsc" : "#006E07", 
                        "vermelho" : "#FF040F",
                        "vermelhoEsc" : "#8C030A",
                        "azul" : "",
                        "P": "#000000",
                        "B": "#FFFFFF"})
        self._config() ## Realiza configuração da janela
        self._rodando = True ## Variavel para saber se o jogo finalizou
        self._reverse = Reverse() ## Instância do jogo reverse, que irá ser usado para pode consumir jogo e sua regras
        self._monta_tabela(tamanho, "verde", "verdeEsc") ## Monta a tabela/janela
        self._bot = None ## Variavel para saber onde foi que bot escolheu ir

    def _config(self) -> None: ## Realiza configuração da janela
        self._janela.title("Reverse")
        self._janela.geometry("900x680")
        self._janela.config(bg="#FFFFFF")
    
    ## Metodo para montar a tabela na janela
    def _monta_tabela(self, tamanho: Tuple[int, int], cor:str, corEsc:str) -> None:
        self._update_score()
        self._label.pack()
        self._label_score.pack()
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
    
    # metodo que atualiza score do jogo na interface
    def _update_score(self):
        score_brancas, score_pretas = self._reverse.get_game_score()
        self._label_score.configure(text="Brancas {} : {} Pretas".format(score_brancas, score_pretas), fg=self._cores["P"])

    # metodo que muda texto do alerta
    def _alerta(self, texto:str, cor:str) -> None:
        self._label.configure(text=texto, fg=cor)

    ## Metodo que trata a jogada do usuário e também realiza a jogda do bot
    def _jogada(self, x:int, y:int) -> None:
        if self._rodando: ## Ver se o jogo já terminou
            ## Jogador jogando ##
            jogada = self._reverse.valida_jogada('P', (x, y))
            if not jogada: ## Ver se a jogada é valida
                self._alerta("Jogada invalida", self._cores["vermelho"])
                return
            destinos = self._reverse.realiza_jogada('P', jogada)
            self._atualiza_tabela(jogada.caminho, self._cores['P'], self._cores['P'])
            self._atualiza_tabela(destinos, self._cores['verde'], self._cores["verdeEsc"])
            ###############################
            ## Agente jogando ##
            if self._is_over('B'):## Ver se o jogo já terminou
                return
            self._alerta("Agente jogando", self._cores["P"])
            self._ultima_jogada_agent(False)
            jogada = self._reverse.agente("B")
            if jogada:
                self._bot = jogada.destino
                self._ultima_jogada_agent(True)
                self._atualiza_tabela(jogada.caminho, self._cores['B'], self._cores['B'])
                self._mostra_jogadas()
                self._update_score()
            if self._is_over('P'):## Ver se o jogo já terminou
                return
        
    # verifica se o jogo acabou, se sim finaliza o jogo
    def _is_over(self, color:str):
        jogadas_disp = self._reverse.get_jogadas_disp(color)
        if len(jogadas_disp) == 0:
            # Game over 
            self._alerta("GAME OVER!", cor=self._cores['vermelho'])
            self._rodando = False
            return True
        return False

    ## Exibi as jogadas disponiveis para o usuário
    def _mostra_jogadas(self) -> None:
        self._atualiza_tabela([x.destino for x in self._reverse.get_jogadas_disp('P')], self._cores["vermelho"], self._cores["vermelhoEsc"])
        self._alerta("Faça sua jogada", self._cores["P"])

    ## Exibi onde foi o destino escolhido pelo bot
    def _ultima_jogada_agent(self, add:bool):
        if add:
            self._lista_botoes[self._bot[0]][self._bot[1]].configure(text="X")
        elif self._bot:
            self._lista_botoes[self._bot[0]][self._bot[1]].configure(text="")

    ## Atualiza os estado da tabela, colocando as peças novas em seu respectivos lugares 
    def _atualiza_tabela(self, posicoes:List[Tuple[int, int]], cor:str, corEsc:str) -> None:
        for posicao in posicoes:
            self._lista_botoes[posicao[0]][posicao[1]].configure(bg=cor)
            self._lista_botoes[posicao[0]][posicao[1]].configure(activebackground=corEsc)

    ## Inicia a interface e o estado atual da tabela
    def start(self) -> None:
        for pecas_posicoes in self._reverse.start():
            self._atualiza_tabela(pecas_posicoes[1], self._cores[pecas_posicoes[0]], self._cores[pecas_posicoes[0]])
        self._mostra_jogadas()
        self._janela.mainloop()


    
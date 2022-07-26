from reverse import Reverse
from interface import Interface

if __name__ == '__main__':
    reverse = Interface((8,8))
    reverse.start()
    reverse.atualiza_tabela([(0,0), (7,7)])
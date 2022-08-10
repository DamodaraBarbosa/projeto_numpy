from classes_numpy import Catalog
import numpy as np
from utils.functions import linha, linha2, menu_ranking_cash, menu_ranking_fanscash, menu_ranking_fans, menu_ranking_fanslikes, menu_ranking_likes

class Analysis(Catalog):
    def __init__(self, strings, numbers ) -> None:
        super().__init__(strings, numbers)
        self.fanslikes = 0
        self.fanscash = 0
    
    def artists_ranking_conv_fanscash(self):
        self.fanscash = (self.numbers[:, 2]/self.numbers[:, 0]) * 100
        index_ranking_fans_cash = np.argsort(self.fanscash)
        name_of_artists = self.strings[:, 0][index_ranking_fans_cash]
        conversion_fans_cash = self.fanscash[index_ranking_fans_cash]
        ranking_fans_cash = np.array([name_of_artists, conversion_fans_cash])
        ranking_fans_cash_stacked = np.column_stack(ranking_fans_cash)

        menu_ranking_fanscash()

        for cont in range(-1, -11, -1):
            print(f'{-  cont}', end='')
            print(f'{"º":<11}', end='')
            print(f'\t{ranking_fans_cash_stacked[cont, 0]:<18}', end='')
            print(f'\t{ranking_fans_cash_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                print('\033[1;33m--\033[m'*30)
        print('\033[1;33m-=\033[m'*30)

    def artists_ranking_conv_fanslikes(self):
        #self.numbers[:, 1] equivale ao nº de curtidas e self.numbers[:, 0] ao nº de fãs
        self.fanslikes = (self.numbers[:, 1]/self.numbers[:, 0]) * 100
        index_ranking_fanslikes = np.argsort(self.fanslikes)
        # o uso de [index_ranking_fanslikes] ordena o nome dos artistas com maior conversão de fãs em likes
        name_of_artists = self.strings[:, 0][index_ranking_fanslikes]
        # o uso de [index_ranking_fanslikes] deixa a conversão de fãs em likes em ordem crescente
        conversion_fans_likes = self.fanslikes[index_ranking_fanslikes]
        ranking_fans_likes_1D = np.array([name_of_artists, conversion_fans_likes])
        ranking_fans_likes_2D = np.column_stack(ranking_fans_likes_1D)

        menu_ranking_fanslikes()

        for cont in range(-1, -11, -1):
            print(f'{-  cont}', end='')
            print(f'{"º":<11}', end='')
            print(f'\t{ranking_fans_likes_2D[cont, 0]:<18}', end='')
            print(f'\t{ranking_fans_likes_2D[cont, 1]}')
            if cont == -10:
                pass
            else:
                print('\033[1;33m--\033[m'*30)
        print('\033[1;33m-=\033[m'*30)

    def ranking_artists_fans(self):
        #argsort indica os indexs dos elementos em ordem do array
        index_ranking_fans = np.argsort(self.numbers[:, 0])
        number_of_fans_sorted = self.numbers[:, 0][index_ranking_fans]
        name_of_artists = self.strings[:, 0][index_ranking_fans]
        ranking_fans = np.array([name_of_artists, number_of_fans_sorted])
        ranking_fans_stacked = np.column_stack(ranking_fans)

        menu_ranking_fans()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_fans_stacked[cont, 0]:<20}', end='')
            print(f'\t{ranking_fans_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
    
    def ranking_artists_likes(self):
        index_ranking_likes = np.argsort(self.numbers[:, 1])
        name_of_artists = self.strings[:, 0][index_ranking_likes]
        number_of_likes_sorted = self.numbers[:, 1][index_ranking_likes]
        ranking_likes = np.array([name_of_artists, number_of_likes_sorted])
        ranking_likes_stacked = np.column_stack(ranking_likes)

        menu_ranking_likes()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_likes_stacked[cont, 0]:<22}', end='')
            print(f'\t{ranking_likes_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()
    
    def ranking_artists_cash(self):
        index_ranking_cash = np.argsort(self.numbers[:, 2])
        name_of_artist = self.strings[:, 0][index_ranking_cash]
        number_of_cash = self.numbers[:, 2][index_ranking_cash]
        ranking_cash = np.array([name_of_artist, number_of_cash])
        ranking_cash_stacked = np.column_stack(ranking_cash)

        menu_ranking_cash()

        for cont in range(-1, -11, -1):
            print(f'{- cont}', end='')
            print(f'{"º":<10}', end='')
            print(f'\t{ranking_cash_stacked[cont, 0]:<22}', end='')
            print(f'\t{ranking_cash_stacked[cont, 1]}')
            if cont == -10:
                pass
            else:
                linha()
        linha2()

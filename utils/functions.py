def linha():
    print('\033[1;33m--\033[m'*28)

def linha2():
    print('\033[1;33m-=\033[m'*28)

def menu_ranking_fans():
        linha2()
        print(f'{"                  TOP 10 ARTISTAS"}')
        linha2()
        print(f'{"Posição":<18}', end='')
        print(f'{"Artista":<25}', end='')
        print('Fãs')
        linha()
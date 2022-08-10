def linha():
    print('\033[1;33m--\033[m'*28)

def linha2():
    print('\033[1;33m-=\033[m'*28)

def menu_ranking_fans():
        linha2()
        print(f'{"                  TOP 10 ARTISTS"}')
        linha2()
        print(f'{"Placing":<18}', end='')
        print(f'{"Artist":<25}', end='')
        print('Fans')
        linha()

def menu_ranking_conversion():
        linha2()
        print(f'{"                  TOP 10 ARTISTS"}')
        linha2()
        print(f'{"Placing":<18}', end='')
        print(f'{"Artist":<25}', end='')
        print('Conversion (%)')
        linha()

def menu_ranking_likes():
        linha2()
        print(f'{"                  TOP 10 ARTISTS"}')
        linha2()
        print(f'{"Placing":<18}', end='')
        print(f'{"Artist":<24}', end='')
        print('Likes')
        linha()

def menu_ranking_cash():
        linha2()
        print(f'{"                  TOP 10 ARTISTS"}')
        linha2()
        print(f'{"Placing":<18}', end='')
        print(f'{"Artist":<24}', end='')
        print('Raise (USD)')
        linha()
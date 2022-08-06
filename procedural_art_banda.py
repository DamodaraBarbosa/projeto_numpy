from random import randint, uniform, choice, randrange

from matplotlib import artist
from func_art_banda import nome_eletronica, nome_funk, nome_hiphop, nome_indie, nome_mpb, nome_pop, nome_rock, nome_samba, nome_sertanejo, num_curtidas, num_fas, num_faturamento

art_banda = dict()
catalogo = list()


for contador in range(1, 11):
    generos = ['MPB', 'Rock', 'Indie', 'Funk', 'Sertanejo', 'Hip hop', 'Samba', 'Pop', 'Eletronica']
    genero_random = choice(generos)

    if genero_random == 'MPB':
        art_banda['nome'] = f'{nome_mpb(randint(1, 100))}'
        art_banda['gênero'] = 'MPB'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Pop':
        art_banda['nome'] = f'{nome_pop(randint(1, 100))}'
        art_banda['gênero'] = 'Pop'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Funk':
        art_banda['nome'] = f'{nome_funk(randint(1, 100))}'
        art_banda['gênero'] = 'Funk'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Hip hop':
        art_banda['nome'] = f'{nome_hiphop(randint(1, 100))}'
        art_banda['gênero'] = 'Hiphop'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Indie':
        art_banda['nome'] = f'{nome_indie(randint(1, 100))}'
        art_banda['gênero'] = 'Indie'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Sertanejo':
        art_banda['nome'] = f'{nome_sertanejo(randint(1, 100))}'
        art_banda['gênero'] = 'Sertanejo'
        if '&' in art_banda['nome']:
            art_banda['tipo'] = 'Dupla'
        else:
            art_banda['tipo'] = 'Solo'
    elif genero_random == 'Samba':
        art_banda['nome'] = f'{nome_samba(randint(1, 100))}'
        art_banda['gênero'] = 'Samba'
        art_banda['tipo'] = 'Solo'
    elif genero_random == 'Eletronica':
        art_banda['nome'] = f'{nome_eletronica(randint(1, 100))}'
        art_banda['gênero'] = 'Eletronica'
        art_banda['tipo'] = 'Solo'
    else:
        art_banda['nome'] = f'{nome_sertanejo(randint(1, 100))}'
        art_banda['gênero'] = 'Rock'
        art_banda['tipo'] = 'Banda'

    art_banda['fãs'] = num_fas(genero_random)
    art_banda['curtidas'] = num_curtidas(genero_random)
    art_banda['faturamento'] = num_faturamento(genero_random)
    catalogo.append(art_banda.copy())

texto_nome = ''
texto_genero = ''
texto_tipo = ''
texto_fans = ''
texto_curtidas = ''
texto_faturamento = ''
arquivo_nome = open('nome_catalogo.txt', 'w')
arquivo_genero = open('genero_catalogo.txt', 'w')
arquivo_tipo = open('tipo_catalogo.txt', 'w')
arquivo_fans = open('fans_catalogo.txt', 'w')
arquivo_curtidas = open('curtidas_catalogo.txt', 'w')
arquivo_faturamento = open('faturament_catalogo.txt', 'w')


for index, artistas in enumerate(catalogo):
    linha_nome = ''
    linha_nome += (f"{artistas['nome']}")
    linha_nome += '\n'
    texto_nome += f'{linha_nome}'
arquivo_nome.writelines(str(texto_nome))
arquivo_nome.close()

for index, artistas in enumerate(catalogo):
    linha_genero = ''
    linha_genero += f"{artistas['gênero']}"
    linha_genero += '\n'
    texto_genero += linha_genero
arquivo_genero.writelines(texto_genero)
arquivo_genero.close()

for index, artistas in enumerate(catalogo):
    linha_artistas = ''
    linha_artistas += f"{artistas['tipo']}"
    linha_artistas += '\n'
    texto_tipo += linha_artistas
arquivo_tipo.writelines(texto_tipo)
arquivo_tipo.close()

for index, artistas in enumerate(catalogo):
    linha_fans = ''
    linha_fans += f"{artistas['fãs']}"
    linha_fans += '\n'
    texto_fans += linha_fans
arquivo_fans.writelines(f'{texto_fans}')
arquivo_fans.close()

for index, artistas in enumerate(catalogo):
    linha_curtidas = ''
    linha_curtidas += f"{artistas['curtidas']}"
    linha_curtidas += '\n'
    texto_curtidas += linha_curtidas
arquivo_curtidas.writelines(texto_curtidas)
arquivo_curtidas.close()

for index, artistas in enumerate(catalogo):
    linha_faturamento = ''
    linha_faturamento += f"{artistas['faturamento']}"
    linha_faturamento += '\n'
    texto_faturamento += linha_faturamento
arquivo_faturamento.writelines(texto_faturamento)
arquivo_faturamento.close()
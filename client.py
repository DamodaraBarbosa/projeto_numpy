import numpy as np

nomes = np.loadtxt('nome_catalogo.txt', dtype=str)
generos = np.loadtxt('genero_catalogo.txt', dtype=str)
tipos = np.loadtxt('tipo_catalogo.txt', dtype=str)
fans = np.loadtxt('fans_catalogo.txt', dtype=int)
curtidas = np.loadtxt('curtidas_catalogo.txt', dtype=int)
faturamentos = np.loadtxt('faturament_catalogo.txt')

catalogo = np.array([nomes, generos, tipos, fans, curtidas, faturamentos])
print(catalogo)
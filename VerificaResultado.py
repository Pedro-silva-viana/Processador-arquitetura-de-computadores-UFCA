def preenche_matriz(N: int, inicio: int, string: str) -> tuple:
    saida = [[0 for _ in range(N)] for _ in range(N)]
    cont = 0
    for i in range(N):
        for j in range(N):
            saida[i][j] = int(string[inicio + cont], 16)
            cont += 1
    return (saida, inicio + cont)

N = int(input('Digite o tamanho das matrizes: '))
endereco = input('Digite o endereço do arquivo: ')

try:
    with open(endereco, 'r') as arquivo:
        arquivo.readline()
        codigo = arquivo.read().replace('\n', ' ').split()
        arquivo.close()

        a, cont = preenche_matriz(N, 0, codigo)
        b, cont = preenche_matriz(N, cont, codigo)
        c, _ = preenche_matriz(N, cont, codigo)

        for i in range(N):
            for j in range(N):
                produto = 0
                for k in range(N):
                    produto += a[i][k] * b[k][j]
                if c[i][j] != produto:
                    print('Resultado incorreto.')
                    exit()
        print('Resultado correto.')
except FileNotFoundError:
    print('Arquivo não encontrado.')
